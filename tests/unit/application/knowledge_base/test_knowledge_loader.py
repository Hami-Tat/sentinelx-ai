from sentinelx_ai.application.knowledge_base.knowledge_loader import (
    KnowledgeLoader,
)


def test_load_returns_list():
    loader = KnowledgeLoader()

    knowledge = loader.load()

    assert isinstance(knowledge, list)
    assert knowledge == []
