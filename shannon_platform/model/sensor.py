from pydantic import BaseModel

class Sensor(BaseModel):
    id: str
    name: str

    

    value: int