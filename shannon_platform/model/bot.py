from typing import Any, Dict, List, Optional
import time

from shannon_platform.model.switch import Switch
from shannon_platform.model.sensor import Sensor


class Bot:
    def __init__(self, id: int, name: str) -> None:
        self.id: int
        self.name: str
        self.enable: bool = False


class AutoLight(Bot):
    def __init__(self, lamp: Switch, motion: Sensor) -> None:
        super().__init__(0x51, 'Automatic Light Controller')

        self.lamp = lamp
        self.motion = motion

        self.__motion_last_sensing = int(time.time())

        self.motion.value_did_changed = self.motion_did_changed


    def motion_did_change(self):
        if self.enable == False:
            return
        
        current_time = int(time.time())
        is_delay_pass = (self.__motion_last_sensing + self.__MOTION_DELAY < current_time)

        if self.motion.value:
            self.lamp.state = True
        elif self.lamp.state and (not is_delay_pass):
            self.lamp.state = True
        else:
            self.lamp.state = False
