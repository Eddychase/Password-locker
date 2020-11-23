from user import User
from credentials import Credentials

def Create_user(name,password):
    new_user=User(name,password)
    return new_user

def save_users(user):
    user.save_user()