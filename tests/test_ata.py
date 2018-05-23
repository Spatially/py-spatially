import unittest
import ata
import api

class ATATest(unittest.TestCase):

	def setUp(self):
		applicationCode = "504f4a12-5877-11e8-9026-0242ac110005"
		applicationKey = "504f49fa-5877-11e8-9026-0242ac110005"
		token = api.GetToken(applicationCode, applicationKey)
		self.token = token

	def test_new_ata(self):
		# print("Testing NewATA call")
		locationWKT = "POINT(-71.064156780428 42.35862883483673)"
		resp = ata.NewATA(self.token,locationWKT)
		self.assertIsNotNone(resp)
		# print("Test ATA response:", resp)
