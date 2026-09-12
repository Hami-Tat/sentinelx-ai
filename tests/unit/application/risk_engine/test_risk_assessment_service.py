"""
Unit tests for RiskAssessmentService.
"""

from __future__ import annotations

from datetime import UTC, datetime

import pytest

from sentinelx_ai.application.risk_engine.risk_assessment_service import (
    RiskAssessmentService,
)
from sentinelx_ai.domain.entities.risk_assessment import RiskAssessment
from sentinelx_ai.domain.entities.threat import Threat
from sentinelx_ai.domain.enums.severity import Severity
from sentinelx_ai.domain.enums.threat_type import ThreatType
from sentinelx_ai.domain.value_objects.probability import Probability
from sentinelx_ai.domain.value_objects.risk_score import RiskScore
from sentinelx_ai.domain.value_objects.timestamp import Timestamp


def make_threat(severity: Severity, confidence: float = 0.9) -> Threat:
    return Threat(
        identifier="THR-001",
        threat_type=ThreatType.DOS,
        severity=severity,
        confidence=Probability(confidence),
        risk_score=RiskScore(0),
        detected_at=Timestamp(datetime(2026, 7, 15, tzinfo=UTC)),
    )


@pytest.mark.parametrize(
    "severity",
    [Severity.LOW, Severity.MEDIUM, Severity.HIGH, Severity.CRITICAL],
)
def test_assess_returns_a_consistent_risk_assessment(severity: Severity) -> None:
    """For every Severity, the returned RiskAssessment must be built
    from the given threat and carry a valid score."""
    service = RiskAssessmentService()
    threat = make_threat(severity)

    assessment = service.assess(threat, identifier="RISK-001")

    assert isinstance(assessment, RiskAssessment)
    assert assessment.identifier == "RISK-001"
    assert assessment.threat is threat
    assert isinstance(assessment.assessed_at, Timestamp)


def test_assess_updates_threat_risk_score_in_place() -> None:
    """Threat.risk_score and RiskAssessment.score must stay
    consistent: assess() must mutate the threat in place rather than
    leaving its original risk_score untouched."""
    service = RiskAssessmentService()
    threat = make_threat(Severity.HIGH, confidence=0.8)
    original_risk_score = threat.risk_score

    assessment = service.assess(threat, identifier="RISK-002")

    expected_score = round(0.8 * 0.75 * 100)

    assert threat.risk_score.value == expected_score
    assert threat.risk_score is not original_risk_score
    assert assessment.score.value == threat.risk_score.value
