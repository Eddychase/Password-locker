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

    def test_save_credentials(self):
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_delete_credentials(self):
        self.new_credentials.save_credentials()
        test_credentials=Credentials("Cory","Wells","Wells98")
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_generate_password(self):
        new_password=self.new_credentials.generate_password()
        self.assertEqual(len(new_password),8)


if __name__=='__main__':
    unittest.main()




    
