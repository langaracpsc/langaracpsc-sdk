<a id="Util.base64"></a>

## base64

<a id="Util.Util"></a>

## Util Objects

```python
class Util()
```

<a id="Util.Util.TrimBase64"></a>

#### TrimBase64

```python
@staticmethod
def TrimBase64(b64str: str)
```

<a id="Util.Util.GetBase64String"></a>

#### GetBase64String

```python
@staticmethod
def GetBase64String(obj) -> str
```

<a id="Util.Util.GetBase64StringBytes"></a>

#### GetBase64StringBytes

```python
@staticmethod
def GetBase64StringBytes(obj: bytearray) -> str
```

<a id="Exec.os"></a>

## os

<a id="Exec.json"></a>

## json

<a id="Exec.requests"></a>

## requests

<a id="Exec.JsonRequest"></a>

## JsonRequest

<a id="Exec.RequestMethod"></a>

## RequestMethod

<a id="Exec.IntEnum"></a>

## IntEnum

<a id="Exec.ExecPosition"></a>

## ExecPosition Objects

```python
class ExecPosition(IntEnum)
```

<a id="Exec.ExecPosition.President"></a>

#### President

<a id="Exec.ExecPosition.VicePresident"></a>

#### VicePresident

<a id="Exec.ExecPosition.TechLead"></a>

#### TechLead

<a id="Exec.ExecPosition.GeneralRep"></a>

#### GeneralRep

<a id="Exec.ExecPosition.PublicRelations"></a>

#### PublicRelations

<a id="Exec.ExecPosition.Finance"></a>

#### Finance

<a id="Exec.ExecPosition.Events"></a>

#### Events

<a id="Exec.Exec"></a>

## Exec Objects

```python
class Exec()
```

Stores info about an Exec

<a id="Exec.Exec.__init__"></a>

#### \_\_init\_\_

```python
def __init__(studentid: int, firstname: str, lastname: str,
             position: ExecPosition, email: str)
```

Contstructor

Args:
    studentid (int): Exec's student ID
    firstname (str): Exec's  First name
    lastname (str): Exec's Last name
    position (ExecPosition): Exec's position
    email (str): Exec's email

<a id="Exec.Exec.ToDict"></a>

#### ToDict

```python
def ToDict() -> dict
```

Generates a dictionary from the current object

Returns:
    dict: Generated dictionary

<a id="Exec.Exec.ToJson"></a>

#### ToJson

```python
def ToJson() -> str
```

Converts the current object to json.

Returns:
    str: Generated json

<a id="Exec.ExecManager"></a>

## ExecManager Objects

```python
class ExecManager()
```

Routines for managing Exec objects.

<a id="Exec.ExecManager.__init__"></a>

#### \_\_init\_\_

```python
def __init__(baseurl: str, apikey: str)
```

Constructor

Args:
    baseurl (str): API base url
    apikey (str): API Key

<a id="Exec.ExecManager.FromJson"></a>

#### FromJson

```python
@staticmethod
def FromJson(jsonStr: str) -> Exec
```

Generates an Exec from json.

Args:
    jsonStr (str): Json to convert.

Returns:
    Exec: Generated Exec.

<a id="Exec.ExecManager.CreateExec"></a>

#### CreateExec

```python
def CreateExec(_exec: Exec) -> dict
```

Args:
    _exec (Exec): Adds the given Exec to the database 

Returns:
    dict: Created Exec dict as a confirmation.

<a id="Exec.ExecManager.CreateExecDict"></a>

#### CreateExecDict

```python
def CreateExecDict(_exec: dict) -> dict
```

Args:
    _exec (Exec): Adds the given Exec dict to the database 

Returns:
    dict: Created Exec dict as a confirmation.

<a id="Exec.ExecManager.EndTenure"></a>

#### EndTenure

```python
def EndTenure(studentid: int) -> bool
```

Ends the tenure for the Exec with the given student ID.

Args:
    studentid (int): Student ID for the exec. 

Returns:
    bool: Execution status.

<a id="Exec.ExecManager.ListAll"></a>

#### ListAll

```python
def ListAll() -> list[dict]
```

Fetches and lists all the Execs in the db

Returns:
    list[dict]: Fetched execs.

<a id="Exec.ExecManager.UpdateExec"></a>

#### UpdateExec

```python
def UpdateExec(execMap: dict) -> dict
```

Updates the given exec info on the database.

Args:
    execMap (dict): Exec info to update

Returns:
    dict: Changed exec as a confirmation.

<a id="Request.json"></a>

## json

<a id="Request.requests"></a>

## requests

<a id="Request.IntEnum"></a>

## IntEnum

<a id="Request.RequestMethod"></a>

## RequestMethod Objects

```python
class RequestMethod(IntEnum)
```

<a id="Request.RequestMethod.Get"></a>

#### Get

<a id="Request.RequestMethod.Post"></a>

#### Post

<a id="Request.RequestMethod.Put"></a>

#### Put

<a id="Request.MethodStrings"></a>

#### MethodStrings

<a id="Request.JsonRequest"></a>

## JsonRequest Objects

```python
class JsonRequest()
```

Http request with a json body

<a id="Request.JsonRequest.__init__"></a>

#### \_\_init\_\_

```python
def __init__(method: RequestMethod,
             url: str,
             headers: dict = dict(),
             payload: dict = dict())
```

Constructor

Args:
    method (RequestMethod): HTTP method
    url (str): URL
    headers (dict, optional): Request headers. Defaults to dict().
    payload (dict, optional): Request body/payload. Defaults to dict().

<a id="Request.JsonRequest.Send"></a>

#### Send

```python
def Send() -> requests.Response
```

Sends the request.

Returns:
    requests.Response: Returned response.

<a id="Request.JsonRequest.ToDict"></a>

#### ToDict

```python
def ToDict() -> dict
```

Generates a dict from the current object

Returns:
    dict: Generated dict.

<a id="ExecImage.os"></a>

## os

<a id="ExecImage.json"></a>

## json

<a id="ExecImage.requests"></a>

## requests

<a id="ExecImage.JsonRequest"></a>

## JsonRequest

<a id="ExecImage.RequestMethod"></a>

## RequestMethod

<a id="ExecImage.MethodStrings"></a>

## MethodStrings

<a id="ExecImage.Util"></a>

## Util

<a id="ExecImage.ExecImage"></a>

## ExecImage Objects

```python
class ExecImage()
```

Stores an image in base64 with metadata

<a id="ExecImage.ExecImage.__init__"></a>

#### \_\_init\_\_

```python
def __init__(studentid: int, name: str, imageBuffer: str)
```

<a id="ExecImage.ExecImage.ToDict"></a>

#### ToDict

```python
def ToDict() -> dict
```

<a id="ExecImage.ExecImage.ToJson"></a>

#### ToJson

```python
def ToJson() -> str
```

<a id="ExecImage.ImageRequest"></a>

## ImageRequest Objects

```python
class ImageRequest(JsonRequest)
```

Http request for ExecImage

<a id="ExecImage.ImageRequest.__init__"></a>

#### \_\_init\_\_

```python
def __init__(url: str, apikey: str, image: ExecImage)
```

Constructor

Args:
    url (str): URL
    apikey (str): API key
    image (ExecImage): Payload image.

<a id="ExecImage.ExecImageManager"></a>

## ExecImageManager Objects

```python
class ExecImageManager()
```

Routines for managing ExecImage objects.

<a id="ExecImage.ExecImageManager.__init__"></a>

#### \_\_init\_\_

```python
def __init__(baseURL: str, apikey: str)
```

Constructor

Args:
    baseURL (str): Base API URL
    apikey (str): API key

<a id="ExecImage.ExecImageManager.LoadImageFromFile"></a>

#### LoadImageFromFile

```python
def LoadImageFromFile(studentid: int, imagePath: str) -> ExecImage
```

Loads an image from the given file, and creates an ExecImage of it.

Args:
    studentid (int): Student id of the exec.
    imagePath (str): Path to the image.

Returns:
    ExecImage: Constructed image.

<a id="ExecImage.ExecImageManager.CreateImage"></a>

#### CreateImage

```python
def CreateImage(image: ExecImage) -> dict
```

Adds the given image to the database

Args:
    image (ExecImage): Image to add.

Raises:
    BaseException: In case of server response failure.

Returns:
    dict: Created image.

<a id="ExecProfile.json"></a>

## json

<a id="ExecProfile.requests"></a>

## requests

<a id="ExecProfile.Exec"></a>

## Exec

<a id="ExecProfile.ExecImage"></a>

## ExecImage

<a id="ExecProfile.ExecImageManager"></a>

## ExecImageManager

<a id="ExecProfile.JsonRequest"></a>

## JsonRequest

<a id="ExecProfile.RequestMethod"></a>

## RequestMethod

<a id="ExecProfile.ExecProfile"></a>

## ExecProfile Objects

```python
class ExecProfile()
```

Stores Exec profile info.

<a id="ExecProfile.ExecProfile.__init__"></a>

#### \_\_init\_\_

```python
def __init__(studentid: int, imageId: str, description: str)
```

Constructor

Args:
    studentid (int): Student id.
    imageId (str): ID of the image uploaded for the exec
    description (str): Exec description.

<a id="ExecProfile.ExecProfile.ToDict"></a>

#### ToDict

```python
def ToDict()
```

Generates a dict from the current object

Returns:
    dict: Generated dict.

<a id="ExecProfile.ExecProfile.ToJson"></a>

#### ToJson

```python
def ToJson()
```

Converts the current object to json.

Returns:
    str: Generated json

<a id="ExecProfile.ExecProfileManager"></a>

## ExecProfileManager Objects

```python
class ExecProfileManager()
```

Routines for managing exec profiles.

<a id="ExecProfile.ExecProfileManager.__init__"></a>

#### \_\_init\_\_

```python
def __init__(baseURL: str, imageURL: str, apikey: str)
```

Constructor

Args:
    baseURL (str): API base URL 
    imageURL (str): Image API base URL
    apikey (str): API key

<a id="ExecProfile.ExecProfileManager.UploadProfile"></a>

#### UploadProfile

```python
def UploadProfile(execProfile: ExecProfile) -> dict
```

Uploaded the given profile to the backend

Args:
    execProfile (ExecProfile): Profile to upload 

Returns:
    dict: Uploaded profile.

<a id="ExecProfile.ExecProfileManager.CreateProfile"></a>

#### CreateProfile

```python
def CreateProfile(studentid: str, imagePath: str, description: str) -> dict
```

Creates a profile with the given info.

Args:
    studentid (str): Student id.
    imagePath (str): Image  
    description (str): Exec description.

Returns:
    dict: Created profile.

<a id="ExecProfile.ExecProfileManager.GetProfile"></a>

#### GetProfile

```python
def GetProfile(studentid: int) -> dict
```

Fetches the ExecProfiles with the given student id.

Args:
    studentid (int): ID of the profile to fetch.

Returns:
    dict: Fetched profile.

<a id="ExecProfile.ExecProfileManager.GetActiveProfiles"></a>

#### GetActiveProfiles

```python
def GetActiveProfiles() -> dict
```

Fetches the ExecProfiles of active Execs.

Returns:
    dict: Fetched profiles.


