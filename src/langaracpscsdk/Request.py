import json
import base64
import requests
from enum import IntEnum
from . import Util

class RequestMethod(IntEnum):
    Get = 0
    Post = 1

class Base64Request:
    MethodStrings = list[str]([ "GET", "POST" ])

    def SerializeHeaders(headers: dict[str]):
        return Util.Util.TrimBase64(str(base64.b64encode(json.dumps(headers).encode("utf-8"))))

    def __init__(self, method: RequestMethod, url: str, headers: dict[str] = {}, payload = str()):
        self.Method: RequestMethod = method
        self.URL: str = url
        self.Payload = payload
        self.Headers: dict[str, object] = headers

        self.Headers.update({"request": Base64Request.SerializeHeaders(payload)})


        self.RequestSession = requests.Session()
        self.mRequest: requests.PreparedRequest = requests.Request(Base64Request.MethodStrings[int(self.Method)], self.URL, headers=self.Headers).prepare()


    def Send(self) -> requests.Response:
        return self.RequestSession.send(self.mRequest)
