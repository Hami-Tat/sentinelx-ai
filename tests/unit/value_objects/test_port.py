import pytest

from sentinelx_ai.domain.value_objects.port import Port


def test_valid_port():
    port = Port(443)

    assert int(port) == 443
    assert str(port) == "443"


def test_minimum_port():
    assert Port(0).value == 0


def test_maximum_port():
    assert Port(65535).value == 65535


@pytest.mark.parametrize("port", [-1, 65536, 70000])
def test_invalid_port(port: int):
    with pytest.raises(ValueError):
        Port(port)
