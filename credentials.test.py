import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_credentials=Credentials("Eddy","Chase","Goog97")

    def test__init(self):
        self.assertEqual(self.new_credentials.first_name,"Eddy")
        self.assertEqual(self.new_credentials.last_name,"Chase")
        self.assertEqual(self.new_credentials.password,"Goog97")

    def tearDown(self):
        Credentials.credentials_list=[]


    
