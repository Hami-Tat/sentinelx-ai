import pytest

from sentinelx_ai.domain.value_objects.ip_address import IPAddress


def test_valid_ipv4():
    ip = IPAddress("192.168.1.10")

    assert str(ip) == "192.168.1.10"
    assert ip.version == 4


def test_valid_ipv6():
    ip = IPAddress("2001:db8::1")

    assert ip.version == 6


def test_invalid_ip():
    with pytest.raises(ValueError):
        IPAddress("999.999.999.999")
