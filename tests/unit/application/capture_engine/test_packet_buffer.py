"""
Unit tests for PacketBuffer.
"""

from __future__ import annotations

import pytest

from sentinelx_ai.application.capture_engine.packet_buffer import PacketBuffer


def test_buffer_is_empty_on_creation() -> None:
    """A new buffer should be empty."""
    buffer = PacketBuffer()

    assert buffer.is_empty() is True
    assert buffer.size() == 0


def test_add_packet() -> None:
    """Adding a packet should increase the buffer size."""
    buffer = PacketBuffer()

    packet = {"id": 1}

    buffer.add(packet)

    assert buffer.size() == 1
    assert buffer.is_empty() is False


def test_pop_packet() -> None:
    """Packets should be removed in FIFO order."""
    buffer = PacketBuffer()

    packet = {"id": 1}

    buffer.add(packet)

    assert buffer.pop() == packet
    assert buffer.is_empty() is True


def test_clear_buffer() -> None:
    """Clearing the buffer removes every packet."""
    buffer = PacketBuffer()

    buffer.add({"id": 1})
    buffer.add({"id": 2})

    buffer.clear()

    assert buffer.size() == 0
    assert buffer.is_empty() is True


def test_pop_empty_buffer_raises_error() -> None:
    """Popping an empty buffer should raise IndexError."""
    buffer = PacketBuffer()

    with pytest.raises(IndexError):
        buffer.pop()
