"""
Risk Assessed Domain Event.
"""

from dataclasses import dataclass

from sentinelx_ai.domain.entities.risk_assessment import RiskAssessment


@dataclass(frozen=True, slots=True)
class RiskAssessed:
    """
    Event raised when a risk assessment is completed.
    """

    assessment: RiskAssessment
