"""
Anomaly Detector.

Coordinates all anomaly detection models (e.g. Isolation Forest,
One-Class SVM, AutoEncoder). These detectors do not identify a
specific ThreatType: they only signal abnormal behaviour, which
EnsembleManager uses to corroborate a supervised proposal or to
detect Zero-Day attacks (see docs/04_Architecture.md, section 5.5.1).
"""

from __future__ import annotations

from sentinelx_ai.application.detection_engine.detector_group import (
    DetectorGroup,
)


class AnomalyDetector(DetectorGroup):
    """
    Executes all registered anomaly detection models.
    """
