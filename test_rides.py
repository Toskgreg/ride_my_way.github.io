# test_rides.py
import unittest
import os
import json
from app import create_app


class RidesTestCase(unittest.TestCase):
    """This class represents the ride test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.ride = {'Start Address': 'Mutungo','Destination':'Kamwokya'}
        
        

       

    def test_ride_offer(self):
        """Test API can create a ride (POST request)"""
        res = self.client().post('api/v1/ride/', data=self.ride)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Mutungo', str(res.data))
        self.assertIn('Kamwokya', str(res.data))

    def test_api_view_all_ride_offers(self):
        """Test API can get a ride (GET request)."""
        res = self.client().post('/api/v1/ride/', data=self.ride)
        self.assertEqual(res.status_code, 201)
        
        self.assertIn('Mutungoo', str(res.data))
        self.assertIn('Kamwokya', str(res.data))

    def test_api_view_ride_offer_by_id(self):
        """Test API can get a single ride by using it's id."""
        rv = self.client().post('/api/v1/ride/', data=self.ride)
        self.assertEqual(rv.status_code, 201)
        result_in_json = json.loads(rv.data.decode('utf-8').replace("'", "\""))
        result = self.client().get(
            '/api/v1/ride/{}'.format(result_in_json['id']))
        self.assertEqual(result.status_code, 200)
        self.assertIn('mutungo', str(result.data))
        

    def test_rides_can_be_edited(self):
        """Test API can edit an existing ride. (PUT request)"""
        rv = self.client().post(
            '/api/v1/ride/',
            data={'Start Address': 'Mutungo',
                   'Destination':'Kamwokya'})
        self.assertEqual(rv.status_code, 201)
        rv = self.client().put(
            '/api/v1/ride/1',
            data={
                'Start Address': 'mutungo',
                'Destination':'Ntinda'
            })
        self.assertEqual(rv.status_code, 200)
        results = self.client().get('/api/v1/ride/1')
        self.assertIn('mutungo', str(results.data))
        self.assertIn('mutungo', str(results.data))

    def test_rides_deletion(self):
        """Test API can delete an existing ride. (DELETE request)."""
        rv = self.client().post(
            '/api/v1/ride/',
            data={'Start Address': 'Mutungo',
                   'Destination':'Kamwokya'})
        self.assertEqual(rv.status_code, 201)
        res = self.client().delete('/api/v1/ride/1')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client().get('/api/v1/ride/1')
        self.assertEqual(result.status_code, 200)

    def tearDown(self):
        """teardown all initialized variables."""
        pass
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()