"""
Prevention Executed Domain Event.
"""

from dataclasses import dataclass

from sentinelx_ai.domain.entities.prevention_action import PreventionAction


@dataclass(frozen=True, slots=True)
class PreventionExecuted:
    """
    Event raised when a prevention action is executed.
    """

    action: PreventionAction
