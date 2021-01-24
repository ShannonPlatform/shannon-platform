from typing import Any, Dict

from shannon_platform.base.notification_center import NotificationCenter

class Sensor:
    def __init__(self, id: str, value: int=0, name: str=None) -> None:
        self.id: int = id
        self.name: str = name
        self._value: int = value
        
        NotificationCenter().add_observer('com.shannon.device-receive', callback=self.__value_changed)


    @property
    def value(self):
        return self._state

    def __value_changed(self, user_info: Dict[str, Any]) -> None:
        if user_info['id'] == self.id:
            self.value = user_info['value']