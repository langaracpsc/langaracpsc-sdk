import os
import enum
import json
import requests

class ExecPostion(Enum):
    President,
    VicePresident,
    TechLead,
    GeneralRep,
    PublicRelations,
    Finance,
    Events

class Exec:
    firstname = str()

    lastname = str()

    email = str()

    position = ExecPostion

    def ToJson(self):
        return json.dumps(self)
    
    def __init__(self, _firstname: str, _lastname: str, _email: str, _position: ExecPosition):
        self.firstname = _firstname
        self.lastname = _lastname
        self.email = _email
        self.Position = position
