import unittest
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):

    def setUp(self):
         self.new_user=User("Eddy","Chase")


