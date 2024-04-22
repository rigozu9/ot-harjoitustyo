class UserService:
    """Class for users application logic"""

    def __init__(self, user_repository):
        self.user_repository = user_repository

    def register_user(self, username, password):
        """
            method for user registration.
            checks if username exists or password too short. If they arent returns "success"
        """
        if self.user_repository.find_by_username(username):
            return "username_exists"
        if len(password) < 4:
            return "password_short"
        self.user_repository.create_user(username, password)
        return "success"

    def login_user(self, username, password):
        """calls user repo's verify_user to check if username and password match"""
        return self.user_repository.verify_user(username, password)

    def get_username(self, user_id):
        """get username from user_id"""
        return self.user_repository.get_username_by_user(user_id)

    def is_first_login(self, user_id):
        """check if first login or not"""
        return self.user_repository.check_first_login(user_id)

    def complete_first_login(self, user_id):
        """completes the first login"""
        self.user_repository.complete_first_login_process(user_id)

    def add_info(self, age, sex, sleep_minutes, exercise_minutes, outside_minutes,
                 productive_minutes, screen_minutes, user_id):
        """
        Validates and updates the user's info with new time goals in minutes.
        """
        age = int(age)
        if age < 13 or age > 120:
            raise ValueError("Age must be between 13 and 120.")

        self.user_repository.create_info(
            age, sex, sleep_minutes, exercise_minutes, outside_minutes,
            productive_minutes, screen_minutes, user_id
        )

    def show_info(self, user_id):
        """calls user repo's get_info method for showing users information from user_id"""
        return self.user_repository.get_info(user_id)
