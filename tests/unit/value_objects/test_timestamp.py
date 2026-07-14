from datetime import datetime

from sentinelx_ai.domain.value_objects.timestamp import Timestamp


def test_timestamp_creation():
    timestamp = Timestamp(datetime(2026, 7, 14, 12, 0, 0))

    assert timestamp.value.year == 2026
    assert timestamp.value.month == 7
    assert timestamp.value.day == 14


def test_timestamp_now():
    timestamp = Timestamp.now()

    assert isinstance(timestamp.value, datetime)


def test_timestamp_string():
    timestamp = Timestamp(datetime(2026, 1, 1, 10, 30, 0))

    assert str(timestamp) == "2026-01-01T10:30:00"
