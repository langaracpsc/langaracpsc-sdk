import os
import json
import requests
from enum import IntEnum

class ExecPosition(IntEnum):
    President = 0
    VicePresident = 1
    TechLead = 2
    GeneralRep = 3
    PublicRelations = 4
    Finance = 5
    Events = 6


class Exec:
    def __init__(self, studentid: str, firstname: str, lastname: str, position: ExecPosition):
        self.StudentID = studentid
        self.FirstName = firstname
        self.LastName = lastname
        self.Position = position

    def ToJson(self) -> str:
        return json.dumps(dict({ "firstname": self.FirstName, "lastname": self.LastName, "position": int(self.Position) }))
