"""
Unit tests for risk_calculator.
"""

from __future__ import annotations

from datetime import UTC, datetime

import pytest

from sentinelx_ai.application.risk_engine.risk_calculator import (
    calculate_risk_score,
)
from sentinelx_ai.domain.entities.threat import Threat
from sentinelx_ai.domain.enums.severity import Severity
from sentinelx_ai.domain.enums.threat_type import ThreatType
from sentinelx_ai.domain.value_objects.probability import Probability
from sentinelx_ai.domain.value_objects.risk_score import RiskScore
from sentinelx_ai.domain.value_objects.timestamp import Timestamp


def make_threat(severity: Severity, confidence: float) -> Threat:
    return Threat(
        identifier="THR-001",
        threat_type=ThreatType.DOS,
        severity=severity,
        confidence=Probability(confidence),
        risk_score=RiskScore(0),
        detected_at=Timestamp(datetime(2026, 7, 15, tzinfo=UTC)),
    )


@pytest.mark.parametrize(
    ("severity", "impact"),
    [
        (Severity.LOW, 0.25),
        (Severity.MEDIUM, 0.50),
        (Severity.HIGH, 0.75),
        (Severity.CRITICAL, 1.0),
    ],
)
def test_calculate_risk_score_per_severity(severity: Severity, impact: float) -> None:
    """Each Severity must use its documented impact factor."""
    confidence = 0.8
    threat = make_threat(severity, confidence)

    score = calculate_risk_score(threat)

    assert score.value == round(confidence * impact * 100)


def test_calculate_risk_score_zero_confidence() -> None:
    """Zero likelihood must yield the lowest possible score."""
    threat = make_threat(Severity.CRITICAL, 0.0)

    score = calculate_risk_score(threat)

    assert score.value == 0


def test_calculate_risk_score_full_confidence_critical_severity() -> None:
    """Full likelihood with the highest impact must yield the
    highest possible score."""
    threat = make_threat(Severity.CRITICAL, 1.0)

    score = calculate_risk_score(threat)

    assert score.value == 100


def test_calculate_risk_score_returns_a_risk_score() -> None:
    threat = make_threat(Severity.MEDIUM, 0.5)

    score = calculate_risk_score(threat)

    assert isinstance(score, RiskScore)
