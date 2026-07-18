"""
Unit tests for InterfaceManager.
"""

from __future__ import annotations

from sentinelx_ai.application.capture_engine.interface_manager import (
    InterfaceManager,
)


def test_no_active_interface_on_creation() -> None:
    """There should be no active interface initially."""
    manager = InterfaceManager()

    assert manager.get_active_interface() is None


def test_set_active_interface() -> None:
    """The active interface should be stored."""
    manager = InterfaceManager()

    manager.set_active_interface("eth0")

    assert manager.get_active_interface() == "eth0"


def test_clear_active_interface() -> None:
    """The active interface can be cleared."""
    manager = InterfaceManager()

    manager.set_active_interface("eth0")
    manager.clear_active_interface()

    assert manager.get_active_interface() is None
