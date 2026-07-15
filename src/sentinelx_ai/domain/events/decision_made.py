"""
Decision Made Domain Event.
"""

from dataclasses import dataclass

from sentinelx_ai.domain.entities.decision import Decision


@dataclass(frozen=True, slots=True)
class DecisionMade:
    """
    Event raised when a security decision is made.
    """

    decision: Decision
