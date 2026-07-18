from datetime import UTC, datetime

from sentinelx_ai.application.knowledge_base.knowledge_matcher import (
    KnowledgeMatcher,
)
from sentinelx_ai.domain.entities.knowledge import Knowledge
from sentinelx_ai.domain.entities.threat import Threat
from sentinelx_ai.domain.enums.severity import Severity
from sentinelx_ai.domain.enums.threat_type import ThreatType
from sentinelx_ai.domain.value_objects.probability import Probability
from sentinelx_ai.domain.value_objects.risk_score import RiskScore
from sentinelx_ai.domain.value_objects.timestamp import Timestamp


def create_threat() -> Threat:
    return Threat(
        identifier="THR-001",
        threat_type=ThreatType.DDOS,
        severity=Severity.CRITICAL,
        confidence=Probability(0.99),
        risk_score=RiskScore(95),
        detected_at=Timestamp(datetime(2026, 7, 15, tzinfo=UTC)),
    )


def create_knowledge() -> Knowledge:
    return Knowledge(
        identifier="KB-001",
        title="DDoS",
        description="Protection against DDoS attacks.",
        created_at=Timestamp(datetime(2026, 7, 15, tzinfo=UTC)),
    )


def test_match_returns_first_knowledge():
    matcher = KnowledgeMatcher()

    threat = create_threat()

    knowledge = create_knowledge()

    result = matcher.match(threat, [knowledge])

    assert result == knowledge


def test_match_returns_none_when_empty():
    matcher = KnowledgeMatcher()

    threat = create_threat()

    result = matcher.match(threat, [])

    assert result is None
