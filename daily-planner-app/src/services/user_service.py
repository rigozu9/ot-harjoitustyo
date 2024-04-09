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
    
    def is_first_login(self, user_id):
        return self.user_repository.check_first_login(user_id)
    
    def complete_first_login(self, user_id):
        self.user_repository.complete_first_login_process(user_id)

    def add_info(self, age, sex, sleep, user_id):
        try:
            age = int(age)
            if age < 15 or age > 120:
                raise ValueError("Age must be between 15 and 120.")
            sleep = int(sleep)
            if sleep < 1 or sleep > 16:
                raise ValueError("Sleep must be between 1 and 16 hours.")
        except ValueError as e:
            raise

        self.user_repository.create_info(age, sex, sleep, user_id)

    def show_info(self, user_id):
        return self.user_repository.get_info(user_id)