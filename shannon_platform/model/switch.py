from __future__ import annotations
from typing import Any, Dict, List, Optional

from shannon_platform.base.notification_center import NotificationCenter


class Switch:
    def __init__(self, id: int, state: bool, name: str=None) -> None:
        self.id: int = id
        self.name: str = name
        self._state: bool = state
        
    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, is_on: bool) -> None:
        self._state = is_on

        if is_on:
            NotificationCenter().post(
                name="com.shannon.device-send",
                user_info={
                    'id': self.id,
                    'value': 0x01
                }
            )
        else:
            NotificationCenter().post(
                name="com.shannon.device-send",
                user_info={
                    'id': self.id,
                    'value': 0x02
                }
            )

