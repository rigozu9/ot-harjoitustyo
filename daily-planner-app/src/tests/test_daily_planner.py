import os
import unittest
import sqlite3
from database_connection import get_database_connection
from repositories.user_repository import UserRepository
from repositories.activity_repository import ActivityRepository
from services.user_service import UserService
from services.daily_planner_service import DailyPlannerService

class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Test enviroment = true
        os.environ["TEST_ENV"] = "True"

        cls.connection = get_database_connection()
        cls.create_tables()

    @classmethod
    def create_tables(cls):
        # Create tables for test database
        users_sql = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
        """
        activities_sql = """
        CREATE TABLE IF NOT EXISTS activities (
            id INTEGER PRIMARY KEY,
            description TEXT NOT NULL
        );
        """
        cursor = cls.connection.cursor()
        cursor.execute(users_sql)
        cursor.execute(activities_sql)
        cls.connection.commit()

    def setUp(self):
        # Clear the database before each test
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM users")
        cursor.execute("DELETE FROM activities")
        self.connection.commit()

        # Initialize repositories and services
        self.user_repository = UserRepository(self.connection)
        self.activity_repository = ActivityRepository(self.connection)
        self.user_service = UserService()
        self.daily_planner_service = DailyPlannerService()

    # Test that a user can be registered and then logged in
    def test_user_registration_and_login(self):
        self.assertTrue(self.user_service.register_user("testuser", "password"))
        self.assertTrue(self.user_service.login_user("testuser", "password"))
    
    # Ensure an activity can be added (assuming a user is needed for context)
    def test_adding_activity(self):
        self.user_service.register_user("testuser", "password")
        self.assertTrue(self.daily_planner_service.add_activity("Test Activity"))
        activities = self.daily_planner_service.show_activities()
        self.assertEqual(len(activities), 1)
        self.assertEqual(activities[0]['description'], "Test Activity")

    # Clean up the test environment
    @classmethod
    def tearDownClass(cls):
        cls.connection.close()
        test_db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "test_database.sqlite"))
        try:
            os.remove(test_db_path)
        except FileNotFoundError:
            print(f"Test database file not found: {test_db_path}")
        del os.environ["TEST_ENV"]

if __name__ == "__main__":
    unittest.main()
