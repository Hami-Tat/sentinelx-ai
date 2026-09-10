"""
Flow Builder.

Responsible for grouping packets into network flows.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from sentinelx_ai.domain.entities.packet import Packet


@dataclass(slots=True)
class NetworkFlow:
    """Represents a network flow."""

    packets: list[Packet] = field(default_factory=list)

    def add_packet(self, packet: Packet) -> None:
        """Add a packet to the flow."""
        self.packets.append(packet)

    @property
    def packet_count(self) -> int:
        """Return the number of packets in the flow."""
        return len(self.packets)


class FlowBuilder:
    """
    Build network flows from captured packets.

    Current limitation: this first implementation groups packets into
    fixed batches of five, with no notion of connection (no 5-tuple
    matching) and no timeout-based flow expiration. It is not the
    final flow-reconstruction logic.
    """

    def __init__(self) -> None:
        self._current_flow = NetworkFlow()

    def add_packet(self, packet: Packet) -> NetworkFlow | None:
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
