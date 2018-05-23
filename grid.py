from config import SpatiallyAPI
import requests
import ast

def GetPopulation(token,wktPoint, radius):
	#GET /grid/pop/point?lon=-71.05878365218564&lat=42.355270748343685&radius=150
	lat, lon = __parseWKT(wktPoint)
	headers = {"Authorization": "Bearer {}".format(token)}
	url = "/grid/pop/point?lat={}&lon={}&radius={}".format(lat, lon, radius)
	resp = requests.get(SpatiallyAPI+url, headers=headers)
	return ast.literal_eval(resp.text)

def GetTradeAreaPopulation(token,ata):
	# POST /grid/pop
	headers = {"Authorization": "Bearer {}".format(token)}
	# print("ATA:", type(ata))
	# for key, value in ata.iteritems():
	# 	print(key)
	data = {"featureCollection":ata["featureCollection"]}
	resp = requests.post(SpatiallyAPI+"/grid/pop", json=data, headers=headers)
	return ast.literal_eval(resp.text)

def GetActivity(token,wktPoint, radius):
	# GET grid/stops?wkt=POINT(-71.05878365218564 42.355270748343685)&radius=150
	url = "/grid/stops?wkt={}&radius={}".format(wktPoint, radius)
	headers = {"Authorization": "Bearer {}".format(token)}
	resp = requests.get(SpatiallyAPI+url, headers=headers)
	return ast.literal_eval(resp.text)

def GetDistanceSensitivity(token,wktPoint, radius):
	# GET /grid/distance?lon=-71.05878365218564&lat=42.355270748343685&radius=150
	lat, lon = __parseWKT(wktPoint)
	url = "/grid/distance?lat={}&lon={}&radius={}".format(lat,lon, radius)
	headers = {"Authorization": "Bearer {}".format(token)}
	resp = requests.get(SpatiallyAPI+url, headers=headers)
	return ast.literal_eval(resp.text)

def GetHighlights(token,wktPoint, radius):
	# GET /grid/highlights?lon=-71.05878365218564&lat=42.355270748343685&radius=150
	lat, lon = __parseWKT(wktPoint)
	url = "/grid/highlights?lat={}&lon={}&radius={}".format(lat,lon, radius)
	headers = {"Authorization": "Bearer {}".format(token)}
	resp = requests.get(SpatiallyAPI+url, headers=headers)
	return ast.literal_eval(resp.text)

# input: POINT(-71.064156780428 42.35862883483673)
# output: 42.35862883483673, -71.064156780428
def __parseWKT(wktPoint):
	wktPoint = wktPoint.lower().replace("point","").replace("(","").replace(")","")
	coords = wktPoint.split(" ")
	return coords[1], coords[0]