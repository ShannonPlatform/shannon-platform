from fastapi import APIRouter
from typing import List

from shannon_platform.model.switch import Switch
from shannon_platform.service.serial import SerialService


router = APIRouter()


@router.get('/', response_model=List[Switch])
def get_switches():
    return Switch.all()

@router.get('/{switch_id}', response_model=Switch)
def get_switch(switch_id: str):
    selected_switch = list(filter(lambda switch: switch.id==switch_id, Switch.all()))[0]
    return selected_switch

@router.put('/{switch_id}', status_code=204)
def update_switch(switch_id: str, state: bool):
    selected_switch = list(filter(lambda switch: switch.id==switch_id, Switch.all()))[0]
    selected_switch.state = state

    serial_service = SerialService()
    serial_service.request(selected_switch.json())
    
