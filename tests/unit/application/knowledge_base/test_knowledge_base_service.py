from datetime import UTC, datetime

from sentinelx_ai.application.knowledge_base.knowledge_base_service import (
    KnowledgeBaseService,
)
from sentinelx_ai.application.knowledge_base.knowledge_loader import (
    KnowledgeLoader,
)
from sentinelx_ai.application.knowledge_base.knowledge_matcher import (
    KnowledgeMatcher,
)
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


def test_find_knowledge_returns_none():
    service = KnowledgeBaseService(
        loader=KnowledgeLoader(),
        matcher=KnowledgeMatcher(),
    )

    result = service.find_knowledge(create_threat())

    assert result is None
