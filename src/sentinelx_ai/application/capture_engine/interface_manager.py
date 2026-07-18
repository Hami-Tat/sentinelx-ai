"""
Interface Manager.

Responsible for discovering and managing network interfaces.
"""

from __future__ import annotations


class InterfaceManager:
    """Manage available network interfaces."""

    def __init__(self) -> None:
        self._active_interface: str | None = None

    def set_active_interface(
        self,
        interface_name: str,
    ) -> None:
        """Set the active network interface."""
        self._active_interface = interface_name

    def get_active_interface(self) -> str | None:
        """Return the active network interface."""
        return self._active_interface

    def clear_active_interface(self) -> None:
        """Clear the active network interface."""
        self._active_interface = None
