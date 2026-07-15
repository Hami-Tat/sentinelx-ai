"""
Threat Type Enumeration.
"""

from enum import StrEnum


class ThreatType(StrEnum):
    """
    Supported threat categories.
    """

    DOS = "DoS"
    DDOS = "DDoS"
    PORT_SCAN = "Port Scan"
    BRUTE_FORCE = "Brute Force"
    MALWARE = "Malware"
    BOTNET = "Botnet"
    PHISHING = "Phishing"
    RANSOMWARE = "Ransomware"
    ZERO_DAY = "Zero-Day"
    NORMAL = "Normal"
    UNKNOWN = "Unknown"
