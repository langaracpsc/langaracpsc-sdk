import os
import json
import requests
from langaracpscsdk.Request import JsonRequest, RequestMethod
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

    def ToDict(self) -> dict:
        return dict({ "studentid": self.StudentID, "firstname": self.FirstName, "lastname": self.LastName, "position": int(self.Position), "email": self.Email })

    def ToJson(self) -> str:
        return json.dumps()

class ExecManager:
    def __init__(self, baseurl: str, apikey: str):
        self.APIKey: str = apikey
        self.BaseURL: str = baseurl

    @staticmethod
    def FromJson(jsonStr: str) -> Exec:
        try:
            jsonMap = json.loads(jsonStr)
            return Exec(jsonMap["studentid"], jsonMap["firstname"], jsonMap["lastName"], jsonMap["position"], jsonMap["email"])

        except json.JSONDecodeError:
            print(f"Failed to decode \'{jsonStr}\'")

        return None

    def CreateExec(self, _exec: Exec) -> dict:
        response: requests.Response = JsonRequest(RequestMethod.Post, f"{self.BaseURL}/Create", dict({ "apikey": self.APIKey}), _exec.ToDict()).Send()

        if (not(response.ok)):
            print(response.reason)

        responseMap = response.json()

        if (responseMap["Type"] == 0):
            print(responseMap)
            return None

        return responseMap["Payload"]

    def CreateExecDict(self, _exec: dict) -> dict:
        response: requests.Response = JsonRequest(RequestMethod.Post, f"{self.BaseURL}/Create", dict({ "apikey": self.APIKey}), _exec).Send()

        if (not(response.ok)):
            print(response.reason)

        responseMap = response.json()

        if (responseMap["Type"] == 0):
            print(responseMap)
            return None

        return responseMap["Payload"]


    def EndTenure(self, studentid: int) -> bool:
        response: requests.Response = JsonRequest(RequestMethod.Post, f"{self.BaseURL}/End", dict({"apikey": self.APIKey}), dict({"studentid": int(studentid)})).Send()

        if (not(response.ok)):
            print(response.reason)
            return False

        responseMap: dict = response.json()

        print(responseMap)

        if (responseMap["Type"] == 0):
            print(responseMap)
            return False

        return True

    def ListAll(self) -> list[dict]:
        response: requests.Response = JsonRequest(RequestMethod.Get, f"{self.BaseURL}/ListAll", dict({"apikey": self.APIKey})).Send()

        if (not(response.ok)):
            print(response.reason)
            return None

        responseMap = response.json()

        if (responseMap["Type"] == 0):
            print(responseMap)
            return None

        return response.json()["Payload"]

    def UpdateExec(self, execMap: dict) -> dict:
        response: requests.Response = JsonRequest(RequestMethod.Post, f"{self.BaseURL}/Update", dict({"apikey": self.APIKey}), execMap).Send()

        if (not(response.ok)):
            print(response.reason)
            return None

        responseMap = response.json()

        if (responseMap["Type"] == 0):
            print(responseMap)
            return None

        return response.json()["Payload"]

