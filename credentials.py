import random

class Credentials:
    credentials_list=[]

    def __init__(self,first_name,last_name,password):
        self.first_name=first_name
        self.last_name=last_name
        self.password=password

    def save_credentials(self):
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        Credentials.credentials_list.remove(self)

