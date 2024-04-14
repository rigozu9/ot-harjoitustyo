#pylint: disable=all
"""tests for dailyplan """
import unittest
import os
# Turn testing enviroment on when running this
os.environ["TEST_ENV"] = "True"
from datetime import date, timedelta
from entities.dailyplan import DailyPlan
from entities.user import User
from services.dailyplan_service import DailyPlanService
from services.user_service import UserService
from repositories.dailyplan_repository import DailyPlanRepository
from repositories.user_repository import UserRepository
from database_connection import get_database_session, Base, engine, database_url, init_db

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
        # Optionally drop all tables after tests
        Base.metadata.drop_all(bind=engine)
        os.environ["TEST_ENV"] = "False"

    def setUp(self):
        self.session.query(User).delete()
        self.session.query(DailyPlan).delete()
        self.session.commit()
        self.user_repository = UserRepository(self.session)
        self.daily_plan_repository = DailyPlanRepository(self.session)
        self.user_service = UserService(self.user_repository)
        self.daily_plan_service = DailyPlanService(self.daily_plan_repository)

        user = User(username='testuser', password='testpassword')
        self.session.add(user)
        self.session.commit()

        self.test_user_id = user.id
        self.test_date = date.today()
        self.test_sleep = 7
        self.test_outside_time = 6
        self.test_productive_time = 1
        self.test_exercise_time = 3
        self.test_screen_time = 11
        self.test_other_activities = "Reading"

        self.daily_plan_service.create_plans(
            self.test_user_id,
            self.test_date,
            self.test_sleep,
            self.test_outside_time,
            self.test_productive_time,
            self.test_exercise_time,
            self.test_screen_time,
            self.test_other_activities
        )
        
    def test_create_plans(self):
        """Test creating daily plans"""
        plan = self.session.query(DailyPlan).filter_by(user_id=self.test_user_id).one_or_none()
        self.assertIsNotNone(plan, "See if plan in db")
        self.assertEqual(plan.date, self.test_date, "date equal.")
        self.assertEqual(plan.sleep, self.test_sleep, "Sleep equal.")
        self.assertEqual(plan.outside_time, self.test_outside_time, "Outsidetime equal")
        self.assertEqual(plan.productive_time, self.test_productive_time, "Productive time equal")
        self.assertEqual(plan.exercise, self.test_exercise_time, "Exercise time equal.")
        self.assertEqual(plan.screen_time, self.test_screen_time, "screentime equal")
        self.assertEqual(plan.other_activities, self.test_other_activities, "other activites equal")


    def test_get_plans_by_id(self):
        """Test retrieving daily plans"""
        plan = self.daily_plan_service.get_plans_by_id(self.test_user_id, self.test_date)
        self.assertIsNotNone(plan, "See if plan in db")
        self.assertEqual(plan.date, self.test_date, "date equal.")
        self.assertEqual(plan.sleep, self.test_sleep, "Sleep equal.")
        self.assertEqual(plan.outside_time, self.test_outside_time, "Outsidetime equal")
        self.assertEqual(plan.productive_time, self.test_productive_time, "Productive time equal")
        self.assertEqual(plan.exercise, self.test_exercise_time, "Exercise time equal.")
        self.assertEqual(plan.screen_time, self.test_screen_time, "screentime equal")
        self.assertEqual(plan.other_activities, self.test_other_activities, "other activites equal")

    def test_get_plans_by_id_no_plan(self):
        """Test retrieving daily plans when no plan exists"""
        no_plan_date = self.test_date - timedelta(days=1)
        plan = self.daily_plan_service.get_plans_by_id(self.test_user_id, no_plan_date)
        self.assertIsNone(plan, "None for wrong date")

if __name__ == "__main__":
    unittest.main()
