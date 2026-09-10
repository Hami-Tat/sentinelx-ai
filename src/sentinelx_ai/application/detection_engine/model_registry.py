"""
Model Registry.

Stores and provides all available detectors.
"""

from __future__ import annotations

from sentinelx_ai.application.detection_engine.detector import (
    Detector,
)


class ModelRegistry:
    """
    Registry of all available detectors.
    """

    def __init__(self) -> None:
        self._detectors: dict[str, Detector] = {}

    def register(
        self,
        detector: Detector,
    ) -> None:
        """
        Register a detector.

        Raises:
            ValueError:
                If another detector with the same name already exists.
        """
        if detector.name in self._detectors:
            raise ValueError(f"Detector '{detector.name}' is already registered.")

        self._detectors[detector.name] = detector

    def unregister(
        self,
        detector_name: str,
    ) -> None:
        """
        Remove a detector from the registry.
        """
        self._detectors.pop(detector_name, None)

    def get_detector(
        self,
        detector_name: str,
    ) -> Detector:
        """
        Return a detector by name.

        Raises:
            KeyError:
                If the detector does not exist.
        """
        return self._detectors[detector_name]

    def get_detectors(self) -> list[Detector]:
        """
        Return every registered detector.
        """
        return list(self._detectors.values())

    def available_detectors(self) -> list[Detector]:
        """
        Return only detectors ready for inference.
        """
        return [
            detector for detector in self._detectors.values() if detector.is_available()
        ]

    def is_registered(
        self,
        detector_name: str,
    ) -> bool:
        """
        Check whether a detector is registered.
        """
        return detector_name in self._detectors

    def count(self) -> int:
        """
        Return the number of registered detectors.
        """
        return len(self._detectors)

    def clear(self) -> None:
        """
        Remove every detector from the registry.
        """
        self._detectors.clear()
