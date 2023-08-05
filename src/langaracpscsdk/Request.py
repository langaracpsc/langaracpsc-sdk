import json
import base64
import requests
from enum import IntEnum
from . import Util

class RequestMethod(IntEnum):
    Get = 0
    Post = 1
    Put = 2

class Base64Request:
    MethodStrings = list[str]([ "GET", "POST", "PUT" ])

    @staticmethod
    def SerializePayload(payload: str) -> str:
        return Util.Util.TrimBase64(str(base64.b64encode(payload.encode("utf-8"))))

    def __init__(self, method: RequestMethod, url: str, headers: dict[str] = {}, payload = str()):
        self.Method: RequestMethod = method
        self.URL: str = url
        self.Payload = payload
        self.Headers: dict[str, object] = headers

        self.Headers.update({"request": Base64Request.SerializePayload(payload)})

        self.RequestSession = requests.Session()
        self.mRequest: requests.PreparedRequest = requests.Request(Base64Request.MethodStrings[int(self.Method)], self.URL, headers=self.Headers).prepare()

    def Send(self) -> requests.Response:
        return self.RequestSession.send(self.mRequest)

class ImageRequest(Base64Request):
    def __init__(self, url: str, method: RequestMethod):
        pass

    def Send() -> requests.Response:
        return None
