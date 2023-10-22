import json
import requests
from enum import IntEnum

class RequestMethod(IntEnum):
    Get = 0
    Post = 1
    Put = 2

MethodStrings: list[str] = list[str]([ "GET", "POST", "PUT" ])

class JsonRequest:
    """Http request with a json body
    """
    def __init__(self, method: RequestMethod, url: str, headers: dict = dict(), payload: dict = dict()):
        """Constructor

        Args:
            method (RequestMethod): HTTP method
            url (str): URL
            headers (dict, optional): Request headers. Defaults to dict().
            payload (dict, optional): Request body/payload. Defaults to dict().
        """
        self.Method: RequestMethod = method
        self.URL: str = url
        self.Payload = json.dumps(payload)
        self.Headers: dict = headers

        self.Headers["Content-Type"] = "application/json"

        self.RequestSession: requests.Session = requests.Session()
        self.mRequest: requests.PreparedRequest = requests.Request(MethodStrings[int(self.Method)], self.URL, headers=self.Headers, data=self.Payload).prepare()
   
    def Send(self) -> requests.Response:
        """Sends the request.

        Returns:
            requests.Response: Returned response.
        """
        return self.RequestSession.send(self.mRequest)
    
    def ToDict(self) -> dict:
        """Generates a dict from the current object

        Returns:
            dict: Generated dict.  
        """
        return {
            "method": self.Method,
            "url": self.URL,
            "payload": self.Payload,
            "headers": self.Headers
        }