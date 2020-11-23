import unittest
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):

    def setUp(self):
         self.new_user=User("Eddy","Chase97")

    def tearDown(self):
        User.user_list=[]

    def test__init(self):
        self.assertEqual(self.new_user.user_name,"Eddy")
        self.assertEqual(self.new_user.user_password,"Chase97")
    
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
if __name__=='__main__':
    unittest.main()



