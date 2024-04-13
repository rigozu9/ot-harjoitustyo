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
