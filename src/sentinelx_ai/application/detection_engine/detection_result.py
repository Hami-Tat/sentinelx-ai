"""
Detection Result.

Represents the prediction produced by a detector.
"""

from __future__ import annotations

from dataclasses import dataclass

from sentinelx_ai.domain.enums.threat_type import ThreatType
from sentinelx_ai.domain.value_objects.probability import Probability


@dataclass(frozen=True, slots=True)
class DetectionResult:
    """
    Standard detection result returned by every detector.

    ``model_accuracy`` is the accuracy of the model that produced this
    result (``MLModel.accuracy``). EnsembleManager uses it as the
    detector's weight when aggregating results (see
    docs/04_Architecture.md, section 5.5.1).
    """

    detector_name: str
    threat_type: ThreatType
    confidence: Probability
    model_accuracy: Probability

    @property
    def is_threat(self) -> bool:
        """
        Return True if the prediction is not NORMAL.
        """
        return self.threat_type != ThreatType.NORMAL

    def __str__(self) -> str:
        """
        Human-readable representation.
        """
        return f"{self.detector_name}: {self.threat_type.value} ({self.confidence})"
