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


    def test_init(self):
        '''
        Test to check if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name, 'John')
        self.assertEqual(self.new_user.last_name, 'Nyamweya')
        self.assertEqual(self.new_user.username, 'nyamzy')
        self.assertEqual(self.new_user.email, 'john@gmail.com')
        self.assertEqual(self.new_user.password, '1234')


if __name__ == '__main__':
    unittest.main()
    