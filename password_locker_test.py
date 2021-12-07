import unittest
from passworsd_locker import User,Credentials

class TestUser(unittest.TestCase):
    '''
    Subclass for testing the user class behaviours
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

    def test_delete_user(self):
        '''
        Test to check if we can remove a user from users list
        '''
        self.new_user.save_user()
        test_user = User('Test', 'User', 'user', 'test@gmail.com', '1234')
        test_user.save_user()
        self.new_user.delete_user() #Deletes a user object
        self.assertEqual(len(User.users),1)

    def test_find_user_by_username(self):
        '''
        Test to check if we can find a user by username and display their information
        '''
        self.new_user.save_user()
        test_user = User('Test', 'User', 'user', 'test@gmail.com', '2134')
        test_user.save_user()
        found_user = User.find_by_username('user')
        self.assertEqual(found_user.username, test_user.username)

    def test_user_exists(self):
        '''
        Test to check if a user exists
        '''
        self.new_user.save_user()
        test_user = User('Test', 'User', "user", 'test@gmail.com', '1234')
        test_user.save_user()
        user_exists = User.user_exist('user')

        self.assertTrue(user_exists)


    def test_display_all_users(self):
        '''
        Test that returns a list of all contacts saved
        '''
        self.assertEqual(User.display_users(),User.users)




class TestCredentials(unittest.TestCase):
    '''
    Test subclass for testing the behaviours of the credentials class
    '''
    def setUp(self):
        '''
        Set up method that runs before each test case
        '''
        self.new_credential = Credentials('nyamzy', 'twitter', '1234')

    def tearDown(self):
        '''
        TearDown method that cleans up after each test has run
        '''
        Credentials.accounts = []

    def test_init(self):
        '''
        Test to check if objects are initialized properly
        '''
        self.assertEqual(self.new_credential.username, "nyamzy")
        self.assertEqual(self.new_credential.application, 'twitter')
        self.assertEqual(self.new_credential.password, '1234')

    def test_save_credential(self):
        '''
        Test to check if the credential is saved in the accounts list
        '''
        self.new_credential.save_credential() #Save credentials method
        self.assertEqual(len(Credentials.accounts),1)

    def test_save_multiple_credentials(self):
        '''
        Test to check if we can save multiple credentials
        '''
        self.new_credential.save_credential()
        test_credential = Credentials('test', 'instagram', 'testy123')
        test_credential.save_credential()

        self.assertEqual(len(Credentials.accounts),2)
    
    def test_delete_credential(self):
        '''
        Test to check if we can delete a credential account
        '''
        self.new_credential.save_credential()
        test_credential = Credentials('testy', 'instagram', 'testing123')
        test_credential.save_credential()

        self.new_credential.delete_credential() #Delete credential method
        self.assertEqual(len(Credentials.accounts),1)

    def test_display_credentials(self):
        '''
        Test to check if we can display the credential accounts
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.accounts)

    def test_credential_exists(self):
        '''
        Test to check if a credential exists by returning a boolean
        '''
        self.new_credential.save_credential()
        test_credential = Credentials('testy', 'instagram', 'testing213')
        test_credential.save_credential()

        credential_exists = Credentials.credential_exist('testy')
        self.assertTrue(credential_exists)
        

if __name__ == '__main__':
    unittest.main()
