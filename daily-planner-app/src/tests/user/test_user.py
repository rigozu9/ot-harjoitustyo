# Tests for user functions.
# pylint: disable=all
import os
# Turn testing enviroment on when running this
os.environ["TEST_ENV"] = "True"
import unittest
from entities.dailyplan import DailyPlan
from entities.user import User
from services.user_service import UserService
from repositories.user_repository import UserRepository
from database_connection import get_database_session, Base, engine


class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.session = get_database_session()
        cls.create_tables()

    @classmethod
    def create_tables(cls):
        Base.metadata.create_all(bind=engine)

    @classmethod
    def tearDownClass(cls):
        cls.session.close()
        engine.dispose()
        # Optionally drop all tables after tests
        Base.metadata.drop_all(bind=engine)
        os.environ["TEST_ENV"] = "False"

    def setUp(self):
        self.session.query(User).delete()
        self.session.query(DailyPlan).delete()
        self.session.commit()
        self.user_repository = UserRepository(self.session)
        self.user_service = UserService(self.user_repository)

    # Test that a user can be registered
    def test_user_registration(self):
        self.assertEqual(self.user_service.register_user(
            "testuser", "password"), "success")

        # Verify the user exists in the database
        user_id = self.user_repository.find_id_by_username("testuser")
        self.assertIsNotNone(
            user_id, "Registered user should have a valid ID.")

    # Too short password test
    def test_password_short_registration(self):
        self.assertEqual(self.user_service.register_user(
            "testuser", "123"), "password_short")

    # Test that cant register with existing username
    def test_for_existing_user_registration(self):
        # Register a user for the first time
        self.user_service.register_user("existinguser", "password")

        # Attempt to register the same username again
        result = self.user_service.register_user("existinguser", "password")
        self.assertEqual(result, "username_exists")

    # Test that a registered user can log in
    def test_user_login(self):
        self.user_service.register_user("loginuser", "password")
        self.assertTrue(self.user_service.login_user(
            "loginuser", "password"), "User should be able to log in with correct credentials.")

        # Test login with incorrect password
        self.assertFalse(self.user_service.login_user("loginuser", "wrongpassword"),
                         "User should not be able to log in with incorrect password.")

    # Test finding non-existent user
    def test_find_nonexistent_user(self):
        user_id = self.user_repository.find_id_by_username("nonexistentuser")
        self.assertIsNone(user_id, "Non-existent user should not have an ID.")

    # test for finding the username by id
    def test_get_username_by_user(self):
        self.user_service.register_user("testuser", "password")

        user_id = self.user_repository.find_id_by_username("testuser")
        self.assertIsNotNone(
            user_id, "User ID should not be None after registration.")

        retrieved_username = self.user_service.get_username(user_id)
        self.assertEqual(retrieved_username, "testuser",
                         "The retrieved username should match the registered username.")

    # test checking for a users first login status
    def test_is_first_login(self):
        self.user_service.register_user("testuser", "password")
        user_id = self.user_repository.find_id_by_username("testuser")
        self.assertTrue(self.user_service.is_first_login(
            user_id), "New user should be first login")

        self.user_service.complete_first_login(user_id)
        self.assertFalse(self.user_service.is_first_login(
            user_id), "Should be False after completing first login")

    # test completing the first login process
    def test_complete_first_login(self):
        self.user_service.register_user("testuser", "password")
        user_id = self.user_repository.find_id_by_username("testuser")
        self.user_service.complete_first_login(user_id)

        user = self.session.query(User).filter_by(id=user_id).one()
        self.assertTrue(user.first_login_completed,
                        "First login should be marked as completed")

    # test for info addiung with valid and invalid data
    def test_add_info(self):
        """Tests for adding user information with valid and invalid data."""
        self.user_service.register_user("testuser", "password")
        user_id = self.user_repository.find_id_by_username("testuser")

        valid_user_info = {
            "age": 25,
            "sex": "Male",
            "total_sleep_minutes": 480,
            "total_exercise_minutes": 60,
            "total_outside_minutes": 120,
            "total_productive_minutes": 480,
            "total_screen_minutes": 420,
            "user_id": user_id
        }

        try:
            self.user_service.add_info(valid_user_info)
        except ValueError:
            self.fail("add_info raised ValueError unexpectedly with valid inputs")

        # if age 0
        invalid_user_info = valid_user_info.copy()
        invalid_user_info['age'] = 0
        with self.assertRaises(ValueError):
            self.user_service.add_info(invalid_user_info)

        # if age 150
        invalid_user_info['age'] = 150
        with self.assertRaises(ValueError):
            self.user_service.add_info(invalid_user_info)

    # test for showing users info

    def test_show_info(self):
        """Test for showing users info after adding it."""
        self.user_service.register_user("testuser", "password")
        user_id = self.user_repository.find_id_by_username("testuser")

        user_info = {
            "age": 25,
            "sex": "Male",
            "total_sleep_minutes": 480,
            "total_exercise_minutes": 60,
            "total_outside_minutes": 120,
            "total_productive_minutes": 480,
            "total_screen_minutes": 420,
            "user_id": user_id
        }
        self.user_service.add_info(user_info)

        info = self.user_service.show_info(user_id)
        expected_info = {
            'age': 25,
            'sex': 'Male',
            'sleep_goal': 480,
            'exercise_goal': 60,
            'outside_goal': 120,
            'productive_goal': 480,
            'screen_goal': 420
        }
        self.assertEqual(info, expected_info,
                         "User info should match the added info")

    def test_get_advice(self):
        """Test for getting advice based on user data."""
        self.user_service.register_user("testuser", "password")
        user_id = self.user_repository.find_id_by_username("testuser")

        user_info = {
            "age": 25,
            "sex": "Male",
            "total_sleep_minutes": 480,
            "total_exercise_minutes": 60,
            "total_outside_minutes": 120,
            "total_productive_minutes": 480,
            "total_screen_minutes": 420,
            "user_id": user_id
        }
        self.user_service.add_info(user_info)

        goals = {'sleep_goal': 480, 'exercise_goal': 60}
        averages = {'avg_sleep': 450, 'avg_exercise': 20} 

        goal_advice, avg_advice = self.user_service.get_advice(goals, averages)

        expected_goal_advice = "Your sleep habits are good."
        expected_avg_advice = "Aim for at least 30 minutes of exercise daily to stay active. " \
                              "Learn more: https://www.cdc.gov/physicalactivity/basics/adults/index.htm " \
                              "https://health.clevelandclinic.org/benefits-of-exercise-other-than-weight-loss " \
                              "https://www.healthdirect.gov.au/exercise-and-mental-health"

        self.assertEqual(goal_advice['sleep_advice'], expected_goal_advice)
        self.assertEqual(avg_advice['exercise_advice'], expected_avg_advice)

if __name__ == "__main__":
    unittest.main()
