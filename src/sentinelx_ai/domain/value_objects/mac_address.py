"""
MACAddress Value Object.

Represents a valid MAC address.
"""

import re
from dataclasses import dataclass

_MAC_REGEX = re.compile(r"^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$")


@dataclass(frozen=True, slots=True)
class MACAddress:
    """
    Immutable Value Object representing a MAC address.
    """

    value: str

    def __post_init__(self) -> None:
        """
        Validate the MAC address.
        """
        if not _MAC_REGEX.fullmatch(self.value):
            raise ValueError(f"Invalid MAC address: {self.value}")

    def __str__(self) -> str:
        return self.value.upper()
