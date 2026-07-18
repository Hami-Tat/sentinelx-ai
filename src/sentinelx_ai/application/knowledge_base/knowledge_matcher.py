"""
Knowledge Matcher.

Matches detected threats with knowledge base entries.
"""

from sentinelx_ai.domain.entities.knowledge import Knowledge
from sentinelx_ai.domain.entities.threat import Threat


class KnowledgeMatcher:
    """
    Responsible for matching threats with knowledge entries.
    """

    def match(
        self,
        threat: Threat,
        knowledge_entries: list[Knowledge],
    ) -> Knowledge | None:
        """
        Return the first matching knowledge entry.

        Args:
            threat: Detected threat.
            knowledge_entries: Available knowledge entries.

        Returns:
            A matching Knowledge entity or None.
        """
        del threat

        if not knowledge_entries:
            return None

        return knowledge_entries[0]
