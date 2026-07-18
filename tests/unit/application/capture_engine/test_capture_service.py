"""
Unit tests for CaptureService.
"""

from __future__ import annotations

from sentinelx_ai.application.capture_engine.capture_service import (
    CaptureService,
)
from sentinelx_ai.application.capture_engine.interface_manager import (
    InterfaceManager,
)
from sentinelx_ai.application.capture_engine.packet_buffer import (
    PacketBuffer,
)


def create_service() -> CaptureService:
    """Create a CaptureService instance for testing."""
    return CaptureService(
        interface_manager=InterfaceManager(),
        packet_buffer=PacketBuffer(),
    )


def test_service_not_running_on_creation() -> None:
    """CaptureService should be stopped by default."""
    service = create_service()

    assert service.is_running() is False


def test_start_service() -> None:
    """Starting the service should change its state."""
    service = create_service()

    service.start()

    assert service.is_running() is True


def test_stop_service() -> None:
    """Stopping the service should change its state."""
    service = create_service()

    service.start()
    service.stop()

    assert service.is_running() is False


def test_capture_packet() -> None:
    """Captured packets should be stored in the buffer."""
    service = create_service()

    packet = {"id": 1}

    service.capture_packet(packet)

    assert service.get_buffer_size() == 1
