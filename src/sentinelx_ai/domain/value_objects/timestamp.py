"""
Timestamp Value Object.

Represents an immutable timestamp.
"""

from dataclasses import dataclass
from datetime import UTC, datetime


@dataclass(frozen=True, slots=True)
class Timestamp:
    """
    Immutable Value Object representing a timestamp.
    """

    value: datetime

    @classmethod
    def now(cls) -> "Timestamp":
        """
        Create a Timestamp with the current UTC date and time.
        """
        return cls(datetime.now(UTC))

    def __str__(self) -> str:
        return self.value.isoformat()
