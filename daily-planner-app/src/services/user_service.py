from repositories.user_repository import UserRepository
from database_connection import get_database_connection

#Class for users application logic

class UserService:
    def __init__(self):
        #initializing database for UserRepository
        self.user_repository = UserRepository(get_database_connection())

    def register_user(self, username, password):
        if self.user_repository.find_by_username(username):
            return False
        self.user_repository.create_user(username, password)
        return True

    def login_user(self, username, password):
        return self.user_repository.verify_user(username, password)
