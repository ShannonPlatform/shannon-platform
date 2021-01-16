import json
from typing import List
from fastapi import APIRouter
from pydantic import parse_obj_as

from shannon_platform.model.sensor import Sensor
from shannon_platform.connection.serial import SerialConnection


router = APIRouter()


@router.get('/', response_model=list[Sensor])
def get_sensors():
    return Sensor.all()

@router.get('/{sensor_id}', response_model=Sensor)
def get_sensor(sensor_id: str):
    serial_connection = SerialConnection()
    responce = serial_connection.request(sensor_id)

    return parse_obj_as(Sensor, json.loads(responce))
