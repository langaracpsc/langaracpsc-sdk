import os
import json
import requests
from langaracpscsdk.Request import JsonRequest, RequestMethod
from langaracpscsdk.Util import Util


class ExecImage:
    def __init__(self, studentid: int, name: str, imageBuffer: str):
        self.StudentID: int = studentid
        self.Name: str = name
        self.ImageBuffer: str = imageBuffer

    def ToDict() -> dict:
        return json.dumps(dict({"id": self.StudentID, "name": self.Name, "buffer": self.ImageBuffer }))

    def ToJson(self) -> str:
        return json.dumps(self.ToDict()) 

class ImageRequest(JsonRequest):
    def __init__(self, url: str, apikey: str, image: ExecImage):
        super().__init__(RequestMethod.Put, url)

        self.Image: ExecImage = image

        self.Headers.update({"apikey" : apikey })

        self.Payload = dict(self.Image.ToJson())

        self.RequestSession = requests.Session()
        self.mRequest = requests.Request(Request.Base64Request.MethodStrings[int(self.Method)], self.URL, json=self.Payload, headers=self.Headers).prepare()

        print(self.mRequest)

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
            execImage = ExecImage(studentid, studentid, Util.GetBase64StringBytes(fp.read()))

        return execImage

    def CreateImage(self, image: ExecImage) -> dict:
        response: requests.Response = ImageRequest(f"{self.BaseURL}/Create", self.APIKey, image).Send()

        if (not(response.ok)):
            print(response.reason)
            return None

        responseMap: dict = None 

        try:
            responseMap = response.json()
        except:
            raise BaseException("Failed to parse server response.")
        
        if (responseMap["Type"] == 0):
            print(responseMap)
            return None

        return responseMap["Payload"]

