from datetime import UTC, datetime

import pytest

from sentinelx_ai.domain.entities.packet import Packet
from sentinelx_ai.domain.enums.protocol_type import ProtocolType
from sentinelx_ai.domain.value_objects.ip_address import IPAddress
from sentinelx_ai.domain.value_objects.port import Port
from sentinelx_ai.domain.value_objects.timestamp import Timestamp


def test_create_packet():
    packet = Packet(
        source_ip=IPAddress("192.168.1.10"),
        destination_ip=IPAddress("192.168.1.20"),
        source_port=Port(443),
        destination_port=Port(8080),
        protocol=ProtocolType.TCP,
        size=1500,
        timestamp=Timestamp(datetime(2026, 7, 15, 12, 0, tzinfo=UTC)),
    )

    assert packet.size == 1500
    assert packet.protocol == ProtocolType.TCP


def test_invalid_packet_size():
    with pytest.raises(ValueError):
        Packet(
            source_ip=IPAddress("192.168.1.10"),
            destination_ip=IPAddress("192.168.1.20"),
            source_port=Port(443),
            destination_port=Port(8080),
            protocol=ProtocolType.TCP,
            size=0,
            timestamp=Timestamp(datetime(2026, 7, 15, 12, 0, tzinfo=UTC)),
        )
