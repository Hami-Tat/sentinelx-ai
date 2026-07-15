"""
Machine Learning Model Repository Interface.
"""

from abc import ABC, abstractmethod

from sentinelx_ai.domain.entities.ml_model import MLModel


class MLModelRepository(ABC):
    """
    Repository interface for ML models.
    """

    @abstractmethod
    def save(self, model: MLModel) -> None:
        """Save a machine learning model."""

    @abstractmethod
    def get_all(self) -> list[MLModel]:
        """Return all machine learning models."""

    @abstractmethod
    def delete_all(self) -> None:
        """Delete all machine learning models."""
