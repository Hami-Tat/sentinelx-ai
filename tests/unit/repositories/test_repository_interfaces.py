import pytest

from sentinelx_ai.domain.repositories.alert_repository import AlertRepository
from sentinelx_ai.domain.repositories.incident_repository import IncidentRepository
from sentinelx_ai.domain.repositories.knowledge_repository import KnowledgeRepository
from sentinelx_ai.domain.repositories.ml_model_repository import MLModelRepository
from sentinelx_ai.domain.repositories.packet_repository import PacketRepository
from sentinelx_ai.domain.repositories.risk_assessment_repository import (
    RiskAssessmentRepository,
)
from sentinelx_ai.domain.repositories.threat_repository import ThreatRepository


@pytest.mark.parametrize(
    "repository",
    [
        PacketRepository,
        ThreatRepository,
        AlertRepository,
        IncidentRepository,
        KnowledgeRepository,
        MLModelRepository,
        RiskAssessmentRepository,
    ],
)
def test_repository_is_abstract(repository):
    with pytest.raises(TypeError):
        repository()
