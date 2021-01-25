from typing import List
from fastapi import APIRouter

from shannon_platform.model.sensor import Sensor
from shannon_platform.base.notification_center import NotificationCenter, NotificationDefaultNames


router = APIRouter()
sensors: List[Sensor] = []

@router.get('/')
def get_sensors():
    return sensors

@router.get('/{sensor_id}')
def get_sensor(sensor_id: str):
    return None


def register_sensors(user_info) -> None:
    device_id = user_info['id']

    # check sensor type
    if device_id >= 0x20 and device_id <= 0x2f:

        # check sensor is exist
        if not device_id in map(lambda sensor: sensor.id, sensors):
            new_sensor = Sensor(id=device_id)
            sensors.append(new_sensor)


NotificationCenter().add_observer(NotificationDefaultNames.REGISTER, register_sensors)