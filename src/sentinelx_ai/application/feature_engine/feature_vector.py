"""
Feature Vector.

Represents the machine learning feature vector extracted
from a network flow.
"""

from __future__ import annotations

from dataclasses import dataclass

from sentinelx_ai.application.feature_engine.flow_builder import (
    NetworkFlow,
)


@dataclass(slots=True)
class FeatureVector:
    """Represents the extracted features of a network flow."""

    packet_count: int
    total_bytes: int

    @classmethod
    def from_flow(cls, flow: NetworkFlow) -> FeatureVector:
        """
        Build a FeatureVector from a NetworkFlow.

        Args:
            flow: A completed network flow.

        Returns:
            A FeatureVector instance.
        """
        total_bytes = sum(len(str(packet)) for packet in flow.packets)

        return cls(
            packet_count=flow.packet_count,
            total_bytes=total_bytes,
        )

    def to_dict(self) -> dict[str, int]:
        """
        Convert the feature vector into a dictionary.

        Returns:
            Dictionary representation of the feature vector.
        """
        return {
            "packet_count": self.packet_count,
            "total_bytes": self.total_bytes,
        }
