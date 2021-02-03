from typing import Any, Dict, List, Optional
import time

from shannon_platform.model.switch import Switch
from shannon_platform.model.sensor import Sensor, SensorDelegate


class Bot:
    def __init__(self, id: int, name: str) -> None:
        self.id: int = id
        self.name: str = name
        self.enable: bool = False


class AutoLight(Bot, SensorDelegate):
    def __init__(self, lamp: Switch, motion: Sensor) -> None:
        super().__init__(0x51, 'Automatic Light Controller')

        self.lamp = lamp
        self.motion = motion
        self.motion.delegate = self

        self.__motion_last_sensing = int(time.time())
        self.__MOTION_DELAY = 10 * 60

    def sensor_did_update(self, sensor: Sensor, state: bool) -> None:
        if self.enable == False:
            return
        
        current_time = int(time.time())
        is_delay_pass = (self.__motion_last_sensing + self.__MOTION_DELAY < current_time)

        if state:
            self.lamp.state = True
        elif self.lamp.state and (not is_delay_pass):
            self.lamp.state = True
        else:
            self.lamp.state = False
