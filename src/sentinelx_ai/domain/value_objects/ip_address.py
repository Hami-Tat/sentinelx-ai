"""
IPAddress Value Object.

Represents a valid IPv4 or IPv6 address.
"""

from dataclasses import dataclass
from ipaddress import ip_address


@dataclass(frozen=True, slots=True)
class IPAddress:
    """
    Immutable Value Object representing an IP address.
    """

    value: str

    def __post_init__(self) -> None:
        """
        Validate the IP address after initialization.
        """
        try:
            ip_address(self.value)
        except ValueError as exc:
            raise ValueError(f"Invalid IP address: {self.value}") from exc

    @property
    def version(self) -> int:
        """
        Return the IP version (4 or 6).
        """
        return ip_address(self.value).version

    def __str__(self) -> str:
        return self.value
