import json
from . import Exec
from . import ExecImage
from . import Request

class ExecProfile:
    def __init__(self, studentid: int, imageId: str, description: str):
        self.StudentID: int = studentid
        self.ImageID: str = imageId
        self.Description: str = description

    def ToJson(self):
        return json.dumps(dict({ "studentid": self.StudentID, "imageid": self.ImageID, "description": self.Description }))

class ExecProfileManager:
    def __init__(self, baseURL: str, imageURL: str, apikey: str):
        self.BaseURL = baseURL
        self.APIKey: str = apikey
        self.ImageManager: ExecImage.ExecImageManager = ExecImage.ExecImageManager(imageURL, self.APIKey)

    def UploadProfile(self, execProfile: ExecProfile):
        response: requests.Response = Request.Base64Request(Request.RequestMethod.Post, f"{self.BaseURL}/Create", dict({"apikey": self.APIKey}), execProfile.ToJson()).Send()

        if (not(response.ok)):
            print(response.reason)
            return None

        responseMap = response.json()

        if (responseMap["Type"] == 0):
            print(responseMap)
            return None

        return response.json()["Payload"]

    def CreateProfile(self, studentid: str, imagePath: str, description: str) -> dict:
        imageResponse: dict = Request.Base64Request(Request.RequestMethod.Get, f"{self.ImageManager.BaseURL}/{studentid}", dict({"apikey": self.APIKey})).Send().json()

        image: str = None

        if (imageResponse["Type"] == 0):
            image = self.ImageManager.CreateImage(self.ImageManager.LoadImageFromFile(studentid, imagePath))["ID"]

            if (image == None):
                print(f"Failed to create image for {studentid}")
                return image

        image = json.loads(imageResponse["Payload"])["ID"]

        return self.UploadProfile(ExecProfile(studentid, image, description))

    def GetProfile(self, studentid: int):
        response: requests.Response = Request.Base64Request(Request.RequestMethod.Get, f"{self.BaseURL}/{studentid}", dict({"apikey": self.APIKey})).Send()

        if (not(response.ok)):
            print(response.reason)
            return None

        return response.json()

    def GetActiveProfiles(self):
        response: requests.Response = Request.Base64Request(Request.RequestMethod.Get, f"{self.BaseURL}/Active", dict({"apikey": self.APIKey})).Send()

        if (not(response.ok)):
            print(response.reason)
            return None

        return response.json()
