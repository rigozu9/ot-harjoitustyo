"""Activity entity User import and bcrypt for handling logins."""
import bcrypt
from entities.user import User


class UserRepository:
    """User repository for database actions"""

    def __init__(self, session):
        self._session = session
        self._good_goals = {
            'sleep': 420,
            'exercise': 30,
            'outside': 20,
            'productive': 456,
            'screen': 360
        }
        self._advice_urls = {
            'sleep': "https://www.sleepfoundation.org/how-sleep-works/" +
                    "how-much-sleep-do-we-really-need",
            'exercise': "https://www.cdc.gov/physicalactivity/basics/adults/index.htm",
            'outside': "https://www.menshealth.com/fitness/a36547849/" +
                        "how-much-time-should-i-spend-outside/",
            'productive': "https://www.atlassian.com/blog/productivity/" +
                            "this-is-how-many-hours-you-should-really-be-working",
            'screen': [
                "https://www.reidhealth.org/blog/screen-time-for-adults",
                "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5574844/"
            ]
        }

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
        """Get advice based on your goals or averages."""
        goal_improvements = self._evaluate_metrics(goals, "goal") if goals else {}
        average_improvements = self._evaluate_metrics(averages, "avg") if averages else {}
        return goal_improvements, average_improvements

    def _evaluate_metrics(self, metrics, fix):
        """Evaluate metrics against good goals and generate advice."""
        improvements = {}
        for key, value in metrics.items():
            if fix == "avg":
                if key.startswith(fix):
                    category = key.split('_')[1]
                    good_value = self._good_goals[category]
                    advice_key = f"{category}_advice"
                    is_good = value <= good_value if category == 'screen' else value >= good_value
                    improvements[advice_key] = self._generate_advice(category, is_good)
            if fix == "goal":
                if key.endswith(fix):
                    category = key[:-len(fix)-1]
                    good_value = self._good_goals[category]
                    advice_key = f"{category}_advice"
                    is_good = value <= good_value if category == 'screen' else value >= good_value
                    improvements[advice_key] = self._generate_advice(category, is_good)
        return improvements

    def _generate_advice(self, category, is_good):
        """Generate advice based on the category and whether the current value is good."""
        if is_good:
            return f"Your {category} habits are good."

        advice_messages = {
            'sleep': "Try to get at least 7 hours of sleep to maintain optimal health.",
            'exercise': "Aim for at least 30 minutes of exercise daily to stay active.",
            'outside': "Spending at least 20 minutes outside daily can " +
                        "greatly benefit your well-being.",
            'productive': "Aim to have around 7-8 hours of productive time each day.",
            'screen': "Consider reducing your screen time to improve your overall health."
        }

        urls = self._advice_urls[category]
        url_text = ' '.join(urls) if isinstance(urls, list) else urls
        return f"{advice_messages[category]} Learn more: {url_text}"
