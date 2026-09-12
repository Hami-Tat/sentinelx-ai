"""
Risk Assessment Service.

Orchestrates the Risk Engine: turns a Threat into a RiskAssessment
using the likelihood/impact model from risk_calculator.
"""

from __future__ import annotations

from sentinelx_ai.application.risk_engine.risk_calculator import (
    calculate_risk_score,
)
from sentinelx_ai.domain.entities.risk_assessment import RiskAssessment
from sentinelx_ai.domain.entities.threat import Threat
from sentinelx_ai.domain.value_objects.timestamp import Timestamp


class RiskAssessmentService:
    """
    Main entry point for the Risk Engine.
    """

    def assess(
        self,
        threat: Threat,
        identifier: str,
    ) -> RiskAssessment:
        """
        Assess the risk carried by a Threat.

        Args:
            threat:
                The threat to assess. Its ``risk_score`` field is
                updated in place with the computed score before this
                method returns, so that ``threat.risk_score`` and the
                returned ``RiskAssessment.score`` never diverge. This
                is intentional, not an oversight: do not remove it
                without also removing the ``Threat.risk_score`` field
                it keeps in sync.
            identifier:
                Identifier for the produced RiskAssessment. Nothing
                elsewhere in the codebase generates entity
                identifiers (they are supplied by the caller), so
                this method follows the same convention rather than
                inventing one.

        Returns:
            The RiskAssessment for this threat, timestamped with the
            current time.
        """
        score = calculate_risk_score(threat)

        threat.risk_score = score

        return RiskAssessment(
            identifier=identifier,
            threat=threat,
            score=score,
            assessed_at=Timestamp.now(),
        )
