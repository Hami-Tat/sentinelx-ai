import pytest

from sentinelx_ai.domain.value_objects.mac_address import MACAddress


def test_valid_mac_colon():
    mac = MACAddress("AA:BB:CC:DD:EE:FF")

    assert str(mac) == "AA:BB:CC:DD:EE:FF"


def test_valid_mac_dash():
    mac = MACAddress("aa-bb-cc-dd-ee-ff")

    assert str(mac) == "AA-BB-CC-DD-EE-FF"


@pytest.mark.parametrize(
    "address",
    [
        "INVALID",
        "AA:BB:CC",
        "GG:BB:CC:DD:EE:FF",
        "AA:BB:CC:DD:EE",
    ],
)
def test_invalid_mac(address: str):
    with pytest.raises(ValueError):
        MACAddress(address)
