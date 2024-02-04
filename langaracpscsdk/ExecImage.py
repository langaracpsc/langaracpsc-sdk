import os
import json
import requests
from langaracpscsdk.Request import JsonRequest, RequestMethod, MethodStrings
from langaracpscsdk.Util import Util

class ExecImage:
    """Stores an image in base64 with metadata
    """
    def __init__(self, studentid: int, name: str, imageBuffer: str):
        self.StudentID: int = studentid
        self.Name: str = name
        self.ImageBuffer: str = imageBuffer

    def ToDict(self) -> dict:
        return json.dumps(dict({"id": self.StudentID, "path": self.Name, "buffer": self.ImageBuffer }))

    def ToJson(self) -> str:
        return json.dumps(self.ToDict()) 


class ImageRequest(JsonRequest):
    """Http request for ExecImage
    """
    def __init__(self, url: str, apikey: str, image: ExecImage):
        """Constructor

        Args:
            url (str): URL
            apikey (str): API key
            image (ExecImage): Payload image.
        """
        super().__init__(RequestMethod.Put, url, {"apikey": apikey})

        self.Image: ExecImage = image
        
        self.Payload = self.Image.ToDict()
        
        self.RequestSession = requests.Session()
        self.mRequest = requests.Request(MethodStrings[int(self.Method)], self.URL, data=self.Payload, headers=self.Headers).prepare()


class ExecImageManager:
    """Routines for managing ExecImage objects.
    """
    def __init__(self, baseURL: str, apikey: str):
        """Constructor

        Args:
            baseURL (str): Base API URL
            apikey (str): API key
        """
        self.BaseURL: str = baseURL
        self.APIKey: str = apikey

    def LoadImageFromFile(self, studentid: int, imagePath: str) -> ExecImage:
        """Loads an image from the given file, and creates an ExecImage of it.

        Args:
            studentid (int): Student id of the exec.
            imagePath (str): Path to the image.

        Returns:
            ExecImage: Constructed image.
        """
        if (not(os.path.exists(imagePath))):
            print(f"File {imagePath} doesn't exist.")
            return None

        execImage: ExecImage = None

        with open(imagePath, "rb") as fp:
            execImage = ExecImage(studentid, imagePath, Util.GetBase64StringBytes(fp.read()))

        return execImage

    def CreateImage(self, image: ExecImage) -> dict:
        """Adds the given image to the database

        Args:
            image (ExecImage): Image to add.

        Raises:
            BaseException: In case of server response failure.

        Returns:
            dict: Created image. 
        """
        response: requests.Response = ImageRequest(f"{self.BaseURL}/Create", self.APIKey, image).Send()

        if (not(response.ok)):
            print(f"Failed to create image for {image.StudentID}. Reason: {response.reason} -> {response.content}")
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
