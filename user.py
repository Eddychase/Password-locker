from credentials import Credentials
class User:
    user_list=[]

    def __init__(self,user_name,user_password):
        self.user_name=user_name
        self.user_password=user_password

    def save_password(self):
        User.user_list.append(self)

    @classmethod
    def display_user(self):
        return cls.user_list

