import os
import json
from . import Request
from . import Util;


class ExecImage:
    def __init__(self, studentid: int, name: str, imageBuffer: str):
        self.StudentID: int = studentid
        self.Name: str = name
        self.ImageBuffer: str = imageBuffer

    def ToJson(self):
        return json.dumps(dict({"id": self.StudentID, "name": self.Name, "buffer": self.ImageBuffer }))

class ImageRequest(Request.Base64Request):
    def __init__(self, url: str, apikey: str, image: ExecImage):
        super(url, RequestMethod.Put)

        self.Image = image

        self.Headers.update("apikey", apikey)
        self.Payload = dict({ "Request": Util.Util.GetBase64String(self.Image.ToJson()) })

        self.RequestSession= requests.Session()
        self.mRequest = requests.Request(Base64Request.MethodStrings[int(self.Method)], self.URL, json=self.Payload, headers=self.Headers).prepare()

class ExecImageManager:
    def __init__(self, baseURL: str, apikey: str):
        self.BaseURL: str = baseURL
        self.APIKey: str = apikey

    def LoadImageFromFile(self, studentid: int, imagePath: str) -> ExecImage:
        if (not(os.path.exists(imagePath))):
            print(f"File {imagePath} doesn't exist.")
            return None

        execImage: ExecImage = None

        with open(imagePath, "rb") as fp:
            execImage = ExecImage(studentid, studentid, Util.Util.GetBase64StringBytes(fp.read()))

        return execImage

    def CreateImage(self, image: ExecImage) -> dict:
        response: request.Response = ImageRequest(self.BaseURL, image).Send()

        if (not(response.ok)):
            print(response.reason)
            return None

        responseMap = response.json()

        if (responseMap["Type"] == 0):
            print(responseMap)
            return None

        return response.json()["Payload"]

