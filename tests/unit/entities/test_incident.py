from datetime import UTC, datetime

from sentinelx_ai.domain.entities.alert import Alert
from sentinelx_ai.domain.entities.incident import Incident
from sentinelx_ai.domain.entities.threat import Threat
from sentinelx_ai.domain.enums.severity import Severity
from sentinelx_ai.domain.enums.threat_type import ThreatType
from sentinelx_ai.domain.value_objects.probability import Probability
from sentinelx_ai.domain.value_objects.risk_score import RiskScore
from sentinelx_ai.domain.value_objects.timestamp import Timestamp


def test_create_incident():
    threat = Threat(
        identifier="THR-001",
        threat_type=ThreatType.DDOS,
        severity=Severity.CRITICAL,
        confidence=Probability(0.99),
        risk_score=RiskScore(95),
        detected_at=Timestamp(datetime(2026, 7, 15, tzinfo=UTC)),
    )

    alert = Alert(
        identifier="ALT-001",
        threat=threat,
        message="Attack detected",
        created_at=Timestamp(datetime(2026, 7, 15, tzinfo=UTC)),
    )

    incident = Incident(
        identifier="INC-001",
        alert=alert,
        description="Security incident",
        created_at=Timestamp(datetime(2026, 7, 15, tzinfo=UTC)),
    )

    assert incident.identifier == "INC-001"
    assert incident.alert == alert
