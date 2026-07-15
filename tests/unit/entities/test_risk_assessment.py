from datetime import UTC, datetime

from sentinelx_ai.domain.entities.risk_assessment import RiskAssessment
from sentinelx_ai.domain.entities.threat import Threat
from sentinelx_ai.domain.enums.severity import Severity
from sentinelx_ai.domain.enums.threat_type import ThreatType
from sentinelx_ai.domain.value_objects.probability import Probability
from sentinelx_ai.domain.value_objects.risk_score import RiskScore
from sentinelx_ai.domain.value_objects.timestamp import Timestamp


def test_create_risk_assessment():
    threat = Threat(
        identifier="THR-001",
        threat_type=ThreatType.MALWARE,
        severity=Severity.HIGH,
        confidence=Probability(0.91),
        risk_score=RiskScore(85),
        detected_at=Timestamp(datetime(2026, 7, 15, tzinfo=UTC)),
    )

    assessment = RiskAssessment(
        identifier="RISK-001",
        threat=threat,
        score=RiskScore(85),
        assessed_at=Timestamp(datetime(2026, 7, 15, tzinfo=UTC)),
    )

    assert assessment.score.value == 85
