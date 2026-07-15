"""
Decision Entity.
"""

from dataclasses import dataclass

from sentinelx_ai.domain.entities.risk_assessment import RiskAssessment
from sentinelx_ai.domain.enums.decision_type import DecisionType
from sentinelx_ai.domain.value_objects.timestamp import Timestamp


@dataclass(slots=True)
class Decision:
    """
    Entity representing a security decision.
    """

    identifier: str
    assessment: RiskAssessment
    decision: DecisionType
    created_at: Timestamp
