import requests
from config import SpatiallyAPI
import ast

def GetToken(apiCode, apiKey):
	data = {
		"code": apiCode,
		"key": apiKey
	}
	resp = requests.post(SpatiallyAPI+"/gateway/client", json=data)
	respObj = ast.literal_eval(resp.text)
	return respObj["token"]
