"""
Unit tests for FeatureExtractor.
"""

from __future__ import annotations

from datetime import UTC, datetime

from sentinelx_ai.application.feature_engine.feature_extractor import (
    FeatureExtractor,
)
from sentinelx_ai.application.feature_engine.feature_vector import (
    FeatureVector,
)
from sentinelx_ai.application.feature_engine.flow_builder import (
    FlowBuilder,
)
from sentinelx_ai.domain.entities.packet import Packet
from sentinelx_ai.domain.enums.protocol_type import ProtocolType
from sentinelx_ai.domain.value_objects.ip_address import IPAddress
from sentinelx_ai.domain.value_objects.port import Port
from sentinelx_ai.domain.value_objects.timestamp import Timestamp


def create_extractor() -> FeatureExtractor:
    """Create a FeatureExtractor instance."""
    return FeatureExtractor(
        flow_builder=FlowBuilder(),
    )


def _make_packet(size: int = 100) -> Packet:
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


def test_no_feature_vector_before_five_packets() -> None:
    """No feature vector should be produced before five packets."""
    extractor = create_extractor()

    for _ in range(4):
        assert extractor.process_packet(_make_packet()) is None


def test_feature_vector_after_five_packets() -> None:
    """A FeatureVector should be produced after five packets."""
    extractor = create_extractor()

    vector = None

    for _ in range(5):
        vector = extractor.process_packet(_make_packet())

    assert vector is not None
    assert isinstance(vector, FeatureVector)
