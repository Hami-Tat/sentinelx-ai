"""
Deep Learning Detector.

Coordinates all deep learning detection models. Per
docs/04_Architecture.md, section 5.5.1, deep learning classifiers are
calibrated and aggregated the same way as Random Forest: they play
the "supervised" role (identifying a specific ThreatType), not the
"anomaly" role.

No deep learning framework (torch/tensorflow/keras) is currently a
project dependency, so this category has no concrete Detector
implementation yet: it is expected to stay empty (no available
detectors) until that framework decision is made.
"""

from __future__ import annotations

from sentinelx_ai.application.detection_engine.detector_group import (
    DetectorGroup,
)


class DeepLearningDetector(DetectorGroup):
    """
    Executes all registered deep learning detectors.
    """
