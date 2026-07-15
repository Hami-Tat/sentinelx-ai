"""
Severity Enumeration.
"""

from enum import StrEnum


class Severity(StrEnum):
    """
    Threat severity levels.
    """

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"
