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

    accounts = []


    def __init__(self, username, application, password):
        '''
        Initialization method that helps define properties of our credential objects
        '''
        self.username = username
        self.application = application
        self.password = password

    