import json

from flask import current_app

from . import base_test

class TestParties(base_test.TestBaseClass):
    # class contains tests for party endpoints

    
    def test_get_parties(self):
        response = self.app_test_client.get('/api/v1/party',json=self.PARTY)

        self.assertEqual(response.status_code,200)
        
    def test_add_new_party(self):

        response = self.app_test_client.post('/api/v1/party/add',json=self.PARTY)

        self.assertEqual(response.status_code, 201)
        

    def test_edit_party(self):
        
        response1 = self.app_test_client.post('/api/v1/party/add',json=self.PARTY)

        response = self.app_test_client.put('/api/v1/party/update/1',json=self.PARTY)

        self.assertEqual(response.status_code, 200)

    
    def test_unexisting_office_endpoint(self):

        """ Test when unexisting url is provided """
        response = self.app_test_client.get('api/v1/party/remove')

        self.assertEqual(response.status_code, 404)

    def test_get_specific_party(self):
        """ Test endpoint to return only one office """
        addParty = self.app_test_client.post('/api/v1/party/add',json=self.PARTY)

        response = self.app_test_client.get('/api/v1/party/getparty/1',json=self.PARTY)

        self.assertEqual(response.status_code,200)


    def test_party_with_int_name(self):
        """Test endpoint to ensure it doesnt accept integer for name """
        response = self.app_test_client.post('/api/v1/party/add',json=self.wrong_party_name)

        self.assertEqual(response.status_code, 400)
    def test_update_party_with_wrong_url(self):

        response = self.app_test_client.put('/api/v1/party/update/k',json=self.PARTY)

        self.assertEqual(response.status_code, 404)