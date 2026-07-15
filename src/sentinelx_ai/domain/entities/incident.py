"""
Incident Entity.

Represents a confirmed security incident.
"""

from dataclasses import dataclass

from sentinelx_ai.domain.entities.alert import Alert
from sentinelx_ai.domain.value_objects.timestamp import Timestamp


@dataclass(slots=True)
class Incident:
    """
    Entity representing a security incident.
    """

    identifier: str
    alert: Alert
    description: str
    created_at: Timestamp
