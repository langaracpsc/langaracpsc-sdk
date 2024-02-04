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
    """Stores info about an Exec
    """
    def __init__(self, studentid: int, firstname: str, lastname: str, position: ExecPosition, email: str):
        """Contstructor

        Args:
            studentid (int): Exec's student ID
            firstname (str): Exec's  First name
            lastname (str): Exec's Last name
            position (ExecPosition): Exec's position
            email (str): Exec's email
        """
        self.StudentID: int = studentid
        self.FirstName: str = firstname
        self.LastName: str = lastname
        self.Position: ExecPosition = position
        self.Email: str = email

    def ToDict(self) -> dict:
        """Generates a dictionary from the current object

        Returns:
            dict: Generated dictionary
        """
        return dict({ "studentid": self.StudentID, "firstname": self.FirstName, "lastname": self.LastName, "position": int(self.Position), "email": self.Email })

    def ToJson(self) -> str:
        """Converts the current object to json.

        Returns:
            str: Generated json
        """
        return json.dumps(self.ToDict())


class ExecManager:
    """Routines for managing Exec objects.
    """
    def __init__(self, baseurl: str, apikey: str):
        """Constructor

        Args:
            baseurl (str): API base url
            apikey (str): API Key
        """
        self.APIKey: str = apikey
        self.BaseURL: str = baseurl

    @staticmethod
    def FromJson(jsonStr: str) -> Exec:
        """Generates an Exec from json.

        Args:
            jsonStr (str): Json to convert.

        Returns:
            Exec: Generated Exec.
        """
        try:
            jsonMap = json.loads(jsonStr)
            return Exec(jsonMap["studentid"], jsonMap["firstname"], jsonMap["lastName"], jsonMap["position"], jsonMap["email"])

        except json.JSONDecodeError:
            print(f"Failed to decode \'{jsonStr}\'")

        return None

    def CreateExec(self, _exec: Exec) -> dict:
        """
        Args:
            _exec (Exec): Adds the given Exec to the database 

        Returns:
            dict: Created Exec dict as a confirmation.
        """
        response: requests.Response = JsonRequest(RequestMethod.Post, f"{self.BaseURL}/Create", dict({ "apikey": self.APIKey}), _exec.ToDict()).Send()

        if (not(response.ok)):
            print(response.reason)

        responseMap = response.json()

        if (responseMap["Type"] == 0):
            print(responseMap)
            return None

        return responseMap["Payload"]

    def CreateExecDict(self, _exec: dict) -> dict:
        """
        Args:
            _exec (Exec): Adds the given Exec dict to the database 

        Returns:
            dict: Created Exec dict as a confirmation.
        """
        response: requests.Response = JsonRequest(RequestMethod.Post, f"{self.BaseURL}/Create", dict({ "apikey": self.APIKey}), _exec).Send()

        if (not(response.ok)):
            print(response.reason)

        responseMap = response.json()

        if (responseMap["Type"] == 0):
            print(responseMap)
            return None

        return responseMap["Payload"]


    def EndTenure(self, studentid: int) -> bool:
        """Ends the tenure for the Exec with the given student ID.

        Args:
            studentid (int): Student ID for the exec. 

        Returns:
            bool: Execution status.
        """
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
        """Fetches and lists all the Execs in the db

        Returns:
            list[dict]: Fetched execs.
        """
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
        """Updates the given exec info on the backend.

        Args:
            execMap (dict): Exec info to update

        Returns:
            dict: Changed exec as a confirmation.
        """
        response: requests.Response = JsonRequest(RequestMethod.Post, f"{self.BaseURL}/Update", dict({"apikey": self.APIKey}), execMap).Send()

        if (not(response.ok)):
            print(response.reason)
            return None

        responseMap = response.json()

        if (responseMap["Type"] == 0):
            print(responseMap)
            return None

        return response.json()["Payload"]

