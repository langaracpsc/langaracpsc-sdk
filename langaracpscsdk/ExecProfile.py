import json
import requests
from langaracpscsdk.Exec import Exec
from langaracpscsdk.ExecImage import ExecImage, ExecImageManager
from langaracpscsdk.Request import JsonRequest, RequestMethod

class ExecProfile:
    """Stores Exec profile info.
    """
    def __init__(self, studentid: int, imageId: str, description: str):
        """Constructor

        Args:
            studentid (int): Student id.
            imageId (str): ID of the image uploaded for the exec
            description (str): Exec description. 
        """
        self.StudentID: int = studentid
        self.ImageID: str = imageId
        self.Description: str = description

    def ToDict(self):
        """Generates a dict from the current object

        Returns:
            dict: Generated dict.  
        """
        return dict({ "studentid": self.StudentID, "imageid": self.ImageID, "description": self.Description })

    def ToJson(self):
        """Converts the current object to json.

        Returns:
            str: Generated json
        """
        return json.dumps(self.ToDict())

class ExecProfileManager:
    """Routines for managing exec profiles.
    """
    def __init__(self, baseURL: str, imageURL: str, apikey: str):
        """Constructor

        Args:
            baseURL (str): API base URL 
            imageURL (str): Image API base URL
            apikey (str): API key
        """
        self.BaseURL = baseURL
        self.APIKey: str = apikey
        self.ImageManager: ExecImageManager = ExecImageManager(imageURL, self.APIKey)

    def UploadProfile(self, execProfile: ExecProfile) -> dict:
        """Uploaded the given profile to the backend

        Args:
            execProfile (ExecProfile): Profile to upload 

        Returns:
            dict: Uploaded profile.  
        """
        req = JsonRequest(RequestMethod.Post, f"{self.BaseURL}/Create", dict({"apikey": self.APIKey}), execProfile.ToDict())

        response: requests.Response = req.Send()

        if (not(response.ok)):
            print(f"Profile creation failed for {execProfile.StudentID}. Reason: {response.reason}. content: {response.content}")
            return None

        responseMap = response.json()

        if (responseMap["Type"] == 0):
            print(responseMap)
            return None

        return response.json()["Payload"]

    def UpdateProfile(self, profileMap: dict[str, str]):
        """Updates the given exec profile on the backend

        Args:
            profileMap (dict): Profile to update

        Returns:
            dict: Changed profile as a confirmation.
        """
        if ("image" in profileMap.keys()):
            imageResult = self.ImageManager.CreateImage(self.ImageManager.LoadImageFromFile(profileMap["id"], profileMap["image"]))
            print(imageResult)

        profileMap.pop("image")

        response: requests.Response = JsonRequest(RequestMethod.Post, f"{self.BaseURL}/Update", dict({"apikey": self.APIKey}), profileMap).Send()

        print(response.url)

        if (not(response.ok)):
            print(response.reason)
            return None

        responseMap = response.json()

        if (responseMap["Type"] <= 0):
            print(responseMap)
            return None

        return response.json()["Payload"]

    def CreateProfile(self, studentid: str, imagePath: str, description: str) -> dict:
        """Creates a profile with the given info.

        Args:
            studentid (str): Student id.
            imagePath (str): Image  
            description (str): Exec description.

        Returns:
            dict: Created profile.
        """

        imageResponse: requests.Response = JsonRequest(RequestMethod.Get, f"{self.ImageManager.BaseURL}/{studentid}", dict({"apikey": self.APIKey})).Send() 

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
        """Fetches the ExecProfiles with the given student id.

        Args:
            studentid (int): ID of the profile to fetch.

        Returns:
            dict: Fetched profile.
        """
        response: requests.Response = JsonRequest(RequestMethod.Get, f"{self.BaseURL}/{studentid}", dict({"apikey": self.APIKey})).Send()

        if (not(response.ok)):
            print(f"Failed to fetch profile. Reason: {response.reason} -> {response.content}")
            return None

        return response.json()

    def GetActiveProfiles(self) -> dict:
        """Fetches the ExecProfiles of active Execs.

        Returns:
            dict: Fetched profiles.
        """
        response: requests.Response = JsonRequest(RequestMethod.Get, f"{self.BaseURL}/Active", dict({"apikey": self.APIKey})).Send()

        if (not(response.ok)):
            print(f"Failed to fetch active profiles. Reason: {response.reason} -> {response.content}")
            return None

        return response.json()["Payload"]
