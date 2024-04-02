#Class for users application logic
#Now receives the repository when app starting or testing

class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository
        

    def register_user(self, username, password):
        if self.user_repository.find_by_username(username):
            return "username_exists"
        if len(password) < 4:
            return "password_short"
        self.user_repository.create_user(username, password)
        return "success"

    def login_user(self, username, password):
        return self.user_repository.verify_user(username, password)
    
    def get_username(self, user_id):
        return self.user_repository.get_username_by_user(user_id)
