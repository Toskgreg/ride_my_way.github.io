# test_rides.py
import unittest
import os
import json
from app.views import app
from app.models import rides, Ride


class RidesTestCase(unittest.TestCase):
    """This class represents the ride test case"""

    def test_index(self):
        """ Initial test to ensure flask was setup correctly """
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    def test_returnAll(self):
        """Test method to get all rides """
        returned_result = Ride.returnAll()
        self.assertEqual(returned_result, "No existing Ride offer")

    def test_returnOne(self):
        """Test method to get  a ride by id"""
        returned_result = Ride.returnOne(id)
        self.assertEqual(returned_result, "Ride not Found")

    def test_getride(self):
        """Test method to request a ride  """
        returned_result = Ride.getride(id)
        self.assertEqual(returned_result, "Ride not Found")


if __name__ == "__main__":
    unittest.main()
