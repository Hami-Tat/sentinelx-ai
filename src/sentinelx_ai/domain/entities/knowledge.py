"""
Knowledge Entity.
"""

from dataclasses import dataclass

from sentinelx_ai.domain.value_objects.timestamp import Timestamp


@dataclass(slots=True)
class Knowledge:
    """
    Entity representing a knowledge base record.
    """

    identifier: str
    title: str
    description: str
    created_at: Timestamp
