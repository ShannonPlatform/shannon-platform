from fastapi import APIRouter, HTTPException, Response
from typing import List

from shannon_platform.model.switch import Switch
from shannon_platform.base.notification_center import NotificationCenter, NotificationDefaultNames


router = APIRouter()
switches: List[Switch] = []

@router.get('/')
def get_switches():
    return switches

@router.get('/{switch_id}')
def get_switch(switch_id: int):
    selected_switch = next((switch for switch in switches if switch.id==switch_id), None)
    if selected_switch:
        return selected_switch
    else:
        raise HTTPException(404, f'Switch with id {switch_id} not found.')

@router.put('/{switch_id}', status_code=204)
def update_switch(switch_id: int, state: bool):
    selected_switch = next((switch for switch in switches if switch.id==switch_id), None)
    if selected_switch:
        selected_switch.state = state
        return Response(status_code=204)
    else:
        raise HTTPException(404, f'Switch with id {switch_id} not found.')
    

def register_switches(user_info) -> None:
    device_id = user_info['id']

    # check sensor type
    if device_id >= 0x10 and device_id <= 0x1f:

        # check sensor is exist
        if not device_id in map(lambda switch: switch.id, switches):
            new_switch = Switch(id=device_id)
            switches.append(new_switch)


NotificationCenter().add_observer(NotificationDefaultNames.REGISTER, register_switches)