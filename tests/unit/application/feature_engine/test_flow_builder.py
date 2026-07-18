"""
Unit tests for FlowBuilder.
"""

from __future__ import annotations

from sentinelx_ai.application.feature_engine.flow_builder import (
    FlowBuilder,
)


def test_flow_not_ready_before_five_packets() -> None:
    """A flow should not be completed before five packets."""
    builder = FlowBuilder()

    for i in range(4):
        assert builder.add_packet({"id": i}) is None


def test_flow_ready_after_five_packets() -> None:
    """A flow should be returned after five packets."""
    builder = FlowBuilder()

    flow = None

    for i in range(5):
        flow = builder.add_packet({"id": i})

    assert flow is not None
    assert flow.packet_count == 5


def test_reset_flow() -> None:
    """Reset should clear the current flow."""
    builder = FlowBuilder()

    builder.add_packet({"id": 1})

    builder.reset()

    assert builder.add_packet({"id": 2}) is None
