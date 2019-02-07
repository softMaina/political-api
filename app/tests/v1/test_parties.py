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
    
    # add test to test an update of a political party
    # def test_edit_party(self):
    #     party = self.app_test_client.post('/api/v1/party/add',json=self.PARTY)

    #     response = self.app_test_client.put('/api/v1/party/update/1>',json=self.PARTY)

    #     self.assertEqual(response.status_code,200)