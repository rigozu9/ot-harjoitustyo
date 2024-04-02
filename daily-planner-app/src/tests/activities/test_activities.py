#Tests for activity functions. 

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
    
    # Test for adding activity
    def test_adding_activity(self):
        self.user_service.register_user("testuser", "password")
        user_id = self.user_repository.find_id_by_username("testuser")

        self.assertTrue(self.daily_planner_service.create_activity("Test Activity", user_id), "Activity should be successfully added.")

        activities = self.daily_planner_service.show_activities(user_id)
        self.assertEqual(len(activities), 1, "There should be exactly one activity.")
        self.assertEqual(activities[0].description, "Test Activity", "The activity description should match the input.")
    
    # Test for removing activity
    def test_deleting_activity(self):
        self.user_service.register_user("testuser", "password")
        user_id = self.user_repository.find_id_by_username("testuser")
        self.assertTrue(self.daily_planner_service.create_activity("Activity to be deleted", user_id), "Activity should be successfully added.")
        
        activities = self.daily_planner_service.show_activities(user_id)
        activity_id = activities[0].id

        self.assertTrue(self.daily_planner_service.remove_activity(activity_id), "Activity should be successfully removed.")

        activities_after_removal = self.daily_planner_service.show_activities(user_id)
        self.assertEqual(len(activities_after_removal), 0, "There should be no activities after removal.")

if __name__ == "__main__":
    unittest.main()