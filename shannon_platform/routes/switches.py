from fastapi import APIRouter
from typing import List

from shannon_platform.model.switch import Switch


router = APIRouter()


@router.get('/', response_model=List[Switch])
def get_switches():
    return [Switch(id='qweqwe', name='lamp', state=False)]

@router.get('/{switch_id}', response_model=Switch)
def get_switch(switch_id: str):
    selected_switch = list(filter(lambda switch: switch.id==switch_id, Switch.all()))[0]
    return selected_switch

@router.put('/{switch_id}', status_code=204)
def update_switch(switch_id: str, state: bool):
    pass
    
