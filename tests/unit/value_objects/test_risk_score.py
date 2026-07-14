import pytest

from sentinelx_ai.domain.value_objects.risk_score import RiskScore


def test_valid_risk_score():
    score = RiskScore(85)

    assert int(score) == 85
    assert score.normalized == 0.85


def test_minimum_score():
    assert RiskScore(0).value == 0


def test_maximum_score():
    assert RiskScore(100).value == 100


@pytest.mark.parametrize("value", [-1, 101, 200])
def test_invalid_risk_score(value: int):
    with pytest.raises(ValueError):
        RiskScore(value)
