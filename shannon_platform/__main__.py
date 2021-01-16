from shannon_platform.model.switch import Switch
from shannon_platform.model.sensor import Sensor
import uvicorn
from typing import Optional
from fastapi import FastAPI

from shannon_platform.routes import sensors, switches


app = FastAPI()

@app.get('/')
def index():
    return {"message": "shannon home automation platform"}

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
    uvicorn.run(app, port=80, host='0.0.0.0')

if __name__ == '__main__':
    main()