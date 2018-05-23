import unittest
import api

class APITest(unittest.TestCase):
	def test_get_token(self):
		# print("Testing token call")
		applicationCode = "504f4a12-5877-11e8-9026-0242ac110005"
		applicationKey = "504f49fa-5877-11e8-9026-0242ac110005"
		resp = api.GetToken(applicationCode, applicationKey)
		self.assertGreater(len(resp), 0)
		# print("Test API response:", resp)
