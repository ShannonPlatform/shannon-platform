from __future__ import annotations
from pydantic import BaseModel, parse_file_as
from typing import List


class Switch(BaseModel):
    id: str
    name: str
    state: bool

    def all() -> List[Switch]:
        return parse_file_as(List[Switch], '/etc/switches.json')