"""
Supervised Detector.

Coordinates all supervised machine learning models (e.g. Random
Forest). These detectors identify a specific ThreatType with a
calibrated confidence (see docs/04_Architecture.md, section 5.5.1).
"""

from __future__ import annotations

from sentinelx_ai.application.detection_engine.detector_group import (
    DetectorGroup,
)


class SupervisedDetector(DetectorGroup):
    """
    Executes all registered supervised detectors.
    """
