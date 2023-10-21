import json
import requests
from langaracpscsdk.Exec import Exec
from langaracpscsdk.ExecImage import ExecImage, ExecImageManager
from langaracpscsdk.Request import JsonRequest, RequestMethod

class ExecProfile:
    def __init__(self, studentid: int, imageId: str, description: str):
        self.StudentID: int = studentid
        self.ImageID: str = imageId
        self.Description: str = description

    def ToDict(self):
        return dict({ "studentid": self.StudentID, "imageid": self.ImageID, "description": self.Description })

    def ToJson(self):
        return json.dumps(self.ToMap())

class ExecProfileManager:
    def __init__(self, baseURL: str, imageURL: str, apikey: str):
        self.BaseURL = baseURL
        self.APIKey: str = apikey
        self.ImageManager: ExecImageManager = ExecImageManager(imageURL, self.APIKey)

    def UploadProfile(self, execProfile: ExecProfile) -> dict:
        req = JsonRequest(RequestMethod.Post, f"{self.BaseURL}/Create", dict({"apikey": self.APIKey}), execProfile.ToDict())

        response: requests.Response = req.Send()# requests.post(f"{self.BaseURL}/Create", headers=dict({"apikey": self.APIKey, "Content-Type": "application/json"}, json=json.dumps(execProfile.ToDict())))

        if (not(response.ok)):
            print(f"Profile creation failed for {execProfile.StudentID}. Reason: {response.reason}. content: {response.content}")
            return None

        responseMap = response.json()

        if (responseMap["Type"] == 0):
            print(responseMap)
            return None

        return response.json()["Payload"]

    def CreateProfile(self, studentid: str, imagePath: str, description: str) -> dict:
        imageResponse: requests.Response = JsonRequest(RequestMethod.Get, f"{self.ImageManager.BaseURL}/{studentid}", dict({"apikey": self.APIKey})).Send() #.json()

        if (not(imageResponse.ok)):
            print(f"Image request failed because {imageResponse.reason}")
            return None
        
        image: str = None
        imageResponse = imageResponse.json()

        if (imageResponse["Type"] == 0):
            image = self.ImageManager.CreateImage(self.ImageManager.LoadImageFromFile(studentid, imagePath))["ID"]

            if (image == None):
                print(f"Failed to create image for {studentid}")
                return image
            else:
                print(f"Created image for {studentid}")
        else:
            print(imageResponse)
            
            image = imageResponse["Payload"]["ID"]

        return self.UploadProfile(ExecProfile(studentid, image, description))

    
    def GetProfile(self, studentid: int) -> dict:
        response: requests.Response = JsonRequest(RequestMethod.Get, f"{self.BaseURL}/{studentid}", dict({"apikey": self.APIKey})).Send()

        if (not(response.ok)):
            print(f"Failed to fetch profile. Reason: {response.reason} -> {response.content}")
            return None

        return response.json()

    def GetActiveProfiles(self) -> dict:
        response: requests.Response = JsonRequest(RequestMethod.Get, f"{self.BaseURL}/Active", dict({"apikey": self.APIKey})).Send()

        if (not(response.ok)):
            print(f"Failed to fetch active profiles. Reason: {response.reason} -> {response.content}")
            return None

        return response.json()["Payload"]