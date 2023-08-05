import os
import json
import requests
from . import Request
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
        self.StudentID: int = studentid
        self.FirstName: str = firstname
        self.LastName: str = lastname
        self.Position: ExecPosition = position
        self.Email: str = email

    def ToJson(self) -> str:
        return json.dumps(dict({ "studentid": self.StudentID, "firstname": self.FirstName, "lastname": self.LastName, "position": int(self.Position), "email": self.Email }))

class ExecManager:
    def __init__(self, apikey: str, baseurl: str):
        self.APIKey: str = apikey
        self.BaseURL: str = baseurl

    @staticmethod
    def FromJson(jsonStr: str) -> Exec:
        try:
            jsonMap = json.loads(jsonStr)
            return Exec(jsonMap["studentid"], jsonMap["firstname"], jsonMap["lastName"], jsonMap["position"], jsonMap["email"])

        except JsonDecodeError:
            print(f"Failed to decode \'{jsonStr}\'")

        return None

    def CreateExec(self, _exec: Exec) -> dict:
        response: requests.Response = Request.Base64Request(Request.RequestMethod.Post, f"{self.BaseURL}/Exec/Create", dict({ "apikey": self.APIKey}), _exec.ToJson()).Send()

        if (not(response.ok)):
            print(response.reason)

        responseMap = response.json()

        if (responseMap["Type"] == 0):
            print(responseMap)
            return None

        return responseMap["Payload"]

    def EndTenure(self, studentid: str) -> bool:
        response: requests.Response = Request.Base64Request(Request.RequestMethod.Post, f"{self.BaseURL}/Exec/End", dict({"apikey": self.APIKey}, json.dumps(dict({"studentid": studentid})))).Send()

        if (not(response.ok)):
            print(response.reason)

        return response.ok

    def ListAll(self) -> list[dict]:
        response: requests.Response = Request.Base64Request(Request.RequestMethod.Get, f"{self.BaseURL}/Exec/ListAll", dict({"apikey": self.APIKey})).Send()

        if (not(response.ok)):
            print(response.reason)
            return None

        responseMap = response.json()

        if (responseMap["Type"] == 0):
            print(responseMap)
            return None

        return response.json()["Payload"]

class ExecProfile:
    def __init__(self, studentid: int, imageId: str, description: str):
        self.StudentID = studentid
        self.ImageID = imageId
        self.Description = description

    def ToJson(self):
        return json.dumps(dict({ "studentid": self.StudentID, "imageid": self.ImageID, "description": self.Description }))

class ExecImage:
    def __init__(self, studentid: str, imagepath: str):
        self.StudentID = studentid
        self.ImagePath = imagepath
        self.image
