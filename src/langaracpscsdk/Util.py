import base64

class Util:
    def TrimBase64(b64str: str):
        return b64str[2: -1]

    def GetBase64String(obj) -> str:
        return str(base64.b64encode(str(obj).encode("utf-8")))[2:-1]
