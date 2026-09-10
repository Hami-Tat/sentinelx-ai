"""
Random Forest Detector.

Concrete supervised Detector wrapping a
sklearn.ensemble.RandomForestClassifier trained to recognise
ThreatType categories from a FeatureVector.
"""

from __future__ import annotations

from pathlib import Path

import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier

from sentinelx_ai.application.detection_engine.detection_result import (
    DetectionResult,
)
from sentinelx_ai.application.detection_engine.detector import (
    Detector,
)
from sentinelx_ai.application.feature_engine.feature_vector import (
    FeatureVector,
)
from sentinelx_ai.domain.enums.threat_type import ThreatType
from sentinelx_ai.domain.value_objects.probability import Probability


class RandomForestDetector(Detector):
    """
    Supervised detector backed by a trained RandomForestClassifier.

    The classifier is expected to have been trained with
    ``ThreatType.value`` strings as class labels, so that
    ``model.classes_`` can be mapped back to ``ThreatType`` directly.
    """

    def __init__(
        self,
        model_path: Path | str,
        model_accuracy: float = 0.0,
    ) -> None:
        """
        Args:
            model_path:
                Path to the trained model, serialized with joblib
                (``.joblib``). If the file does not exist, the
                detector stays unavailable instead of raising.
            model_accuracy:
                Accuracy of the loaded model (``MLModel.accuracy``),
                used by EnsembleManager as this detector's weight.
                Loading MLModel metadata from persistence is out of
                scope here: the caller supplies it directly.
        """
        self._model_path = Path(model_path)
        self._model_accuracy = model_accuracy
        self._model: RandomForestClassifier | None = self._load_model()

    def _load_model(self) -> RandomForestClassifier | None:
        """
        Load the trained model from disk, or None if unavailable.
        """
        if not self._model_path.is_file():
            return None

        return joblib.load(self._model_path)

    @property
    def name(self) -> str:
        """
        Return the detector name.
        """
        return "random_forest"

    def is_available(self) -> bool:
        """
        Return whether a trained model was successfully loaded.
        """
        return self._model is not None

    def detect(
        self,
        features: FeatureVector,
    ) -> DetectionResult:
        """
        Predict a ThreatType from a feature vector.

        Args:
            features:
                Extracted feature vector.

        Returns:
            DetectionResult with the predicted ThreatType and its
            calibrated confidence.

        Raises:
            RuntimeError:
                If called while no model is loaded. Callers should
                check is_available() first (DetectorGroup already
                does this before calling detect()).
        """
        if self._model is None:
            raise RuntimeError(
                "RandomForestDetector.detect() called while unavailable "
                "(no model loaded)."
            )

        feature_array = np.array(
            [[features.packet_count, features.total_bytes]],
        )

        # TODO calibration: sklearn.calibration.CalibratedClassifierCV
        # (Platt scaling / isotonic regression, per 5.5.1) requires a
        # labelled validation set that does not exist yet. Until then,
        # predict_proba is used directly as an approximation of the
        # calibrated confidence.
        probabilities = self._model.predict_proba(feature_array)[0]

        best_index = int(np.argmax(probabilities))
        threat_type = ThreatType(self._model.classes_[best_index])
        confidence = Probability(float(probabilities[best_index]))

        return DetectionResult(
            detector_name=self.name,
            threat_type=threat_type,
            confidence=confidence,
            model_accuracy=Probability(self._model_accuracy),
        )
