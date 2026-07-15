"""
Risk Assessment Entity.
"""

from dataclasses import dataclass

from sentinelx_ai.domain.entities.threat import Threat
from sentinelx_ai.domain.value_objects.risk_score import RiskScore
from sentinelx_ai.domain.value_objects.timestamp import Timestamp


@dataclass(slots=True)
class RiskAssessment:
    """
    Entity representing a risk assessment.
    """

    identifier: str
    threat: Threat
    score: RiskScore
    assessed_at: Timestamp
