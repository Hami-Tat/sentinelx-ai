"""
Knowledge Updated Domain Event.
"""

from dataclasses import dataclass

from sentinelx_ai.domain.entities.knowledge import Knowledge


@dataclass(frozen=True, slots=True)
class KnowledgeUpdated:
    """
    Event raised when the knowledge base is updated.
    """

    knowledge: Knowledge
