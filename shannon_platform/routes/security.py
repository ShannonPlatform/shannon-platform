from fastapi import APIRouter, HTTPException, Response

from shannon_platform.model.security import Security, SecurityState

router = APIRouter()
security_device = Security()

@router.get('/')
def get_security_state():
    if security_device.state == SecurityState.STAY:
        return Response(b"0")
    elif security_device.state == SecurityState.AWAY:
        if security_device.is_motion_detected:
            return Response(b"4")
        else:
            return Response(b"1")
    elif security_device.state == SecurityState.NIGHT:
        if security_device.door_did_open:
            return Response(b"4")
        else:
            return Response(b"2")
    elif security_device.state == SecurityState.DISARM:
        return Response(b"3")

@router.get('/set', status_code=204)
def set_security(state: SecurityState):
    security_device.state = state
    return Response(status_code=204)

@router.get('/trigger')
def get_security_trigger():
    if security_device.state == SecurityState.STAY:
        return Response(b"0")
    elif security_device.state == SecurityState.AWAY:
        return Response(b"1")
    elif security_device.state == SecurityState.NIGHT:
        return Response(b"2")
    elif security_device.state == SecurityState.DISARM:
        return Response(b"3")
    
