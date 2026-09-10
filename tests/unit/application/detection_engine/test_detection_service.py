"""
Unit tests for DetectionService.
"""

from __future__ import annotations

import pytest

from sentinelx_ai.application.detection_engine.anomaly_detector import (
    AnomalyDetector,
)
from sentinelx_ai.application.detection_engine.deep_learning_detector import (
    DeepLearningDetector,
)
from sentinelx_ai.application.detection_engine.detection_result import (
    DetectionResult,
)
from sentinelx_ai.application.detection_engine.detection_service import (
    DetectionService,
)
from sentinelx_ai.application.detection_engine.detector import Detector
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


class FakeDetector(Detector):
    """Minimal Detector test double returning a fixed DetectionResult."""

    def __init__(
        self,
        detector_name: str,
        threat_type: ThreatType,
        confidence: float,
        model_accuracy: float,
        available: bool = True,
    ) -> None:
        self._detector_name = detector_name
        self._threat_type = threat_type
        self._confidence = confidence
        self._model_accuracy = model_accuracy
        self._available = available

    @property
    def name(self) -> str:
        return self._detector_name

    def is_available(self) -> bool:
        return self._available

    def detect(self, features: FeatureVector) -> DetectionResult:
        return DetectionResult(
            detector_name=self._detector_name,
            threat_type=self._threat_type,
            confidence=Probability(self._confidence),
            model_accuracy=Probability(self._model_accuracy),
        )


def create_features() -> FeatureVector:
    return FeatureVector(packet_count=5, total_bytes=1000)


def test_detect_returns_unknown_when_no_detector_available() -> None:
    service = DetectionService(
        supervised_detector=SupervisedDetector(detectors=[]),
        anomaly_detector=AnomalyDetector(detectors=[]),
        deep_learning_detector=DeepLearningDetector(detectors=[]),
        ensemble_manager=EnsembleManager(),
    )

    result = service.detect(create_features())

    assert result.threat_type == ThreatType.UNKNOWN
    assert result.confidence.value == pytest.approx(0.0)


def test_detect_uses_available_supervised_detector() -> None:
    service = DetectionService(
        supervised_detector=SupervisedDetector(
            detectors=[
                FakeDetector("random_forest", ThreatType.DOS, 0.9, 0.8),
            ],
        ),
        anomaly_detector=AnomalyDetector(detectors=[]),
        deep_learning_detector=DeepLearningDetector(detectors=[]),
        ensemble_manager=EnsembleManager(decision_threshold=0.5),
    )

    result = service.detect(create_features())

    assert result.threat_type == ThreatType.DOS
    assert result.confidence.value == pytest.approx(0.9)


def test_detect_skips_unavailable_detectors() -> None:
    service = DetectionService(
        supervised_detector=SupervisedDetector(
            detectors=[
                FakeDetector("unavailable", ThreatType.DOS, 0.99, 0.9, available=False),
            ],
        ),
        anomaly_detector=AnomalyDetector(detectors=[]),
        deep_learning_detector=DeepLearningDetector(detectors=[]),
        ensemble_manager=EnsembleManager(),
    )

    result = service.detect(create_features())

    assert result.threat_type == ThreatType.UNKNOWN
    assert result.confidence.value == pytest.approx(0.0)


def test_deep_learning_results_are_aggregated_with_supervised_results() -> None:
    """Per 5.5.1, deep learning detectors play the supervised role:
    their proposal must be weighted alongside SupervisedDetector's,
    not treated as a corroboration-only anomaly signal."""
    service = DetectionService(
        supervised_detector=SupervisedDetector(
            detectors=[
                FakeDetector("random_forest", ThreatType.DOS, 0.8, 0.9),
            ],
        ),
        anomaly_detector=AnomalyDetector(detectors=[]),
        deep_learning_detector=DeepLearningDetector(
            detectors=[
                FakeDetector("deep_net", ThreatType.DOS, 0.4, 0.3),
            ],
        ),
        ensemble_manager=EnsembleManager(decision_threshold=0.5),
    )

    result = service.detect(create_features())

    # weights = 0.9 / 1.2 = 0.75 and 0.3 / 1.2 = 0.25
    # weighted average = 0.75 * 0.8 + 0.25 * 0.4 = 0.7
    assert result.threat_type == ThreatType.DOS
    assert result.confidence.value == pytest.approx(0.7)


def test_anomaly_results_corroborate_supervised_result() -> None:
    service = DetectionService(
        supervised_detector=SupervisedDetector(
            detectors=[
                FakeDetector("random_forest", ThreatType.DOS, 0.7, 0.8),
            ],
        ),
        anomaly_detector=AnomalyDetector(
            detectors=[
                FakeDetector("isolation_forest", ThreatType.UNKNOWN, 0.9, 0.5),
            ],
        ),
        deep_learning_detector=DeepLearningDetector(detectors=[]),
        ensemble_manager=EnsembleManager(
            decision_threshold=0.5,
            corroboration_cap=0.2,
        ),
    )

    result = service.detect(create_features())

    assert result.threat_type == ThreatType.DOS
    assert result.confidence.value == pytest.approx(0.88)
