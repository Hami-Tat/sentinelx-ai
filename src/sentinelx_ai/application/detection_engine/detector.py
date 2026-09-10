"""
Detector interface.

Defines the common contract for every detection model used
by SentinelX AI.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from sentinelx_ai.application.detection_engine.detection_result import (
    DetectionResult,
)
from sentinelx_ai.application.feature_engine.feature_vector import (
    FeatureVector,
)


class Detector(ABC):
    """
    Base interface for every detector.

    Every supervised, anomaly-based and deep learning detector
    must implement this contract.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Return the detector name.
        """

    @abstractmethod
    def detect(
        self,
        features: FeatureVector,
    ) -> DetectionResult:
        """
        Analyse a feature vector.

        Args:
            features:
                Extracted feature vector.

        Returns:
            DetectionResult produced by the detector.
        """

    @abstractmethod
    def is_available(self) -> bool:
        """
        Return whether the detector is ready for inference.
        """
