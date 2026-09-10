"""
Unit tests for FeatureVector.
"""

from __future__ import annotations

from datetime import UTC, datetime

from sentinelx_ai.application.feature_engine.feature_vector import (
    FeatureVector,
)
from sentinelx_ai.application.feature_engine.flow_builder import (
    NetworkFlow,
)
from sentinelx_ai.domain.entities.packet import Packet
from sentinelx_ai.domain.enums.protocol_type import ProtocolType
from sentinelx_ai.domain.value_objects.ip_address import IPAddress
from sentinelx_ai.domain.value_objects.port import Port
from sentinelx_ai.domain.value_objects.timestamp import Timestamp


def _make_packet(size: int) -> Packet:
    """Build a valid Packet with a given size."""
    return Packet(
        source_ip=IPAddress("192.168.1.10"),
        destination_ip=IPAddress("192.168.1.20"),
        source_port=Port(443),
        destination_port=Port(8080),
        protocol=ProtocolType.TCP,
        size=size,
        timestamp=Timestamp(datetime(2026, 7, 15, 12, 0, tzinfo=UTC)),
    )


def test_feature_vector_creation() -> None:
    """FeatureVector should be created from a flow."""
    flow = NetworkFlow()

    flow.add_packet(_make_packet(1000))
    flow.add_packet(_make_packet(1500))

    vector = FeatureVector.from_flow(flow)

    assert vector.packet_count == 2
    assert vector.total_bytes > 0


def test_feature_vector_total_bytes_sums_packet_sizes() -> None:
    """
    total_bytes must be the sum of each Packet.size, not the length
    of the packets' string representation.
    """
    flow = NetworkFlow()

    flow.add_packet(_make_packet(1000))
    flow.add_packet(_make_packet(1500))

    vector = FeatureVector.from_flow(flow)

    wrong_total_bytes = sum(len(str(packet)) for packet in flow.packets)

    assert vector.total_bytes == 2500
    assert vector.total_bytes != wrong_total_bytes


def test_feature_vector_to_dict() -> None:
    """FeatureVector should be converted to a dictionary."""
    flow = NetworkFlow()

    flow.add_packet(_make_packet(1000))

    vector = FeatureVector.from_flow(flow)

    data = vector.to_dict()

    assert data["packet_count"] == 1
    assert data["total_bytes"] == 1000
