"""
Alert Repository Interface.
"""

from abc import ABC, abstractmethod

from sentinelx_ai.domain.entities.alert import Alert


class AlertRepository(ABC):
    """
    Repository interface for Alert entities.
    """

    @abstractmethod
    def save(self, alert: Alert) -> None:
        """Save an alert."""

    @abstractmethod
    def get_all(self) -> list[Alert]:
        """Return all alerts."""

    @abstractmethod
    def delete_all(self) -> None:
        """Delete all alerts."""
