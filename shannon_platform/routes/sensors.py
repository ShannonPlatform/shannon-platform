from typing import List
from fastapi import APIRouter, HTTPException

from shannon_platform.model.sensor import Sensor
from shannon_platform.base.notification_center import NotificationCenter, NotificationDefaultNames


router = APIRouter()
sensors: List[Sensor] = []

@router.get('/')
def get_sensors():
    return sensors

@router.get('/{sensor_id}')
def get_sensor(sensor_id: int):
    sensor = next((sensor for sensor in sensors if sensor.id==sensor_id), None)
    if sensor:
        return sensor
    else:
        raise HTTPException(404, f'Sensor with id {sensor_id} not found.')


def register_sensors(user_info) -> None:
    device_id = user_info['id']

    # check sensor type
    if device_id >= 0x20 and device_id <= 0x2f:

        # check sensor is exist
        if not device_id in map(lambda sensor: sensor.id, sensors):
            new_sensor = Sensor(id=device_id)
            sensors.append(new_sensor)


NotificationCenter().add_observer(NotificationDefaultNames.REGISTER, register_sensors)