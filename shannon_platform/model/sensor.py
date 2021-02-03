from typing import Any, Callable, Dict

from shannon_platform.base.notification_center import NotificationCenter, NotificationDefaultNames

class Sensor:
    def __init__(self, id: int, value: int=0, name: str=None) -> None:
        self.id: int = id
        self.name: str = name
        self._value: int = value
        self.delegate: SensorDelegate = None
        
        NotificationCenter().add_observer(NotificationDefaultNames.DATA_RECEIVE, callback=self.__value_changed)

    def __del__(self) -> None:
        NotificationCenter().remove_observer(self.__value_changed)

    @property
    def value(self) -> int:
        return self._value

    def __value_changed(self, user_info: Dict[str, Any]) -> None:
        if user_info['id'] == self.id:
            
            new_value = user_info['value']
            if self._value == new_value:
                return

            self._value = user_info['value']
            
            if self.delegate:
                self.delegate.sensor_did_update(self, new_value)

class SensorDelegate:
    def sensor_did_update(self, sensor: Sensor, state: bool) -> None:
        raise NotImplementedError