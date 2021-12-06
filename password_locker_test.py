import unittest

from passworsd_locker import User

class TestUser(unittest.TestCase):
    '''
    Subclass for testing the behavious of the user class behaviours
    '''

    def setUp(self):
        '''
        Set up method that runs before each test case
        '''
        self.new_user = User('John', 'Nyamweya', 'nyamzy', 'john@gmail.com', '1234') #Create new contact object