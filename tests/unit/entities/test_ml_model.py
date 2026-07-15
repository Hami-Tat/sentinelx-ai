from datetime import UTC, datetime

from sentinelx_ai.domain.entities.ml_model import MLModel
from sentinelx_ai.domain.value_objects.timestamp import Timestamp


def test_create_ml_model():
    model = MLModel(
        identifier="ML-001",
        name="Random Forest",
        version="1.0",
        accuracy=0.99,
        created_at=Timestamp(datetime(2026, 7, 15, tzinfo=UTC)),
    )

    assert model.name == "Random Forest"
    assert model.accuracy == 0.99
