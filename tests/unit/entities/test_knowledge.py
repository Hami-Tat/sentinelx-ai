from datetime import UTC, datetime

from sentinelx_ai.domain.entities.knowledge import Knowledge
from sentinelx_ai.domain.value_objects.timestamp import Timestamp


def test_create_knowledge():
    knowledge = Knowledge(
        identifier="KB-001",
        title="DDoS Detection",
        description="Knowledge about DDoS attacks.",
        created_at=Timestamp(datetime(2026, 7, 15, tzinfo=UTC)),
    )

    assert knowledge.title == "DDoS Detection"
