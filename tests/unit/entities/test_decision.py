from datetime import UTC, datetime

from sentinelx_ai.domain.entities.decision import Decision
from sentinelx_ai.domain.entities.risk_assessment import RiskAssessment
from sentinelx_ai.domain.entities.threat import Threat
from sentinelx_ai.domain.enums.decision_type import DecisionType
from sentinelx_ai.domain.enums.severity import Severity
from sentinelx_ai.domain.enums.threat_type import ThreatType
from sentinelx_ai.domain.value_objects.probability import Probability
from sentinelx_ai.domain.value_objects.risk_score import RiskScore
from sentinelx_ai.domain.value_objects.timestamp import Timestamp


def test_create_decision():
    threat = Threat(
        identifier="THR-001",
        threat_type=ThreatType.DDOS,
        severity=Severity.CRITICAL,
        confidence=Probability(0.98),
        risk_score=RiskScore(95),
        detected_at=Timestamp(datetime(2026, 7, 15, tzinfo=UTC)),
    )

    assessment = RiskAssessment(
        identifier="RISK-001",
        threat=threat,
        score=RiskScore(95),
        assessed_at=Timestamp(datetime(2026, 7, 15, tzinfo=UTC)),
    )

    decision = Decision(
        identifier="DEC-001",
        assessment=assessment,
        decision=DecisionType.BLOCK,
        created_at=Timestamp(datetime(2026, 7, 15, tzinfo=UTC)),
    )

    assert decision.decision == DecisionType.BLOCK
