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

    def tearDown(self):
        '''
        Tear down method that cleans up after each test has run
        '''
        User.users = []

    def test_init(self):
        '''
        Test to check if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name, 'John')
        self.assertEqual(self.new_user.last_name, 'Nyamweya')
        self.assertEqual(self.new_user.username, 'nyamzy')
        self.assertEqual(self.new_user.email, 'john@gmail.com')
        self.assertEqual(self.new_user.password, '1234')


    def test_save_user(self):
        '''
        Test to check if the user object is saved into user list
        '''
        self.new_user.save_user() #saves the new user
        self.assertEqual(len(User.users),1)


    def test_save_multiple_users(self):
        '''
        Test to check if we can save multiple users
        '''
        self.new_user.save_user()
        test_user = User('Test', 'User', 'user', 'test@gmail.com', '1234')
        test_user.save_user()
        self.assertEqual(len(User.users),2)

if __name__ == '__main__':
    unittest.main()
