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
    def __init__(self, studentid: int, firstname: str, lastname: str, position: ExecPosition, email: str):
        self.StudentID = studentid
        self.FirstName = firstname
        self.LastName = lastname
        self.Position = position
        self.Email = email

    def ToJson(self) -> str:
        return json.dumps(dict({ "studentid": self.StudentID, "firstname": self.FirstName, "lastname": self.LastName, "position": int(self.Position), "email": self.Email }))
