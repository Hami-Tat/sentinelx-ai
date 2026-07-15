"""
Protocol Type Enumeration.
"""

from enum import StrEnum


class ProtocolType(StrEnum):
    """
    Supported network protocols.
    """

    TCP = "TCP"
    UDP = "UDP"
    ICMP = "ICMP"
    HTTP = "HTTP"
    HTTPS = "HTTPS"
    DNS = "DNS"
    FTP = "FTP"
    SSH = "SSH"
