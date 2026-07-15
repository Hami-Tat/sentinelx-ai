"""
Machine Learning Model Entity.
"""

from dataclasses import dataclass

from sentinelx_ai.domain.value_objects.timestamp import Timestamp


@dataclass(slots=True)
class MLModel:
    """
    Entity representing a Machine Learning model.
    """

    identifier: str
    name: str
    version: str
    accuracy: float
    created_at: Timestamp
