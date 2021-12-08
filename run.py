#!/usr/bin/env python3
from passworsd_locker import User, Credentials

#User functions
def create_user(fname, lname, uname, email, password):
    '''
    Function that creates a new user
    '''
    new_user = User(fname, lname, uname, email, password)
    return new_user

def save_users(user):
    '''
    Function that saves a new user
    '''
    user.save_user()

def del_user(user):
    '''
    Function that deletes a user
    '''
    user.delete_user()

def find_user(username):
    '''
    Function that finds a user by username
    '''
    return User.find_by_username(username)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def check_existing_users(username):
    '''
    Function that checks if a user is existing and returns a Boolean
    '''
    return User.user_exist(username)


#Credentials functions
def create_credential(uname, application, password):
    '''
    Function that creates a new credential
    '''
    new_credential = Credentials(uname, application, password)
    return new_credential

def save_credentials(credential):
    '''
    Function that saves a new credential
    '''
    credential.save_credential()

def del_credential(credential):
    '''
    Function that deletes a credential account
    '''
    credential.delete_credential()

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def check_existing_credentials(username):
    '''
    Function that checks if a credential exists
    '''
    return Credentials.credential_exist(username)


