from datetime import UTC, datetime

from sentinelx_ai.domain.entities.threat import Threat
from sentinelx_ai.domain.enums.severity import Severity
from sentinelx_ai.domain.enums.threat_type import ThreatType
from sentinelx_ai.domain.value_objects.probability import Probability
from sentinelx_ai.domain.value_objects.risk_score import RiskScore
from sentinelx_ai.domain.value_objects.timestamp import Timestamp


def test_create_threat():
    threat = Threat(
        identifier="THR-001",
        threat_type=ThreatType.DDOS,
        severity=Severity.HIGH,
        confidence=Probability(0.97),
        risk_score=RiskScore(92),
        detected_at=Timestamp(datetime(2026, 7, 15, 12, 0, tzinfo=UTC)),
    )

    assert threat.identifier == "THR-001"
    assert threat.threat_type == ThreatType.DDOS
    assert threat.severity == Severity.HIGH
