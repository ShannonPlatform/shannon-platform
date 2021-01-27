from enum import Enum
from typing import Any, Dict

from shannon_platform.base.notification_center import NotificationCenter, NotificationDefaultNames


class SecurityState(str, Enum):
    STAY = 'STAY'
    AWAY = 'AWAY'
    NIGHT = 'NIGHT'
    DISARM = 'DISARM'

class Security:
    def __init__(self) -> None:
        self.id = 0x40
        self.name = 'Security Device'
        self.state: SecurityState = SecurityState.DISARM
        self.is_motion_detected: bool = False
        self.door_did_open: bool = False

        NotificationCenter().add_observer(name=NotificationDefaultNames.DATA_RECEIVE, callback=self.motion_state_changed)

    def motion_state_changed(self, user_info: Dict[str, Any]):
        if user_info['id'] == 0x21:
            self.is_motion_detected = user_info['value']
    