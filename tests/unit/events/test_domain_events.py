from datetime import UTC, datetime

from sentinelx_ai.domain.entities.knowledge import Knowledge
from sentinelx_ai.domain.entities.ml_model import MLModel
from sentinelx_ai.domain.entities.packet import Packet
from sentinelx_ai.domain.enums.protocol_type import ProtocolType
from sentinelx_ai.domain.events.knowledge_updated import KnowledgeUpdated
from sentinelx_ai.domain.events.model_retrained import ModelRetrained
from sentinelx_ai.domain.events.packet_captured import PacketCaptured
from sentinelx_ai.domain.value_objects.ip_address import IPAddress
from sentinelx_ai.domain.value_objects.port import Port
from sentinelx_ai.domain.value_objects.timestamp import Timestamp


def test_packet_captured_event():
    packet = Packet(
        source_ip=IPAddress("192.168.1.1"),
        destination_ip=IPAddress("192.168.1.2"),
        source_port=Port(80),
        destination_port=Port(8080),
        protocol=ProtocolType.TCP,
        size=1500,
        timestamp=Timestamp(datetime(2026, 7, 15, tzinfo=UTC)),
    )

    event = PacketCaptured(packet)

    assert event.packet == packet


def test_knowledge_updated_event():
    knowledge = Knowledge(
        identifier="KB-001",
        title="Knowledge",
        description="Knowledge Base",
        created_at=Timestamp(datetime(2026, 7, 15, tzinfo=UTC)),
    )

    event = KnowledgeUpdated(knowledge)

    assert event.knowledge == knowledge


def test_model_retrained_event():
    model = MLModel(
        identifier="ML-001",
        name="RandomForest",
        version="1.0",
        accuracy=0.99,
        created_at=Timestamp(datetime(2026, 7, 15, tzinfo=UTC)),
    )

    event = ModelRetrained(model)

    assert event.model == model
