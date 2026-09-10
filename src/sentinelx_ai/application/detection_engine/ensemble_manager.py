"""
Ensemble Manager.

Aggregates calibrated detection results into a single DetectionResult,
following the aggregation rule defined in docs/04_Architecture.md,
section 5.5.1 ("Calibration et Agrégation des Scores de Confiance").
"""

from __future__ import annotations

from collections.abc import Callable

from sentinelx_ai.application.detection_engine.detection_result import (
    DetectionResult,
)
from sentinelx_ai.domain.enums.threat_type import ThreatType
from sentinelx_ai.domain.value_objects.probability import Probability

_DEFAULT_DECISION_THRESHOLD = 0.5
_DEFAULT_CORROBORATION_CAP = 0.2

_ENSEMBLE_DETECTOR_NAME = "ensemble"


class EnsembleManager:
    """
    Combines supervised and anomaly detection results into one
    aggregated DetectionResult.

    Roles (see 5.5.1):
        - Supervised results (Random Forest, Deep Learning) each
          identify a specific ThreatType with a calibrated
          confidence.
        - Anomaly results (Isolation Forest, One-Class SVM,
          AutoEncoder) carry no specific ThreatType: they only
          corroborate a supervised proposal, or, alone, signal a
          possible Zero-Day attack.
    """

    def __init__(
        self,
        decision_threshold: float = _DEFAULT_DECISION_THRESHOLD,
        corroboration_cap: float = _DEFAULT_CORROBORATION_CAP,
    ) -> None:
        """
        Args:
            decision_threshold:
                Minimum final confidence required to keep the
                aggregated threat type (also used to decide whether
                an anomaly-only signal counts as "strong"). Below
                this threshold, the result is reclassified as
                ThreatType.UNKNOWN and should be escalated for human
                review rather than forwarded automatically to the
                Decision Engine.
            corroboration_cap:
                Maximum confidence boost a supervised proposal can
                receive from corroborating anomaly detectors.

        Raises:
            ValueError:
                If either threshold is not between 0.0 and 1.0.
        """
        if not 0.0 <= decision_threshold <= 1.0:
            raise ValueError(
                "decision_threshold must be between 0.0 and 1.0.",
            )

        if not 0.0 <= corroboration_cap <= 1.0:
            raise ValueError(
                "corroboration_cap must be between 0.0 and 1.0.",
            )

        self._decision_threshold = decision_threshold
        self._corroboration_cap = corroboration_cap

    def combine(
        self,
        supervised_results: list[DetectionResult],
        anomaly_results: list[DetectionResult],
    ) -> DetectionResult | None:
        """
        Aggregate supervised and anomaly detection results.

        Args:
            supervised_results:
                Calibrated results from Random Forest / Deep Learning
                detectors, each proposing a specific ThreatType.
            anomaly_results:
                Calibrated results from Isolation Forest / One-Class
                SVM / AutoEncoder detectors, used only as a
                corroboration signal.

        Returns:
            The aggregated DetectionResult, or None if both lists are
            empty (no detector was available).
        """
        anomaly_confidence = self._weighted_average(
            anomaly_results,
            lambda result: result.confidence.value,
        )

        if supervised_results:
            result = self._combine_supervised(
                supervised_results,
                anomaly_confidence,
            )
        elif anomaly_results:
            result = self._combine_anomaly_only(
                anomaly_results,
                anomaly_confidence,
            )
        else:
            return None

        if result.confidence.value < self._decision_threshold:
            result = DetectionResult(
                detector_name=result.detector_name,
                threat_type=ThreatType.UNKNOWN,
                confidence=result.confidence,
                model_accuracy=result.model_accuracy,
            )

        return result

    def _combine_supervised(
        self,
        supervised_results: list[DetectionResult],
        anomaly_confidence: float,
    ) -> DetectionResult:
        """
        Weighted-average the confidence of every ThreatType proposed
        by supervised detectors, keep the best-supported one, and
        boost it with any anomaly corroboration signal.
        """
        weights = self._normalized_weights(supervised_results)

        weighted_sum: dict[ThreatType, float] = {}
        weight_total: dict[ThreatType, float] = {}

        for result in supervised_results:
            weight = weights[result.detector_name]
            weighted_sum[result.threat_type] = (
                weighted_sum.get(result.threat_type, 0.0)
                + weight * result.confidence.value
            )
            weight_total[result.threat_type] = (
                weight_total.get(result.threat_type, 0.0) + weight
            )

        averages = {
            threat_type: weighted_sum[threat_type] / weight_total[threat_type]
            for threat_type in weighted_sum
        }
        best_type = max(averages, key=lambda threat_type: averages[threat_type])
        base_confidence = averages[best_type]

        boosted_confidence = min(
            1.0,
            base_confidence + anomaly_confidence * self._corroboration_cap,
        )

        model_accuracy = self._weighted_average(
            supervised_results,
            lambda result: result.model_accuracy.value,
        )

        return DetectionResult(
            detector_name=_ENSEMBLE_DETECTOR_NAME,
            threat_type=best_type,
            confidence=Probability(boosted_confidence),
            model_accuracy=Probability(model_accuracy),
        )

    def _combine_anomaly_only(
        self,
        anomaly_results: list[DetectionResult],
        anomaly_confidence: float,
    ) -> DetectionResult:
        """
        No supervised detector proposed a type: a strong anomaly
        signal alone is reported as a possible Zero-Day attack.
        """
        model_accuracy = self._weighted_average(
            anomaly_results,
            lambda result: result.model_accuracy.value,
        )

        return DetectionResult(
            detector_name=_ENSEMBLE_DETECTOR_NAME,
            threat_type=ThreatType.ZERO_DAY,
            confidence=Probability(anomaly_confidence),
            model_accuracy=Probability(model_accuracy),
        )

    @staticmethod
    def _weighted_average(
        results: list[DetectionResult],
        value_of: Callable[[DetectionResult], float],
    ) -> float:
        """
        Weighted average of value_of(result) over results, weighted
        by each detector's normalized accuracy. Returns 0.0 for an
        empty list.
        """
        if not results:
            return 0.0

        weights = EnsembleManager._normalized_weights(results)

        return sum(
            weights[result.detector_name] * value_of(result) for result in results
        )

    @staticmethod
    def _normalized_weights(
        results: list[DetectionResult],
    ) -> dict[str, float]:
        """
        Normalize each result's model_accuracy so the weights of the
        given (already available-only) results sum to 1.0.

        Results are provided only by detectors for which
        is_available() was True: an unavailable detector never
        produces a result, so it is naturally excluded from this
        pool and its weight is redistributed among the others. Falls
        back to equal weights if every accuracy is zero.
        """
        total_accuracy = sum(result.model_accuracy.value for result in results)

        if total_accuracy <= 0.0:
            equal_weight = 1.0 / len(results)
            return {result.detector_name: equal_weight for result in results}

        return {
            result.detector_name: result.model_accuracy.value / total_accuracy
            for result in results
        }
