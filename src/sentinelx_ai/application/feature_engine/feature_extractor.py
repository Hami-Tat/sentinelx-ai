"""
Feature Extractor.

This module orchestrates the feature extraction process.
It converts network flows into feature vectors that can be
consumed by the Detection Engine.
"""

from __future__ import annotations

from sentinelx_ai.application.feature_engine.feature_vector import (
    FeatureVector,
)
from sentinelx_ai.application.feature_engine.flow_builder import (
    FlowBuilder,
)


class FeatureExtractor:
    """Orchestrates feature extraction from network packets."""

    def __init__(
        self,
        flow_builder: FlowBuilder,
    ) -> None:
        self._flow_builder = flow_builder

    def process_packet(self, packet: object) -> FeatureVector | None:
        """
        Process a packet and return a feature vector when a flow is ready.

        Args:
            packet: Captured network packet.

        Returns:
            A FeatureVector if a complete flow is available,
            otherwise None.
        """
        flow = self._flow_builder.add_packet(packet)

        if flow is None:
            return None

        return FeatureVector.from_flow(flow)
