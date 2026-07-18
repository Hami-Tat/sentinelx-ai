"""
Unit tests for FeatureVector.
"""

from __future__ import annotations

from sentinelx_ai.application.feature_engine.feature_vector import (
    FeatureVector,
)
from sentinelx_ai.application.feature_engine.flow_builder import (
    NetworkFlow,
)


def test_feature_vector_creation() -> None:
    """FeatureVector should be created from a flow."""
    flow = NetworkFlow()

    flow.add_packet("packet1")
    flow.add_packet("packet2")

    vector = FeatureVector.from_flow(flow)

    assert vector.packet_count == 2
    assert vector.total_bytes > 0


def test_feature_vector_to_dict() -> None:
    """FeatureVector should be converted to a dictionary."""
    flow = NetworkFlow()

    flow.add_packet("packet")

    vector = FeatureVector.from_flow(flow)

    data = vector.to_dict()

    assert data["packet_count"] == 1
    assert "total_bytes" in data
