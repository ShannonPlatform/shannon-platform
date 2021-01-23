from __future__ import annotations
from os import PRIO_PGRP
from pydantic import BaseModel, parse_file_as
from typing import Any, Dict, List, Optional

from shannon_platform.base.notification_center import NotificationCenter


class Switch(BaseModel):
    id: str
    name: Optional[str]
    _state: bool

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

