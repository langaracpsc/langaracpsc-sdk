import json
import base64
import requests
from enum import IntEnum
from Util import Util

class RequestMethod(IntEnum):
    Get = 0
    Post = 1
    Put = 2

MethodStrings: list = list[str]([ "GET", "POST", "PUT" ])
class JsonRequest:
    def __init__(self, method: RequestMethod, url: str, headers: dict[str] = {}, payload = str()):
        json.loads(payload) # will throw an exception on invalid JSON
        
        self.Method: RequestMethod = method
        self.URL: str = url
        self.Payload = payload
        self.Headers: dict[str, object] = headers

        self.Headers["Content-Type"] = "application/json"

        self.RequestSession: requests.Session = requests.Session()
        self.mRequest: requests.PreparedRequest = requests.Request(MethodStrings[int(self.Method)], self.URL, headers=self.Headers).prepare()

    def Send(self) -> requests.Response:
        return self.RequestSession.send(self.mRequest)