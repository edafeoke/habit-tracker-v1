"""
A module containing all user controllers (funtions that processes user data)
"""

from models.user import User

def get_user(user_id):
    pass

def create_user(username, password):
    user = User(username, password)
    user.save()

def update_user(user_id, username, password):
    user = User(username, password)
    user.update(user_id, username, password)

def all_users():
    pass

def delete_user(user_id):
    pass