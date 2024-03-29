class User:
    '''
    Class that generates new instances of users
    '''
    users = [] #Empty list that will store users

    def __init__(self, first_name, last_name, username, email, password):
        '''
        init method helps to define the properties for our user objects
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password

    
    def save_user(self):
        '''
        Method that saves the user objects into users list
        '''
        User.users.append(self)

    def delete_user(self):
        '''
        Method that deletes a saved user from the users list
        '''
        User.users.remove(self)

    @classmethod
    def find_by_username(cls,username):
        '''
        Method that takes in a username and returns a user that matches that username
        '''
        for user in cls.users:
            if user.username == username:
                return user

    @classmethod
    def user_exist(cls,username):
        '''
        Method that checks if a user exists from the user list
        '''
        for user in cls.users:
            if user.username == username:
                return True

        return False
    
    @classmethod
    def display_users(cls):
        '''
        Method that returns the users list
        '''
        return cls.users

    

class Credentials:
    '''
    Class that generates new instances of credentials
    '''

    accounts = [] #Empty list that will store credentials


    def __init__(self, username, application, password):
        '''
        Initialization method that helps define properties of our credential objects
        '''
        self.username = username
        self.application = application
        self.password = password

    def save_credential(self):
        '''
        Method that saves the credentials to the accounts list
        '''
        Credentials.accounts.append(self)

    def delete_credential(self):
        '''
        Method that can delete your saved credentials
        '''
        Credentials.accounts.remove(self)

    @classmethod
    def display_credentials(cls):
        '''
        Method that can display credentials in the accounts list
        '''
        return cls.accounts

    @classmethod
    def credential_exist(cls,username):
        '''
        Method that checks if a credential exists by using the username
        '''
        for credential in cls.accounts:
            if credential.username == username:
                return True
        return False




    

    

    

