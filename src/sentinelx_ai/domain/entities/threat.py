"""
Threat Entity.

Represents a detected cyber threat.
"""

from dataclasses import dataclass

from sentinelx_ai.domain.enums.severity import Severity
from sentinelx_ai.domain.enums.threat_type import ThreatType
from sentinelx_ai.domain.value_objects.probability import Probability
from sentinelx_ai.domain.value_objects.risk_score import RiskScore
from sentinelx_ai.domain.value_objects.timestamp import Timestamp


@dataclass(slots=True)
class Threat:
    """
    Entity representing a detected threat.
    """

    identifier: str
    threat_type: ThreatType
    severity: Severity
    confidence: Probability
    risk_score: RiskScore
    detected_at: Timestamp
