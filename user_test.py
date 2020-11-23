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

    def test_save_multiple_users(self):
        self.new_user.save_user()
        test_user=User("Cory","Ills97")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_display_user(self):
        self.assertEqual(User.display_user(),User.user_list)

    def test_find_credentials(self):
        self.new_user.save_user()
        test_user=User("Cory","Ills97")
        test_user.save_user()
        found_credentials=User.find_credentials("Ills97")
        self.assertEqual(found_credentials, True)

    def test_user_exists(self):
        self.new_user.save_user()
        test_user=User("Cory","Ills97")
        test_user.save_user()
        user_exists=User.user_exists("Cory")
        self.assertTrue(user_exists)

        

    def test_log_in(self):
        self.new_user.save_user()
        test_user=User("Cory","Ills97")
        test_user.save_user()
        found_credentials=User.log_in("Cory","Ills97")
        self.assertEqual(found_credentials,Credentials.credentials_list)
        
   
        

if __name__=='__main__':
    unittest.main()



