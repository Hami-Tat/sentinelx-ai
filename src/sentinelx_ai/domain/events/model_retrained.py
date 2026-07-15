"""
Model Retrained Domain Event.
"""

from dataclasses import dataclass

from sentinelx_ai.domain.entities.ml_model import MLModel


@dataclass(frozen=True, slots=True)
class ModelRetrained:
    """
    Event raised when an ML model is retrained.
    """

    model: MLModel
