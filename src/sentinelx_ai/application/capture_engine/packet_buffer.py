"""
Packet Buffer.

Responsible for temporarily storing captured packets.
"""

from __future__ import annotations

from collections import deque
from typing import Any


class PacketBuffer:
    """A FIFO buffer for captured packets."""

    def __init__(self) -> None:
        self._buffer: deque[Any] = deque()

    def add(self, packet: Any) -> None:
        """Add a packet to the buffer."""
        self._buffer.append(packet)

    def pop(self) -> Any:
        """
        Remove and return the oldest packet.

        Raises:
            IndexError: If the buffer is empty.
        """
        if self.is_empty():
            msg = "Packet buffer is empty."
            raise IndexError(msg)

        return self._buffer.popleft()

    def size(self) -> int:
        """Return the number of packets in the buffer."""
        return len(self._buffer)

    def is_empty(self) -> bool:
        """Return True if the buffer is empty."""
        return len(self._buffer) == 0

    def clear(self) -> None:
        """Remove all packets from the buffer."""
        self._buffer.clear()
