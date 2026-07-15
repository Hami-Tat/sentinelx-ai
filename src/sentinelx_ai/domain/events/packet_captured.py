"""
Packet Captured Domain Event.
"""

from dataclasses import dataclass

from sentinelx_ai.domain.entities.packet import Packet


@dataclass(frozen=True, slots=True)
class PacketCaptured:
    """
    Event raised when a network packet is captured.
    """

    packet: Packet
