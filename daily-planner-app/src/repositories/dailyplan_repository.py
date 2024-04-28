"""Activity entity class import"""
from entities.dailyplan import DailyPlan


class DailyPlanRepository:
    """Dailyplan repository for database actions"""

    def __init__(self, session):
        self._session = session

    def add_plans(self,
                  user_id,
                  date,
                  sleep,
                  outsidetime,
                  productivetime,
                  exercisetime,
                  screentime,
                  other
                  ):
        """adding plans to database"""
        plan = DailyPlan()

        plan.user_id = user_id
        plan.date = date
        plan.sleep = sleep
        plan.outside_time = outsidetime
        plan.productive_time = productivetime
        plan.exercise = exercisetime
        plan.screen_time = screentime
        plan.other_activities = other

        self._session.add(plan)
        self._session.commit()

    def get_plan_from_db(self, user_id, date):
        """Gets a user's plan from the database for a specific date."""
        daily_plan = self._session.query(DailyPlan).filter(DailyPlan.user_id == user_id,
                                                           DailyPlan.date == date).one_or_none()
        return daily_plan

    def get_all_plans_for_user_db(self, user_id):
        """Retrieve all daily plans for a specific user_id."""
        daily_plans = self._session.query(DailyPlan).filter(DailyPlan.user_id == user_id).all()
        return daily_plans
    
    def delete_plan(self, plan_id):
        """Deletes a specific plan based on plan_id."""
        plan_to_delete = self._session.query(DailyPlan).filter(DailyPlan.id == plan_id).one_or_none()
        if plan_to_delete:
            self._session.delete(plan_to_delete)
            self._session.commit()
