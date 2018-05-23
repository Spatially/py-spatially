from config import SpatiallyAPI
import requests
import ast

timeOfDayValues = ("AllDay", "Morning", "MidDay", "Evening", "Night")
locationValues = ("Home", "Work", "HomeAndWork")


def NewATA(token,locationWKT,timeOfDay="AllDay", locationType="Home", geoFence=False):
	if timeOfDay not in timeOfDayValues:
		raise ValueError("Value provided for timeOfDay invalid:", timeOfDay, "Must be one of the following:", timeOfDayValues)
	if locationType not in locationValues:
		raise ValueError("Value provided for locationType invalid:", locationType, "Must be one of the following:", locationValues)
	data = {
		"pointWKT": locationWKT,
		"areaType": "ATA",
		"buffer": 100,
		"distance": 0,
		"timeOfDay": timeOfDay,
	}
	if locationType == "Home":
		data["locationType"] = ["Home"]
	if locationType == "Work":
		data["locationType"] = ["Work"]
	if locationType == "HomeAndWork":
		data["locationType"] = ["Home", "Work"]
	headers = {"Authorization": "Bearer {}".format(token)}
	resp = requests.post(SpatiallyAPI+"/ads/science/ata", data=data, headers=headers)
	print("response:",resp.text)
	print("Request data:", data)
	return ast.literal_eval(resp.text)
