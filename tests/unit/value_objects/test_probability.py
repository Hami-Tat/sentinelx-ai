import pytest

from sentinelx_ai.domain.value_objects.probability import Probability


def test_valid_probability():
    probability = Probability(0.95)

    assert float(probability) == 0.95
    assert probability.percentage() == 95.0


def test_zero_probability():
    assert Probability(0.0).value == 0.0


def test_one_probability():
    assert Probability(1.0).value == 1.0


@pytest.mark.parametrize("value", [-0.1, 1.1, 2.0])
def test_invalid_probability(value: float):
    with pytest.raises(ValueError):
        Probability(value)
