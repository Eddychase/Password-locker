from user import User
from credentials import Credentials

def Create_user(name,password):
    new_user=User(name,password)
    return new_user

def save_users(user):
    user.save_user()

def check_existing_users(name):
    return User.user_exists(name)

def user_log_in(name, password):
     log_in = User.log_in(name, password)
     if log_in != False:
        return User.log_in(name, password)

def display_users():
     return User.display_user()

def create_credentials(user_password, name, password):
    new_credential = Credentials(user_password,name,password)
    return new_credential

def save_credentials(credential):
    Credentials.save_credentials()

def display_credentials(password):
     return Credentials.display_credentials(password)


def create_generated_password(name):
     password = Credentials.generate_password()
     return password


def main():
     print("Welcome to Password Locker.A place to store all your passwords")
     print('\n')

     while True:
         print('''Use these short codes :
         CC:- create a Password Locker account \n
         DC:- display names of current Password Locker users \n
         LG:- log into your Password Locker account \n
         EX:- exit the Password Locker account''')

         short_code = input().lower()
         if short_code == 'CC':
              print("\n")
              print("New Password Locker Account")
              print("-"*10)
              print("User name ...")
              user_name = input()
              print("Password ...")
              user_password = input()
              save_users(Create_user(user_name, user_password))
              print("\n")
              print(f"{user_name} welcome to Password Locker")
              print("\n")

         elif short_code == 'DC':
             if display_users():
                print("\n")
                print("These are the current users of Password Locker")
                print("-"*10)

                for user in display_users():
                    print(f"{user.user_name}")
                    print("-"*10)

             else:
                print("\n")
                print("Password Locker seems to have no current user.\n    Be the first! :")
                print("\n")

         elif short_code == 'LG':
             print("\n")
             print("Log into your Password Locker Account")
             print("Enter your user name")
             user_name = input()
             print("Enter the password")
             user_password = input()

             if user_log_in(user_name,user_password) == None:
                print("\n")
                print("Please try again")
                print("\n")

             else:
                user_log_in(user_name,user_password)
                print("\n")
                print(f'''{user_name} These are your Credentials\n
                Use these short codes to get around''')

                while True:
                    print('''  Short codes:
                    ac - add a credential \n
                    dc - display credentials \n
                    gp - create a credential with a generated password \n
                    ex - exit Credentials''')


                    short_code = input().lower()
                    if short_code == 'ac':
                         print("\n")
                         print("New Credential")
                         print("-"*10)
                         print("Name of the credential ...")
                         credential_name = input()
                         print("Password of the credential ...")
                         credential_password = input()

                         save_credentials(create_credentials(user_password, credential_name, credential_password))
                         print("\n")
                         print(f"Credentials for {credential_name} have been created and saved")
                         print("\n")

                    elif short_code == 'dc':
                        if display_credentials(user_password):
                            print("\n")
                            print(f"{user_name}\'s credentials")
                            print("-"*10)
                            for credential in display_credentials(user_password):
                                print(f"Account ..... {Credentials.credential_name}")
                                print(f"Password .... {Credentials.credential_password}")
                                print("-"*10)

                        else:
                            print("\n")
                            print("You have no credentials")
                            print("\n")

                    elif short_code == 'gp':
                         print("\n")
                         print("New Credential")
                         print("-"*10)
                         print("Name of the credential ...")
                         credential_name = input()
                         save_credentials(Credentials(user_password, credential_name,(create_generated_password(credential_name))))
                         print("\n")
                         print(f"Credentials for {credential_name} have been created and saved")
                         print("\n")

                    elif short_code == 'ex':
                        print(f"See you later {user_name}")
                        print("\n")
                        break

                    else:
                        print("\n")
                        print(f'''{short_code} is not recognized.
                        Please use the short codes''')
                        print("\n")

         elif short_code == 'ex':
             print("\n")
             print("Bye .....")
             break

         else:
            print("\n")
            print(f'''Sorry we did not understand you.What is {short_code}?
            Please use the short codes''')
            print("\n")

if __name__ == '__main__':
    main()




                        




              

              


    