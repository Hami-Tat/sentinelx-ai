"""
Unit tests for FeatureExtractor.
"""

from __future__ import annotations

from sentinelx_ai.application.feature_engine.feature_extractor import (
    FeatureExtractor,
)
from sentinelx_ai.application.feature_engine.feature_vector import (
    FeatureVector,
)
from sentinelx_ai.application.feature_engine.flow_builder import (
    FlowBuilder,
)


def create_extractor() -> FeatureExtractor:
    """Create a FeatureExtractor instance."""
    return FeatureExtractor(
        flow_builder=FlowBuilder(),
    )


def test_no_feature_vector_before_five_packets() -> None:
    """No feature vector should be produced before five packets."""
    extractor = create_extractor()

    for i in range(4):
        assert extractor.process_packet({"id": i}) is None


def test_feature_vector_after_five_packets() -> None:
    """A FeatureVector should be produced after five packets."""
    extractor = create_extractor()

    vector = None

    for i in range(5):
        vector = extractor.process_packet({"id": i})

    assert vector is not None
    assert isinstance(vector, FeatureVector)
