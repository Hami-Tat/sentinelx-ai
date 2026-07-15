"""
Decision Type Enumeration.
"""

from enum import StrEnum


class DecisionType(StrEnum):
    """
    Possible decisions produced by the Decision Engine.
    """

    IGNORE = "Ignore"
    MONITOR = "Monitor"
    ALERT = "Alert"
    BLOCK = "Block"
    QUARANTINE = "Quarantine"
