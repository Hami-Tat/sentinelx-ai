"""
Risk Calculator.

Computes an explainable RiskScore from a Threat, using the
likelihood/impact model documented in docs/05_Database.md (the
risk_assessments table's ``likelihood`` and ``impact`` columns), so
the score is never an opaque black box.

Model
-----
- ``likelihood`` is taken directly from ``Threat.confidence.value``
  (already a Probability on [0, 1]): a direct proxy for how likely it
  is that the detected threat is real.
- ``impact`` is derived from ``Threat.severity`` through the explicit
  mapping in ``_IMPACT_BY_SEVERITY`` below.
- The final score is ``round(likelihood * impact * 100)``, clamped to
  [0, 100] before being wrapped in a RiskScore (which itself enforces
  that range).
"""

from __future__ import annotations

from sentinelx_ai.domain.entities.threat import Threat
from sentinelx_ai.domain.enums.severity import Severity
from sentinelx_ai.domain.value_objects.risk_score import RiskScore

_IMPACT_BY_SEVERITY: dict[Severity, float] = {
    Severity.LOW: 0.25,
    Severity.MEDIUM: 0.50,
    Severity.HIGH: 0.75,
    Severity.CRITICAL: 1.0,
}


def calculate_risk_score(threat: Threat) -> RiskScore:
    """
    Compute the RiskScore of a Threat from its likelihood and impact.

    Args:
        threat:
            The threat to score. ``threat.confidence`` is used as the
            likelihood, ``threat.severity`` is mapped to an impact
            factor via ``_IMPACT_BY_SEVERITY``.

    Returns:
        A RiskScore in [0, 100].
    """
    likelihood = threat.confidence.value
    impact = _IMPACT_BY_SEVERITY[threat.severity]

    score = round(likelihood * impact * 100)
    score = max(0, min(100, score))

    return RiskScore(score)
