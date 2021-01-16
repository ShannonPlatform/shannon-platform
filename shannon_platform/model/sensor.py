from __future__ import annotations
from typing import List
from pydantic import BaseModel, parse_file_as

from shannon_platform.connection.serial import SerialConnection

class Sensor(BaseModel):
    id: str
    name: str
    value: int

    def all() -> List[Sensor]:
        return parse_file_as(List[Sensor], '/etc/sensors.json')