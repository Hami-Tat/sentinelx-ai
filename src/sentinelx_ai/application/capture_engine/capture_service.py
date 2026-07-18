"""
Capture Engine Service.

This module orchestrates the packet capture process.
It coordinates the Interface Manager and the Packet Buffer
without depending on any packet capture implementation.
"""

from __future__ import annotations

from sentinelx_ai.application.capture_engine.interface_manager import (
    InterfaceManager,
)
from sentinelx_ai.application.capture_engine.packet_buffer import (
    PacketBuffer,
)


class CaptureService:
    """Orchestrates the Capture Engine."""

    def __init__(
        self,
        interface_manager: InterfaceManager,
        packet_buffer: PacketBuffer,
    ) -> None:
        self._interface_manager = interface_manager
        self._packet_buffer = packet_buffer
        self._running = False

    def start(self) -> None:
        """Start the capture engine."""
        self._running = True

    def stop(self) -> None:
        """Stop the capture engine."""
        self._running = False

    def is_running(self) -> bool:
        """Return the running state."""
        return self._running

    def capture_packet(self, packet: object) -> None:
        """Store a captured packet."""
        self._packet_buffer.add(packet)

    def get_buffer_size(self) -> int:
        """Return the number of buffered packets."""
        return self._packet_buffer.size()
