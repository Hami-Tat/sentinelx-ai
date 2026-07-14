"""
RiskScore Value Object.

Represents a risk score between 0 and 100.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class RiskScore:
    """
    Immutable Value Object representing a risk score.
    """

    value: int

    def __post_init__(self) -> None:
        if not 0 <= self.value <= 100:
            raise ValueError("Risk score must be between 0 and 100.")

    @property
    def normalized(self) -> float:
        """
        Return the normalized risk score.
        """
        return self.value / 100

    def __int__(self) -> int:
        return self.value

    def __str__(self) -> str:
        return str(self.value)
