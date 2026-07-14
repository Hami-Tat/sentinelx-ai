"""
Probability Value Object.

Represents a probability between 0.0 and 1.0.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Probability:
    """
    Immutable Value Object representing a probability.
    """

    value: float

    def __post_init__(self) -> None:
        if not 0.0 <= self.value <= 1.0:
            raise ValueError("Probability must be between 0.0 and 1.0.")

    def percentage(self) -> float:
        """
        Return the probability as a percentage.
        """
        return self.value * 100

    def __float__(self) -> float:
        return self.value

    def __str__(self) -> str:
        return f"{self.value:.4f}"
