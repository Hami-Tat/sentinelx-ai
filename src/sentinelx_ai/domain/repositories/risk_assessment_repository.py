"""
Risk Assessment Repository Interface.
"""

from abc import ABC, abstractmethod

from sentinelx_ai.domain.entities.risk_assessment import RiskAssessment


class RiskAssessmentRepository(ABC):
    """
    Repository interface for RiskAssessment entities.
    """

    @abstractmethod
    def save(self, risk_assessment: RiskAssessment) -> None:
        """Save a risk assessment."""

    @abstractmethod
    def get_all(self) -> list[RiskAssessment]:
        """Return all risk assessments."""

    @abstractmethod
    def delete_all(self) -> None:
        """Delete all risk assessments."""
