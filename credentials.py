import random
import string

class Credentials:
    credentials_list=[]
    user_credentials_list=[]

    def __init__(self,first_name,last_name,password):
        self.first_name=first_name
        self.last_name=last_name
        self.password=password

    def save_credentials(self):
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        Credentials.credentials_list.remove(self)

    @classmethod
    def generate_password(cls,size):
        scope=string.ascii_letters + string.digits
        '''
        Takes random choices from ascii_letters and digits
        '''
        generate_password = ''.join([random.choice(scope) 
                             for n in range(size)]) 

        return generate_password

   