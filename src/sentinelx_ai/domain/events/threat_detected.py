"""
Threat Detected Domain Event.
"""

from dataclasses import dataclass

from sentinelx_ai.domain.entities.threat import Threat


@dataclass(frozen=True, slots=True)
class ThreatDetected:
    """
    Event raised when a threat is detected.
    """

    threat: Threat
