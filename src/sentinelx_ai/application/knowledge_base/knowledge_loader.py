"""
Knowledge Loader.

Loads knowledge entries from the configured data source.
"""

from sentinelx_ai.domain.entities.knowledge import Knowledge


class KnowledgeLoader:
    """
    Responsible for loading knowledge entries.
    """

    def load(self) -> list[Knowledge]:
        """
        Load all available knowledge entries.

        Returns:
            A list of Knowledge entities.
        """
        return []
