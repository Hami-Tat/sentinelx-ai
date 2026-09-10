"""
Detection Service.

Orchestrates the Detection Engine: runs every available detector by
category and aggregates their results into a single DetectionResult.
"""

from __future__ import annotations

from sentinelx_ai.application.detection_engine.anomaly_detector import (
    AnomalyDetector,
)
from sentinelx_ai.application.detection_engine.deep_learning_detector import (
    DeepLearningDetector,
)
from sentinelx_ai.application.detection_engine.detection_result import (
    DetectionResult,
)
from sentinelx_ai.application.detection_engine.ensemble_manager import (
    EnsembleManager,
)
from sentinelx_ai.application.detection_engine.supervised_detector import (
    SupervisedDetector,
)
from sentinelx_ai.application.feature_engine.feature_vector import (
    FeatureVector,
)
from sentinelx_ai.domain.enums.threat_type import ThreatType
from sentinelx_ai.domain.value_objects.probability import Probability

_NO_DETECTION_RESULT = DetectionResult(
    detector_name="ensemble",
    threat_type=ThreatType.UNKNOWN,
    confidence=Probability(0.0),
    model_accuracy=Probability(0.0),
)


class DetectionService:
    """
    Main entry point for the Detection Engine.

    Built directly from the three DetectorGroup coordinators rather
    than from ModelRegistry: ModelRegistry stores detectors as a flat,
    unordered collection and has no notion of category (supervised /
    anomaly / deep learning), which EnsembleManager needs to apply the
    5.5.1 aggregation roles. Composing the groups explicitly keeps
    that categorization visible and easy to test; ModelRegistry
    remains available for a future composition root that dynamically
    builds these groups from configuration.

    Per docs/04_Architecture.md, section 5.5.1, deep learning
    classifiers play the same "supervised" aggregation role as Random
    Forest (both identify a specific ThreatType), so their results are
    merged with SupervisedDetector's before being passed to
    EnsembleManager.
    """

    def __init__(
        self,
        supervised_detector: SupervisedDetector,
        anomaly_detector: AnomalyDetector,
        deep_learning_detector: DeepLearningDetector,
        ensemble_manager: EnsembleManager,
    ) -> None:
        self._supervised_detector = supervised_detector
        self._anomaly_detector = anomaly_detector
        self._deep_learning_detector = deep_learning_detector
        self._ensemble_manager = ensemble_manager

    def detect(
        self,
        features: FeatureVector,
    ) -> DetectionResult:
        """
        Run every available detector and return the aggregated
        DetectionResult.

        Args:
            features:
                Feature vector produced by the Feature Engine.

        Returns:
            The DetectionResult produced by EnsembleManager, or a
            zero-confidence ThreatType.UNKNOWN result if no detector
            was available at all.
        """
        supervised_results = self._supervised_detector.detect(
            features,
        ) + self._deep_learning_detector.detect(features)

        anomaly_results = self._anomaly_detector.detect(features)

        combined = self._ensemble_manager.combine(
            supervised_results,
            anomaly_results,
        )

        if combined is None:
            return _NO_DETECTION_RESULT

        return combined
