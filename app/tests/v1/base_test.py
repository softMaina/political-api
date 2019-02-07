import unittest

from app import create_app
from instance.config import config



class TestBaseClass(unittest.TestCase):
    """ Base test class """

    def setUp(self):
        # create and setup the application for testing
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.app_test_client = self.app.test_client()
        self.app.testing = True

        self.PARTY = {
            'id':1,
            'name':'Jubilee',
            'hqaddress':'Tuko Pamoja',
            'logoUrl':'www.youtube.com'
        }

        
    def tearDown(self):
        # destroy application that is created for testing
        self.app_context.pop()
    
    
if __name__ == '__main__':
    unittest.main() 