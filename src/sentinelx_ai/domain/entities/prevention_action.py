"""
Prevention Action Entity.
"""

from dataclasses import dataclass

from sentinelx_ai.domain.entities.decision import Decision
from sentinelx_ai.domain.enums.prevention_type import PreventionType
from sentinelx_ai.domain.value_objects.timestamp import Timestamp


@dataclass(slots=True)
class PreventionAction:
    """
    Entity representing a prevention action.
    """

    identifier: str
    decision: Decision
    action: PreventionType
    executed_at: Timestamp
