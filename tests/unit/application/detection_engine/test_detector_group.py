"""
Unit tests for DetectorGroup and its named subclasses
(AnomalyDetector, SupervisedDetector, DeepLearningDetector).
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
from sentinelx_ai.application.detection_engine.detector import Detector
from sentinelx_ai.application.detection_engine.detector_group import (
    DetectorGroup,
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
    """Minimal Detector test double."""

    def __init__(
        self,
        detector_name: str = "fake",
        available: bool = True,
    ) -> None:
        self._detector_name = detector_name
        self._available = available

    @property
    def name(self) -> str:
        return self._detector_name

    def is_available(self) -> bool:
        return self._available

    def detect(self, features: FeatureVector) -> DetectionResult:
        return DetectionResult(
            detector_name=self._detector_name,
            threat_type=ThreatType.DOS,
            confidence=Probability(0.9),
            model_accuracy=Probability(0.8),
        )


def create_features() -> FeatureVector:
    return FeatureVector(packet_count=5, total_bytes=1000)


def test_detect_only_calls_available_detectors() -> None:
    """Unavailable detectors must be skipped, not called."""
    group = DetectorGroup(
        detectors=[
            FakeDetector("available", available=True),
            FakeDetector("unavailable", available=False),
        ],
    )

    results = group.detect(create_features())

    assert [result.detector_name for result in results] == ["available"]


def test_detector_count() -> None:
    group = DetectorGroup(
        detectors=[
            FakeDetector("a", available=True),
            FakeDetector("b", available=False),
        ],
    )

    assert group.detector_count() == 2


def test_available_detector_count() -> None:
    group = DetectorGroup(
        detectors=[
            FakeDetector("a", available=True),
            FakeDetector("b", available=False),
            FakeDetector("c", available=True),
        ],
    )

    assert group.available_detector_count() == 2


def test_named_subclasses_share_detector_group_behaviour() -> None:
    """
    AnomalyDetector, SupervisedDetector and DeepLearningDetector must
    all behave like DetectorGroup (no duplicated/diverging logic)
    while remaining distinct, named types.
    """
    for group_class in (AnomalyDetector, SupervisedDetector, DeepLearningDetector):
        group = group_class(
            detectors=[
                FakeDetector("available", available=True),
                FakeDetector("unavailable", available=False),
            ],
        )

        assert isinstance(group, DetectorGroup)
        assert group.detector_count() == 2
        assert group.available_detector_count() == 1
        assert [result.detector_name for result in group.detect(create_features())] == [
            "available"
        ]
