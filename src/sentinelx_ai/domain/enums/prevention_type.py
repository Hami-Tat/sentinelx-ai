"""
Prevention Type Enumeration.
"""

from enum import StrEnum


class PreventionType(StrEnum):
    """
    Prevention actions supported by SentinelX AI.
    """

    FIREWALL_RULE = "Firewall Rule"
    ACL = "Access Control List"
    ISOLATE_HOST = "Isolate Host"
    TERMINATE_PROCESS = "Terminate Process"
    DISABLE_ACCOUNT = "Disable Account"
