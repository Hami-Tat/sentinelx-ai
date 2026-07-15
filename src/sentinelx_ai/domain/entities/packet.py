"""
Packet Entity.

Represents a captured network packet.
"""

from dataclasses import dataclass

from sentinelx_ai.domain.enums.protocol_type import ProtocolType
from sentinelx_ai.domain.value_objects.ip_address import IPAddress
from sentinelx_ai.domain.value_objects.port import Port
from sentinelx_ai.domain.value_objects.timestamp import Timestamp


@dataclass(slots=True)
class Packet:
    """
    Entity representing a captured network packet.
    """

    source_ip: IPAddress
    destination_ip: IPAddress
    source_port: Port
    destination_port: Port
    protocol: ProtocolType
    size: int
    timestamp: Timestamp

    def __post_init__(self) -> None:
        """
        Validate packet attributes.
        """
        if self.size <= 0:
            raise ValueError("Packet size must be greater than zero.")
