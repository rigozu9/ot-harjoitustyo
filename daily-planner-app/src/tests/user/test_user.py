#Tests for user functions. 

import os
#Turn testing enviroment on when running this 
os.environ["TEST_ENV"] = "True"
import unittest
from database_connection import get_database_session, Base, engine, database_url, init_db
from repositories.user_repository import UserRepository
from repositories.activity_repository import ActivityRepository
from services.user_service import UserService
from services.daily_planner_service import DailyPlannerService
from entities.user import User
from entities.activity import Activity

class TestApp(unittest.TestCase):
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
        Base.metadata.drop_all(bind=engine)  # Optionally drop all tables after tests
        os.environ["TEST_ENV"] = "False"

    def setUp(self):
        self.session.query(User).delete()
        self.session.query(Activity).delete()
        self.session.commit()
        self.user_repository = UserRepository(self.session)
        self.activity_repository = ActivityRepository(self.session)
        self.user_service = UserService(self.user_repository)
        self.daily_planner_service = DailyPlannerService(self.activity_repository)
    # Test that a user can be registered
    def test_user_registration(self):        
        self.assertEqual(self.user_service.register_user("testuser", "password"), "success")
        
        # Verify the user exists in the database
        user_id = self.user_repository.find_id_by_username("testuser")
        self.assertIsNotNone(user_id, "Registered user should have a valid ID.")
    
    # Too short password test
    def test_password_short_registration(self):      
        self.assertEqual(self.user_service.register_user("testuser", "123"), "password_short")
        
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
        self.assertTrue(self.user_service.login_user("loginuser", "password"), "User should be able to log in with correct credentials.")
        
        # Test login with incorrect password
        self.assertFalse(self.user_service.login_user("loginuser", "wrongpassword"), "User should not be able to log in with incorrect password.")
        
    # Test finding non-existent user
    def test_find_nonexistent_user(self):
        user_id = self.user_repository.find_id_by_username("nonexistentuser")
        self.assertIsNone(user_id, "Non-existent user should not have an ID.")
    
    #test for finding the username by id
    def test_get_username_by_user(self):
        self.user_service.register_user("testuser", "password")

        user_id = self.user_repository.find_id_by_username("testuser")
        self.assertIsNotNone(user_id, "User ID should not be None after registration.")

        retrieved_username = self.user_service.get_username(user_id)
        self.assertEqual(retrieved_username, "testuser", "The retrieved username should match the registered username.")

if __name__ == "__main__":
    unittest.main()
