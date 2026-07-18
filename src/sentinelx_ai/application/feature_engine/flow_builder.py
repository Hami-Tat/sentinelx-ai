"""
Flow Builder.

Responsible for grouping packets into network flows.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class NetworkFlow:
    """Represents a network flow."""

    packets: list[Any] = field(default_factory=list)

    def add_packet(self, packet: Any) -> None:
        """Add a packet to the flow."""
        self.packets.append(packet)

    @property
    def packet_count(self) -> int:
        """Return the number of packets in the flow."""
        return len(self.packets)


class FlowBuilder:
    """Build network flows from captured packets."""

    def __init__(self) -> None:
        self._current_flow = NetworkFlow()

    def add_packet(self, packet: Any) -> NetworkFlow | None:
        """
        Add a packet to the current flow.

        For this first implementation, every packet is added to a
        single flow. A flow is considered ready after five packets.

        Args:
            packet: Captured network packet.

        Returns:
            A completed NetworkFlow or None.
        """
        self._current_flow.add_packet(packet)

        if self._current_flow.packet_count < 5:
            return None

        completed_flow = self._current_flow
        self._current_flow = NetworkFlow()

        return completed_flow

    def reset(self) -> None:
        """Reset the current flow."""
        self._current_flow = NetworkFlow()
