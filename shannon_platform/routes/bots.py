from fastapi import APIRouter, HTTPException, Response
from typing import List

from shannon_platform.model.bot import *
from shannon_platform.model.switch import Switch
from shannon_platform.model.sensor import Sensor
from shannon_platform.base.notification_center import NotificationCenter, NotificationDefaultNames


router = APIRouter()
bots: List[Bot] = [
    AutoLight(lamp=Switch(12), motion=Sensor(0x21))
]

@router.get('/')
def get_bots():
    return bots

@router.get('/{bot_id}')
def get_bot(bot_id: int):
    selected_bot = next((bot for bot in bots if bot.id==bot_id), None)
    if selected_bot:
        return {'state': selected_bot.enable}
    else:
        raise HTTPException(404, f'Bot with id {bot_id} not found.')

@router.put('/{bot_id}', status_code=204)
def update_bot(bot_id: int, enable: bool):
    selected_bot = next((bot for bot in bots if bot.id==bot_id), None)
    if selected_bot:
        selected_bot.enable = enable
        return Response(status_code=204)
    else:
        raise HTTPException(404, f'Bot with id {bot_id} not found.')
