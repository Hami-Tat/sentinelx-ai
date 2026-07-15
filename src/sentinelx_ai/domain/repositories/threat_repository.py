"""
Threat Repository Interface.
"""

from abc import ABC, abstractmethod

from sentinelx_ai.domain.entities.threat import Threat


class ThreatRepository(ABC):
    """
    Repository interface for Threat entities.
    """

    @abstractmethod
    def save(self, threat: Threat) -> None:
        """Save a threat."""

    @abstractmethod
    def get_all(self) -> list[Threat]:
        """Return all threats."""

    @abstractmethod
    def delete_all(self) -> None:
        """Delete all threats."""
