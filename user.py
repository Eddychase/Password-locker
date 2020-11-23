from credentials import Credentials
class User:
    user_list=[]

    def __init__(self,user_name,user_password):
        self.user_name=user_name
        self.user_password=user_password

    def save_password(self):
        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        return cls.user_list

    @classmethod
    def find_credentials(cls,name):
        for credentials in Credentials.credentials_list:
            if credentials.credentials_name==name:
                return True
            else:
                return False

    @classmethod
    def log_in(cls,name,password):
        for user in cls.user_list:
            if user.user_name==name and password:
                return Credentials.credentials_list
            else:
                return False

    @classmethod
    def user_exists(cls,name):
        for user in cls.user_list:
            if user.user_name==name:
                return True
            else:
                return False

    


