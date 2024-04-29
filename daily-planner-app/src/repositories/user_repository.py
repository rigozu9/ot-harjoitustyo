"""Activity entity User import and bcrypt for handling logins."""
import bcrypt
from entities.user import User


class UserRepository:
    """User repository for database actions"""

    def __init__(self, session):
        self._session = session

    def find_by_username(self, username):
        """Check for username in the database"""
        return self._session.query(User).filter_by(username=username).first()

    def create_user(self, username, password):
        """Creates a user"""
        hashed_password = bcrypt.hashpw(password.encode(
            'utf-8'), bcrypt.gensalt()).decode('utf-8')
        new_user = User(username=username, password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def verify_user(self, username, password):
        """Logging in verification of username and password."""
        user_record = self.find_by_username(username)
        password_match = user_record and bcrypt.checkpw(
            password.encode('utf-8'), user_record.password.encode('utf-8')
        )
        if password_match:
            return user_record.id
        return False

    def find_id_by_username(self, username):
        """Find an ID belonging to a user"""
        user = self.find_by_username(username)
        return user.id if user else None

    def get_username_by_user(self, user_id):
        """Retrieving user's username"""
        user = self._session.get(User, user_id)
        return user.username if user else None

    def check_first_login(self, user_id):
        """checks if users has logged in before"""
        user = self._session.query(User).filter_by(id=user_id).one_or_none()
        return user is not None and not user.first_login_completed

    def complete_first_login_process(self, user_id):
        """completes users first login"""
        user = self._session.query(User).filter_by(id=user_id).one_or_none()
        if user:
            user.first_login_completed = True
            self._session.commit()

    def create_info(self, user_info):
        """method for creating or updating info for a user"""
        user = self._session.query(User).filter_by(id=user_info['user_id']).one_or_none()
        if user:
            user.age = user_info['age']
            user.sex = user_info['sex']
            user.sleep_goal = user_info['total_sleep_minutes']
            user.exercise_goal = user_info['total_exercise_minutes']
            user.outside_goal = user_info['total_outside_minutes']
            user.productive_goal = user_info['total_productive_minutes']
            user.screen_goal = user_info['total_screen_minutes']
            self._session.commit()

    def get_info(self, user_id):
        """method for getting info from a user"""
        user = self._session.query(User).filter_by(id=user_id).one_or_none()
        return {
            'age': user.age,
            'sex': user.sex,
            'sleep_goal': user.sleep_goal,
            'exercise_goal': user.exercise_goal,
            'outside_goal': user.outside_goal,
            'productive_goal': user.productive_goal,
            'screen_goal': user.screen_goal
        }
