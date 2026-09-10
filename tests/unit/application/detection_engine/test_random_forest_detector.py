"""
Unit tests for RandomForestDetector.
"""

from __future__ import annotations

from pathlib import Path

import joblib
import pytest
from sklearn.ensemble import RandomForestClassifier

from sentinelx_ai.application.detection_engine.random_forest_detector import (
    RandomForestDetector,
)
from sentinelx_ai.application.feature_engine.feature_vector import (
    FeatureVector,
)
from sentinelx_ai.domain.enums.threat_type import ThreatType


def create_features() -> FeatureVector:
    return FeatureVector(packet_count=5, total_bytes=1000)


def train_and_save_model(model_path: Path) -> None:
    """Train a tiny RandomForestClassifier and save it as .joblib."""
    x_train = [
        [1, 100],
        [2, 150],
        [50, 60000],
        [60, 70000],
    ]
    y_train = [
        ThreatType.NORMAL.value,
        ThreatType.NORMAL.value,
        ThreatType.DOS.value,
        ThreatType.DOS.value,
    ]

    classifier = RandomForestClassifier(n_estimators=5, random_state=0)
    classifier.fit(x_train, y_train)

    joblib.dump(classifier, model_path)


def test_is_available_false_when_model_file_missing(tmp_path: Path) -> None:
    """No .joblib file at model_path => unavailable, not an exception."""
    detector = RandomForestDetector(
        model_path=tmp_path / "missing_model.joblib",
    )

    assert detector.is_available() is False


def test_detect_raises_when_unavailable(tmp_path: Path) -> None:
    """detect() must not be called on an unavailable detector."""
    detector = RandomForestDetector(
        model_path=tmp_path / "missing_model.joblib",
    )

    with pytest.raises(RuntimeError):
        detector.detect(create_features())


def test_is_available_true_when_model_loaded(tmp_path: Path) -> None:
    model_path = tmp_path / "random_forest.joblib"
    train_and_save_model(model_path)

    detector = RandomForestDetector(model_path=model_path, model_accuracy=0.95)

    assert detector.is_available() is True


def test_detect_returns_a_detection_result(tmp_path: Path) -> None:
    model_path = tmp_path / "random_forest.joblib"
    train_and_save_model(model_path)

    detector = RandomForestDetector(model_path=model_path, model_accuracy=0.95)

    result = detector.detect(
        FeatureVector(packet_count=55, total_bytes=65000),
    )

    assert result.detector_name == "random_forest"
    assert isinstance(result.threat_type, ThreatType)
    assert 0.0 <= result.confidence.value <= 1.0
    assert result.model_accuracy.value == 0.95
