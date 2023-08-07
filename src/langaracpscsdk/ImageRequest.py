import requests
from . import Request

class ImageRequest(Request.Base64Request):
    def __init__(self, url: str, apikey: str, image: ExecImage):
        super(url, RequestMethod.Put)

        self.Image = image

        self.Headers.update("apikey", apikey)
        self.Payload = dict({ "Request": Util.Util.GetBase64String(self.Image.ToJson()) })

        self.RequestSession= requests.Session()
        self.mRequest = requests.Request(Base64Request.MethodStrings[int(self.Method)], self.URL, json=self.Payload, headers=self.Headers).prepare()
