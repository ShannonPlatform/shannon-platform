import json
from typing import List
from fastapi import APIRouter
from pydantic import parse_obj_as

from shannon_platform.model.sensor import Sensor


router = APIRouter()


@router.get('/', response_model=list[Sensor])
def get_sensors():
    return Sensor.all()

@router.get('/{sensor_id}', response_model=Sensor)
def get_sensor(sensor_id: str):
    return None
