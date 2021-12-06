class User:
    '''
    Class that generates new instances of users
    '''
    users = [] #Empty list that will store users

    def __init__(self, first_name, last_name, username, email, password):
        '''
        init method helps to define the properties for our objects
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
        

