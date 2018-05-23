import unittest
import grid
import api

class GridTest(unittest.TestCase):

	def setUp(self):
		applicationCode = "504f4a12-5877-11e8-9026-0242ac110005"
		applicationKey = "504f49fa-5877-11e8-9026-0242ac110005"
		token = api.GetToken(applicationCode, applicationKey)
		self.token = token

	def test_get_population(self):
		locationWKT = "POINT(-71.064156780428 42.35862883483673)"
		resp = grid.GetPopulation(self.token, locationWKT, 100)
		self.assertIsNotNone(resp)
		# print("Test grid response population:", resp)

	# def test_get_area_population(self):
	# 	locationWKT = "POINT(-71.064156780428 42.35862883483673)"
	# 	resp = grid.GetTradeAreaPopulation(locationWKT, 100)
	# 	print("Test grid response:", resp)

	def test_get_Activity(self):
		locationWKT = "POINT(-71.064156780428 42.35862883483673)"
		resp = grid.GetActivity(self.token, locationWKT, 100)
		self.assertIsNotNone(resp)
		# print("Test grid response activity:", resp)

	def test_get_distance_sensitivity(self):
		locationWKT = "POINT(-71.064156780428 42.35862883483673)"
		resp = grid.GetDistanceSensitivity(self.token, locationWKT, 100)
		self.assertIsNotNone(resp)
		# print("Test grid response distance:", resp)

	def test_get_highlights(self):
		locationWKT = "POINT(-71.064156780428 42.35862883483673)"
		resp = grid.GetHighlights(self.token, locationWKT, 100)
		self.assertIsNotNone(resp)
		# print("Test grid response highlights:", resp)