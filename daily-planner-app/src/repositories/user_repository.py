"""Activity entity User import and bcrypt for handling logins."""
import bcrypt
from entities.user import User


class UserRepository:
    """User repository for database actions"""

    def __init__(self, session):
        self._session = session

    def find_by_username(self, username):
        """Check for username in the database

        Returns:
            object: User object
        """
        return self._session.query(User).filter_by(username=username).first()

    def create_user(self, username, password):
        """Creates a user

        Returns:
            object: User object
        """
        hashed_password = bcrypt.hashpw(password.encode(
            'utf-8'), bcrypt.gensalt()).decode('utf-8')
        new_user = User(username=username, password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def verify_user(self, username, password):
        """Logging in verification of username and password.

        Returns:
            id: user id or False if password doesnt match
        """
        user_record = self.find_by_username(username)
        password_match = user_record and bcrypt.checkpw(
            password.encode('utf-8'), user_record.password.encode('utf-8')
        )
        if password_match:
            return user_record.id
        return False

    def find_id_by_username(self, username):
        """Find an ID belonging to a user

        Returns:
            id: user id or False if username doesnt match
        """
        user = self.find_by_username(username)
        return user.id if user else None

    def get_username_by_user(self, user_id):
        """Retrieving user's username

        Returns:
            username: users username if exists
        """
        user = self._session.get(User, user_id)
        return user.username if user else None

    def check_first_login(self, user_id):
        """checks if users has logged in before

        Returns:
            object: user object if first login completed
        """
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
        user = self._session.query(User).filter_by(
            id=user_info['user_id']).one_or_none()
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
        """method for getting info from a user

        Returns:
            dict: dictionary that contains user info
        """
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

    def get_advice_from_db(self, goals, averages):
        good_goals = {
            'good_sleep': 420,
            'good_exercise': 30,
            'good_outside': 20,
            'good_productive': 456,
            'good_screen': 360
        }

        goal_improvements = {}
        average_improvements = {}

        if goals:
            if goals["sleep_goal"] < good_goals["good_sleep"]:
                goal_improvements["sleep_advice"] = "Sleep more"
            else:
                goal_improvements["sleep_advice"] = "Your sleep habits are good"

            if goals["exercise_goal"] < good_goals["good_exercise"]:
                goal_improvements["exercise_advice"] = "Exercise more"
            else:
                goal_improvements["exercise_advice"] = "Your exercise habits are good"

            if goals["outside_goal"] < good_goals["good_outside"]:
                goal_improvements["outside_advice"] = "Be outside more"
            else:
                goal_improvements["outside_advice"] = "Your outside habits are good"

            if goals["productive_goal"] < good_goals["good_productive"]:
                goal_improvements["productive_advice"] = "Be more productive"
            else:
                goal_improvements["productive_advice"] = "Your productive habits are good"

            if goals["screen_goal"] > good_goals["good_screen"]:
                goal_improvements["screen_time_advice"] = "Have less screentime"
            else:
                goal_improvements["screen_time_advice"] = "Your screentime habits are good"
        
        if averages:
            if averages["avg_sleep"] < good_goals["good_sleep"]:
                average_improvements["sleep_advice"] = "Sleep more"
            else:
                average_improvements["sleep_advice"] = "Your sleep habits are good"

            if averages["avg_exercise"] < good_goals["good_exercise"]:
                average_improvements["exercise_advice"] = "Exercise more"
            else:
                average_improvements["exercise_advice"] = "Your exercise habits are good"

            if averages["avg_outside_time"] < good_goals["good_outside"]:
                average_improvements["outside_advice"] = "Be outside more"
            else:
                average_improvements["outside_advice"] = "Your outside habits are good"

            if averages["avg_productive_time"] < good_goals["good_productive"]:
                average_improvements["productive_advice"] = "Be more productive"
            else:
                average_improvements["productive_advice"] = "Your productive habits are good"

            if averages["avg_screen_time"] > good_goals["good_screen"]:
                average_improvements["screen_time_advice"] = "Have less screentime"
            else:
                average_improvements["screen_time_advice"] = "Your screentime habits are good"

        return goal_improvements, average_improvements
