# pylint: disable=all
"""tests for dailyplan """
import os
# Turn testing enviroment on when running this
os.environ["TEST_ENV"] = "True"
from database_connection import get_database_session, Base, engine
from repositories.user_repository import UserRepository
from repositories.dailyplan_repository import DailyPlanRepository
from services.user_service import UserService
from services.dailyplan_service import DailyPlanService
from entities.user import User
from entities.dailyplan import DailyPlan
from datetime import date, timedelta
import unittest


class TestDailyPlan(unittest.TestCase):
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
        self.test_sleep = 420
        self.test_outside_time = 360
        self.test_productive_time = 60
        self.test_exercise_time = 180
        self.test_screen_time = 480
        self.test_other_activities = "Reading"

        test_plan = {
            "user_id": self.test_user_id,
            "date": self.test_date,
            "total_sleep_minutes": self.test_sleep,
            "total_outside_minutes": self.test_outside_time,
            "total_productive_minutes": self.test_productive_time,
            "total_exercise_minutes": self.test_exercise_time,
            "total_screen_minutes": self.test_screen_time,
            "other": self.test_other_activities
        }

        self.daily_plan_service.create_plans(test_plan)

        test_plan_2 = {
            "user_id": self.test_user_id,
            "date": self.test_date - timedelta(days=1),
            "total_sleep_minutes": self.test_sleep + 60,
            "total_outside_minutes": self.test_outside_time + 60,
            "total_productive_minutes": self.test_productive_time + 60,
            "total_exercise_minutes": self.test_exercise_time + 60,
            "total_screen_minutes": self.test_screen_time + 60,
            "other": self.test_other_activities
        }
        self.daily_plan_service.create_plans(test_plan_2)

    def test_create_plans(self):
        """Test creating daily plans"""
        plan = self.session.query(DailyPlan).filter_by(user_id=self.test_user_id).first()

        self.assertIsNotNone(plan, "See if plan in db")
        self.assertEqual(plan.date, self.test_date, "date equal.")
        self.assertEqual(plan.sleep, self.test_sleep, "Sleep equal.")
        self.assertEqual(plan.outside_time,
                         self.test_outside_time, "Outsidetime equal")
        self.assertEqual(plan.productive_time,
                         self.test_productive_time, "Productive time equal")
        self.assertEqual(plan.exercise, self.test_exercise_time,
                         "Exercise time equal.")
        self.assertEqual(plan.screen_time,
                         self.test_screen_time, "screentime equal")
        self.assertEqual(plan.other_activities,
                         self.test_other_activities, "other activites equal")


    def test_get_plans_by_id(self):
        """Test retrieving daily plans"""
        plan = self.daily_plan_service.get_plans_by_id(
            self.test_user_id, self.test_date)
        self.assertIsNotNone(plan, "See if plan in db")
        self.assertEqual(plan.date, self.test_date, "date equal.")
        self.assertEqual(plan.sleep, self.test_sleep, "Sleep equal.")
        self.assertEqual(plan.outside_time,
                         self.test_outside_time, "Outsidetime equal")
        self.assertEqual(plan.productive_time,
                         self.test_productive_time, "Productive time equal")
        self.assertEqual(plan.exercise, self.test_exercise_time,
                         "Exercise time equal.")
        self.assertEqual(plan.screen_time,
                         self.test_screen_time, "screentime equal")
        self.assertEqual(plan.other_activities,
                         self.test_other_activities, "other activites equal")

    def test_get_plans_by_id_no_plan(self):
        """Test retrieving daily plans when no plan exists"""
        no_plan_date = self.test_date + timedelta(days=1)
        plan = self.daily_plan_service.get_plans_by_id(
            self.test_user_id, no_plan_date)
        self.assertIsNone(plan, "None for wrong date")

    def test_averages(self):
        """Test for getting the average dailyplan activities"""
        result = self.daily_plan_service.calculate_average_attributes(self.test_user_id)
        expected_result = {
            'avg_sleep': 450,
            'avg_outside_time': 390,
            'avg_productive_time': 90,
            'avg_exercise': 210,
            'avg_screen_time': 510
        }
        self.assertAlmostEqual(result['avg_sleep'], expected_result['avg_sleep'])
        self.assertAlmostEqual(result['avg_outside_time'], expected_result['avg_outside_time'])
        self.assertAlmostEqual(result['avg_productive_time'], expected_result['avg_productive_time'])
        self.assertAlmostEqual(result['avg_exercise'], expected_result['avg_exercise'], places=2)
        self.assertAlmostEqual(result['avg_screen_time'], expected_result['avg_screen_time'], places=2)

    def test_averages_no_date(self):
        """Test for if there are no plans"""
        plan = self.daily_plan_service.calculate_average_attributes(self.test_user_id+1)
        self.assertIsNone(plan, "None for wrong date")    

if __name__ == "__main__":
    unittest.main()
