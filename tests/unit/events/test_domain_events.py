from datetime import UTC, datetime

from sentinelx_ai.domain.entities.decision import Decision
from sentinelx_ai.domain.entities.knowledge import Knowledge
from sentinelx_ai.domain.entities.ml_model import MLModel
from sentinelx_ai.domain.entities.packet import Packet
from sentinelx_ai.domain.entities.prevention_action import PreventionAction
from sentinelx_ai.domain.entities.risk_assessment import RiskAssessment
from sentinelx_ai.domain.entities.threat import Threat
from sentinelx_ai.domain.enums.decision_type import DecisionType
from sentinelx_ai.domain.enums.prevention_type import PreventionType
from sentinelx_ai.domain.enums.protocol_type import ProtocolType
from sentinelx_ai.domain.enums.severity import Severity
from sentinelx_ai.domain.enums.threat_type import ThreatType
from sentinelx_ai.domain.events.decision_made import DecisionMade
from sentinelx_ai.domain.events.knowledge_updated import KnowledgeUpdated
from sentinelx_ai.domain.events.model_retrained import ModelRetrained
from sentinelx_ai.domain.events.packet_captured import PacketCaptured
from sentinelx_ai.domain.events.prevention_executed import PreventionExecuted
from sentinelx_ai.domain.events.risk_assessed import RiskAssessed
from sentinelx_ai.domain.events.threat_detected import ThreatDetected
from sentinelx_ai.domain.value_objects.ip_address import IPAddress
from sentinelx_ai.domain.value_objects.port import Port
from sentinelx_ai.domain.value_objects.probability import Probability
from sentinelx_ai.domain.value_objects.risk_score import RiskScore
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


def test_threat_detected_event():
    threat = Threat(
        identifier="THR-001",
        threat_type=ThreatType.DDOS,
        severity=Severity.CRITICAL,
        confidence=Probability(0.99),
        risk_score=RiskScore(95),
        detected_at=Timestamp(datetime(2026, 7, 15, tzinfo=UTC)),
    )

    event = ThreatDetected(threat)

    assert event.threat == threat


def test_risk_assessed_event():
    threat = Threat(
        identifier="THR-001",
        threat_type=ThreatType.DDOS,
        severity=Severity.HIGH,
        confidence=Probability(0.95),
        risk_score=RiskScore(90),
        detected_at=Timestamp(datetime(2026, 7, 15, tzinfo=UTC)),
    )

    assessment = RiskAssessment(
        identifier="RISK-001",
        threat=threat,
        score=RiskScore(90),
        assessed_at=Timestamp(datetime(2026, 7, 15, tzinfo=UTC)),
    )

    event = RiskAssessed(assessment)

    assert event.assessment == assessment


def test_decision_made_event():
    threat = Threat(
        identifier="THR-001",
        threat_type=ThreatType.DDOS,
        severity=Severity.CRITICAL,
        confidence=Probability(0.99),
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

    event = DecisionMade(decision)

    assert event.decision == decision


def test_prevention_executed_event():
    threat = Threat(
        identifier="THR-001",
        threat_type=ThreatType.DDOS,
        severity=Severity.CRITICAL,
        confidence=Probability(0.99),
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

    action = PreventionAction(
        identifier="PREV-001",
        decision=decision,
        action=PreventionType.FIREWALL_RULE,
        executed_at=Timestamp(datetime(2026, 7, 15, tzinfo=UTC)),
    )

    event = PreventionExecuted(action)

    assert event.action == action


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
