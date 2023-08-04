import langaracpscsdk
from langaracpscsdk import Exec
from langaracpscsdk import Request

print(Request.Base64Request(Request.RequestMethod.Get, "https://www.gnu.org").Send())
