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
        response: requests.Response = Request.Base64Request(Request.RequestMethod.Post, f"{self.BaseURL}/Create", dict({ "apikey": self.APIKey}), _exec.ToJson()).Send()

        if (not(response.ok)):
            print(response.reason)

        responseMap = response.json()

        if (responseMap["Type"] == 0):
            print(responseMap)
            return None

        return responseMap["Payload"]

    def EndTenure(self, studentid: int) -> bool:
        response: requests.Response = Request.Base64Request(Request.RequestMethod.Post, f"{self.BaseURL}/End", dict({"apikey": self.APIKey}), json.dumps(dict({"studentid": studentid}))).Send()

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
        response: requests.Response = Request.Base64Request(Request.RequestMethod.Get, f"{self.BaseURL}/ListAll", dict({"apikey": self.APIKey})).Send()

        if (not(response.ok)):
            print(response.reason)
            return None

        responseMap = response.json()

        if (responseMap["Type"] == 0):
            print(responseMap)
            return None

        return response.json()["Payload"]

    def UpdateExec(self, execMap: dict) -> dict:
        response: requests.Response = Request.Base64Request(Request.RequestMethod.Post, f"{self.BaseURL}/Update", dict({"apikey": self.APIKey}), json.dumps(execMap)).Send()

        if (not(response.ok)):
            print(response.reason)
            return None

        responseMap = response.json()

        if (responseMap["Type"] == 0):
            print(responseMap)
            return None

        return response.json()["Payload"]

class ExecImage:
    def __init__(self, studentid: int, name: str, imageBuffer: str):
        self.StudentID: int = studentid
        self.Name: str = name
        self.ImageBuffer: str = imageBuffer


class ExecImageManager:
    def __init__(self, baseURL: str, apikey: str):
        self.BaseURL: str = baseURL
        self.APIKey: str = apikey

    def LoadImageFromFile(self, studentid: int, imagePath: str) -> ExecImage:
        if (not(os.path.exists(imagePath))):
            print(f"File {imagePath} doesn't exist.")
            return None

        execImage: ExecImage = None

        with open(imagePath, 'r') as fp:
            execImage = ExecImage(studentid, studentid, Util.Util.GetBase64String(fp.read()))

        return execImage

class ExecProfile:
    def __init__(self, studentid: int, imageId: str, description: str):
        self.StudentID: int = studentid
        self.ImageID: str = imageId
        self.Description: str = description

    def ToJson(self):
        return json.dumps(dict({ "studentid": self.StudentID, "imageid": self.ImageID, "description": self.Description }))

class ExecProfileManager:
    def __init__(self, baseURL: str, apikey: str):
        self.BaseURL = baseURL
        self.APIKey: str = apikey

    def CreateProfile(self, execProfile: ExecProfile):
        response: requests.Response = Request.Base64Request(Request.RequestMethod.Post, f"{self.BaseURL}/Create", dict({"apikey": self.APIKey}), json.dumps(execMap)).Send()

        if (not(response.ok)):
            print(response.reason)
            return None

        responseMap = response.json()

        if (responseMap["Type"] == 0):
            print(responseMap)
            return None

        return response.json()["Payload"]


