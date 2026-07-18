"""
Knowledge Base Service.

Provides access to the Knowledge Base.
"""

from sentinelx_ai.application.knowledge_base.knowledge_loader import (
    KnowledgeLoader,
)
from sentinelx_ai.application.knowledge_base.knowledge_matcher import (
    KnowledgeMatcher,
)
from sentinelx_ai.domain.entities.knowledge import Knowledge
from sentinelx_ai.domain.entities.threat import Threat


class KnowledgeBaseService:
    """
    Main entry point for the Knowledge Base.
    """

    def __init__(
        self,
        loader: KnowledgeLoader,
        matcher: KnowledgeMatcher,
    ) -> None:
        self._loader = loader
        self._matcher = matcher

    def find_knowledge(
        self,
        threat: Threat,
    ) -> Knowledge | None:
        """
        Find the best knowledge entry for a detected threat.
        """

        knowledge_entries = self._loader.load()

        return self._matcher.match(
            threat,
            knowledge_entries,
        )
