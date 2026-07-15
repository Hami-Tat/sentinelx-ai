"""
Alert Entity.

Represents a security alert.
"""

from dataclasses import dataclass

from sentinelx_ai.domain.entities.threat import Threat
from sentinelx_ai.domain.value_objects.timestamp import Timestamp


@dataclass(slots=True)
class Alert:
    """
    Entity representing a security alert.
    """

    identifier: str
    threat: Threat
    message: str
    created_at: Timestamp
