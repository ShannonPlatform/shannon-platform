import uvicorn
from fastapi import FastAPI

from shannon_platform.routes import sensors, switches
from shannon_platform.services.serial import SerialService
# from shannon_platform.services.bluetooth import BluetoothService


app = FastAPI()
services = [
    SerialService(port="/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_854333332313515052D0-if00"),
    # BluetoothService(address='')
]


@app.get('/')
def index():
    return {"message": "shannon home automation platform"}

@app.on_event("shutdown")
def shutdown_event():
    for service in services:
        service.shutdown()

app.include_router(
    sensors.router,
    prefix='/sensors',
    tags=['sensors']
)

app.include_router(
    switches.router,
    prefix='/switches',
    tags=['switches']
)

def main():
    for service in services:
        service.request_devices()

    uvicorn.run(app, port=80, host='0.0.0.0')

if __name__ == '__main__':
    main()