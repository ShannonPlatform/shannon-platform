from typing import Any
from pydantic import BaseModel

from shannon_platform.base.notification_center import NotificationCenter

class Sensor(BaseModel):
    id: str
    name: str
    _value: int

    @property
    def value(self):
        return self._state

    def __init__(__pydantic_self__, **data: Any) -> None:
        super().__init__(**data)
        
        NotificationCenter().add_observer('com.shannon.device-receive', callback=__pydantic_self__.__value_changed)

    def __value_changed(self):
        pass