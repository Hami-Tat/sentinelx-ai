"""
Packet Repository Interface.
"""

from abc import ABC, abstractmethod

from sentinelx_ai.domain.entities.packet import Packet


class PacketRepository(ABC):
    """
    Repository interface for Packet entities.
    """

    @abstractmethod
    def save(self, packet: Packet) -> None:
        """Save a packet."""

    @abstractmethod
    def get_all(self) -> list[Packet]:
        """Return all packets."""

    @abstractmethod
    def delete_all(self) -> None:
        """Delete all packets."""
