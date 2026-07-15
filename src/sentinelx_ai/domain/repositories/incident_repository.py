"""
Incident Repository Interface.
"""

from abc import ABC, abstractmethod

from sentinelx_ai.domain.entities.incident import Incident


class IncidentRepository(ABC):
    """
    Repository interface for Incident entities.
    """

    @abstractmethod
    def save(self, incident: Incident) -> None:
        """Save an incident."""

    @abstractmethod
    def get_all(self) -> list[Incident]:
        """Return all incidents."""

    @abstractmethod
    def delete_all(self) -> None:
        """Delete all incidents."""
