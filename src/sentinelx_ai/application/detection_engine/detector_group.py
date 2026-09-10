"""
Detector Group.

Common logic shared by every detector coordinator (Supervised,
Anomaly, Deep Learning). Each coordinator manages a list of Detector
instances of one category and executes only the ones that are
currently available.
"""

from __future__ import annotations

from sentinelx_ai.application.detection_engine.detection_result import (
    DetectionResult,
)
from sentinelx_ai.application.detection_engine.detector import (
    Detector,
)
from sentinelx_ai.application.feature_engine.feature_vector import (
    FeatureVector,
)


class DetectorGroup:
    """
    Executes every available detector of a given category.

    This base class holds the logic that used to be duplicated across
    AnomalyDetector, SupervisedDetector and DeepLearningDetector. Each
    of those remains a distinct, named subclass rather than being
    merged into one generic category, because they play different
    roles during aggregation (see docs/04_Architecture.md, section
    5.5.1): supervised detectors identify a specific ThreatType,
    while anomaly detectors only corroborate that proposal or signal
    a possible Zero-Day attack.
    """

    def __init__(
        self,
        detectors: list[Detector],
    ) -> None:
        self._detectors = detectors

    def detect(
        self,
        features: FeatureVector,
    ) -> list[DetectionResult]:
        """
        Execute every available detector of this group.

        Args:
            features:
                Feature vector produced by the Feature Engine.

        Returns:
            Detection results from every available detector.
        """
        results: list[DetectionResult] = []

        for detector in self._detectors:
            if detector.is_available():
                results.append(
                    detector.detect(features),
                )

        return results

    def detector_count(self) -> int:
        """
        Return the number of registered detectors in this group.
        """
        return len(self._detectors)

    def available_detector_count(self) -> int:
        """
        Return the number of available detectors in this group.
        """
        return sum(detector.is_available() for detector in self._detectors)
