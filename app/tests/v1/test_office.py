""" office tests """
import json

from flask import current_app

from . import base_test

class TestOffices(base_test.TestBaseClass):


    def test_get_offices(self):
        response = self.app_test_client.get('/api/v1/office',json=self.OFFICE)

        self.assertEqual(response.status_code,200)
        
    def test_add_new_office(self):

        response = self.app_test_client.post('/api/v1/office/add',json=self.OFFICE)

        self.assertEqual(response.status_code, 201)

    
    def test_unexisting_office_endpoint(self):

        """ Test when unexisting url is provided """
        response = self.app_test_client.get('api/v1/office/remove')

        self.assertEqual(response.status_code, 404)

    def test_update_office(self):
        """ Test updating already existing office """
        response1 = self.app_test_client.post('/api/v1/office/add',json=self.OFFICE)

        response = self.app_test_client.put('/api/v1/office/update/1',json=self.OFFICE)

        self.assertEqual(response.status_code, 200)
