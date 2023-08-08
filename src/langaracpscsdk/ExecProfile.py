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
        imageResponse: dict = self.ImageManager.CreateImage(self.ImageManager.LoadImageFromFile(studentid, imagePath))

        if (imageResponse == None):
            print(f"Failed to create image for {studentid}")
            return imageResponse

        return self.UploadProfile(ExecProfile(studentid, imageResponse["ID"], description))
