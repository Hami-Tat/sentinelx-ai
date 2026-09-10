"""
Unit tests for EnsembleManager.

Covers the aggregation rule defined in docs/04_Architecture.md,
section 5.5.1: weighted-average of supervised confidences by
MLModel.accuracy, corroboration boost from anomaly detectors,
Zero-Day classification from anomaly-only signals, and the
configurable decision threshold.
"""

from __future__ import annotations

import pytest

from sentinelx_ai.application.detection_engine.detection_result import (
    DetectionResult,
)
from sentinelx_ai.application.detection_engine.ensemble_manager import (
    EnsembleManager,
)
from sentinelx_ai.domain.enums.threat_type import ThreatType
from sentinelx_ai.domain.value_objects.probability import Probability


def make_result(
    detector_name: str,
    threat_type: ThreatType,
    confidence: float,
    model_accuracy: float,
) -> DetectionResult:
    return DetectionResult(
        detector_name=detector_name,
        threat_type=threat_type,
        confidence=Probability(confidence),
        model_accuracy=Probability(model_accuracy),
    )


def test_invalid_decision_threshold_raises() -> None:
    with pytest.raises(ValueError):
        EnsembleManager(decision_threshold=1.5)


def test_invalid_corroboration_cap_raises() -> None:
    with pytest.raises(ValueError):
        EnsembleManager(corroboration_cap=-0.1)


def test_combine_returns_none_when_no_results() -> None:
    manager = EnsembleManager()

    assert manager.combine([], []) is None


def test_simple_supervised_agreement() -> None:
    """A single supervised detector, no anomaly signal: confidence is
    passed through unchanged (no corroboration boost)."""
    manager = EnsembleManager(decision_threshold=0.5)

    supervised = [make_result("random_forest", ThreatType.DOS, 0.9, 0.8)]

    result = manager.combine(supervised, [])

    assert result.threat_type == ThreatType.DOS
    assert result.confidence.value == pytest.approx(0.9)


def test_anomaly_corroboration_boosts_confidence() -> None:
    """A corroborating anomaly detector boosts the supervised
    confidence, capped by corroboration_cap."""
    manager = EnsembleManager(decision_threshold=0.5, corroboration_cap=0.2)

    supervised = [make_result("random_forest", ThreatType.DOS, 0.7, 0.8)]
    anomaly = [make_result("isolation_forest", ThreatType.UNKNOWN, 0.9, 0.5)]

    result = manager.combine(supervised, anomaly)

    # boost = anomaly_confidence * corroboration_cap = 0.9 * 0.2 = 0.18
    assert result.threat_type == ThreatType.DOS
    assert result.confidence.value == pytest.approx(0.88)


def test_corroboration_boost_is_capped_at_one() -> None:
    manager = EnsembleManager(decision_threshold=0.5, corroboration_cap=0.5)

    supervised = [make_result("random_forest", ThreatType.DOS, 0.95, 0.8)]
    anomaly = [make_result("isolation_forest", ThreatType.UNKNOWN, 1.0, 0.5)]

    result = manager.combine(supervised, anomaly)

    assert result.confidence.value == pytest.approx(1.0)


def test_disagreement_with_low_confidence_becomes_unknown() -> None:
    """Two supervised detectors disagree on the threat type and both
    have a confidence below the decision threshold: the aggregated
    result must be reclassified as UNKNOWN."""
    manager = EnsembleManager(decision_threshold=0.5)

    supervised = [
        make_result("random_forest", ThreatType.DOS, 0.30, 0.5),
        make_result("secondary_model", ThreatType.PORT_SCAN, 0.35, 0.5),
    ]

    result = manager.combine(supervised, [])

    assert result.threat_type == ThreatType.UNKNOWN
    assert result.confidence.value == pytest.approx(0.35)


def test_unavailable_detector_excluded_from_weight_normalization() -> None:
    """Weights are normalized only across the results actually given
    to combine(). An unavailable detector never produces a
    DetectionResult (DetectorGroup filters it out before combine() is
    even called), so it cannot appear here and cannot dilute the
    weights of the detectors that did run."""
    manager = EnsembleManager(decision_threshold=0.5)

    supervised = [
        make_result("random_forest", ThreatType.DOS, 0.8, 0.9),
        make_result("secondary_model", ThreatType.DOS, 0.4, 0.3),
    ]

    result = manager.combine(supervised, [])

    # weights = 0.9 / 1.2 = 0.75 and 0.3 / 1.2 = 0.25
    # weighted average = 0.75 * 0.8 + 0.25 * 0.4 = 0.7
    assert result.threat_type == ThreatType.DOS
    assert result.confidence.value == pytest.approx(0.7)


def test_zero_accuracy_detectors_fall_back_to_equal_weights() -> None:
    manager = EnsembleManager(decision_threshold=0.5)

    supervised = [
        make_result("model_a", ThreatType.DOS, 0.6, 0.0),
        make_result("model_b", ThreatType.DOS, 0.8, 0.0),
    ]

    result = manager.combine(supervised, [])

    assert result.confidence.value == pytest.approx(0.7)


def test_strong_anomaly_only_signal_becomes_zero_day() -> None:
    """No supervised detector proposed a type, but anomaly detectors
    signal a strong anomaly: classified as Zero-Day."""
    manager = EnsembleManager(decision_threshold=0.5)

    anomaly = [make_result("isolation_forest", ThreatType.UNKNOWN, 0.9, 1.0)]

    result = manager.combine([], anomaly)

    assert result.threat_type == ThreatType.ZERO_DAY
    assert result.confidence.value == pytest.approx(0.9)


def test_weak_anomaly_only_signal_becomes_unknown() -> None:
    manager = EnsembleManager(decision_threshold=0.5)

    anomaly = [make_result("isolation_forest", ThreatType.UNKNOWN, 0.3, 1.0)]

    result = manager.combine([], anomaly)

    assert result.threat_type == ThreatType.UNKNOWN
    assert result.confidence.value == pytest.approx(0.3)
