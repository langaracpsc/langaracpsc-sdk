import requests
from . import Request
from Request import JsonRequest

class ImageRequest(JsonRequest):
    def __init__(self, url: str, apikey: str, image: ExecImage):
        super(url, RequestMethod.Put)

        self.Image: Image = image

        self.Headers["apikey"] = apikey
        self.Payload = self.Image.

        self.RequestSession = requests.Session()
        self.mRequest = requests.Request(JsonRequest.MethodStrings[int(self.Method)], self.URL, json=self.Payload, headers=self.Headers).prepare()