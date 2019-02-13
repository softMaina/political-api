""" office tests """
import json

from flask import current_app

from . import base_test
from . import helper_functions

class TestOffices(base_test.TestBaseClass):


    def test_get_offices(self):
        response = self.app_test_client.get('/api/v1/office',json=self.OFFICE)

        self.assertEqual(response.status_code,200)
        self.assertEqual(helper_functions.convert_response_to_json(response)["data"][0]['name'], self.OFFICE['name'])
        self.assertEqual(helper_functions.convert_response_to_json(response)["data"][0]['office_type'], self.OFFICE['office_type'])
        
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

    def test_get_specific_office(self):
        """ Test endpoint to return only one office """
        addOffice = self.app_test_client.post('/api/v1/office/add',json=self.OFFICE)

        response = self.app_test_client.get('/api/v1/office/getoffice/1',json=self.OFFICE)

        self.assertEqual(response.status_code,200)

    def test_office_with_int_name(self):
        """Test endpoint to ensure it doesnt accept integer for name """
        response = self.app_test_client.post('/api/v1/office/add',json=self.wrong_office_name)

        self.assertEqual(response.status_code, 400)

    def test_office_with_int_office_type(self):
        """Test endpoint to ensure it doesnt accept integer for office type"""
        response = self.app_test_client.post('/api/v1/office/add',json=self.wrong_office_type)

        self.assertEqual(response.status_code, 400)


    def test_office_with_invalid_Keys(self):
        """test adding office with an invalid key"""
        response = self.app_test_client.post('/api/v1/office/add',json=self.invalid_keys)

        self.assertEqual(response.status_code,400)