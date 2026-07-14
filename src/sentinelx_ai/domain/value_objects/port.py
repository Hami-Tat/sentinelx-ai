"""
Port Value Object.

Represents a valid network port.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Port:
    """
    Immutable Value Object representing a network port.
    """

    value: int

    def __post_init__(self) -> None:
        """
        Validate the port number.
        """
        if not 0 <= self.value <= 65535:
            raise ValueError(
                f"Invalid port number: {self.value}. "
                "A port must be between 0 and 65535."
            )

    def __int__(self) -> int:
        return self.value

    def __str__(self) -> str:
        return str(self.value)
