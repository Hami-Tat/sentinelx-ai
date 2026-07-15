"""
Knowledge Repository Interface.
"""

from abc import ABC, abstractmethod

from sentinelx_ai.domain.entities.knowledge import Knowledge


class KnowledgeRepository(ABC):
    """
    Repository interface for Knowledge entities.
    """

    @abstractmethod
    def save(self, knowledge: Knowledge) -> None:
        """Save a knowledge entry."""

    @abstractmethod
    def get_all(self) -> list[Knowledge]:
        """Return all knowledge entries."""

    @abstractmethod
    def delete_all(self) -> None:
        """Delete all knowledge entries."""
