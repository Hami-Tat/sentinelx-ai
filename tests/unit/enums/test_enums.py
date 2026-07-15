from sentinelx_ai.domain.enums.decision_type import DecisionType
from sentinelx_ai.domain.enums.prevention_type import PreventionType
from sentinelx_ai.domain.enums.protocol_type import ProtocolType
from sentinelx_ai.domain.enums.severity import Severity
from sentinelx_ai.domain.enums.threat_type import ThreatType


def test_threat_type():
    assert ThreatType.DDOS.value == "DDoS"
    assert ThreatType.NORMAL.value == "Normal"


def test_severity():
    assert Severity.CRITICAL.value == "Critical"


def test_protocol():
    assert ProtocolType.TCP.value == "TCP"


def test_decision():
    assert DecisionType.BLOCK.value == "Block"


def test_prevention():
    assert PreventionType.FIREWALL_RULE.value == "Firewall Rule"
