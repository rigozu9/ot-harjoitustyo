"""Activity entity class import"""
from entities.dailyplan import DailyPlan


class DailyPlanRepository:
    """Dailyplan repository for database actions"""

    def __init__(self, session):
        self._session = session

    def add_plans(self, activity_dict):
        """adding plans to database using a dictionary"""
        plan = DailyPlan()

        plan.user_id = activity_dict['user_id']
        plan.date = activity_dict['date']
        plan.sleep = activity_dict['total_sleep_minutes']
        plan.outside_time = activity_dict['total_outside_minutes']
        plan.productive_time = activity_dict['total_productive_minutes']
        plan.exercise = activity_dict['total_exercise_minutes']
        plan.screen_time = activity_dict['total_screen_minutes']
        plan.other_activities = activity_dict['other']

        self._session.add(plan)
        self._session.commit()

    def get_plan_from_db(self, user_id, date):
        """Gets a user's plan from the database for a specific date.

        Returns:
            object: DailyPlan object
        """
        daily_plan = self._session.query(DailyPlan).filter(DailyPlan.user_id == user_id,
                                                           DailyPlan.date == date).one_or_none()
        return daily_plan

    def get_all_plans_for_user_db(self, user_id):
        """Retrieve all daily plans for a specific user_id.

        Returns:
            object: all DailyPlan objects from user
        """
        daily_plans = self._session.query(DailyPlan).filter(DailyPlan.user_id == user_id).all()
        return daily_plans

    def delete_plan(self, plan_id):
        """Deletes a specific plan based on plan_id."""
        plan_to_delete = self._session.query(DailyPlan).filter(
            DailyPlan.id == plan_id).one_or_none()
        if plan_to_delete:
            self._session.delete(plan_to_delete)
            self._session.commit()



    def compare_day_to_goal_from_db(self, plan_id, goals):
        """Comparing a days plan to goals

        Returns:
            dict: dictionary that contains the compared activites
        """
        plan_to_compare = self._session.query(DailyPlan).filter(
            DailyPlan.id == plan_id).one_or_none()
        compared_stats = {}

        sleep_compare = plan_to_compare.sleep - goals['sleep_goal']
        outside_compare = plan_to_compare.outside_time - goals['outside_goal']
        productive_compare = plan_to_compare.productive_time - goals['productive_goal']
        exercise_compare = plan_to_compare.exercise - goals['exercise_goal']
        screen_time_compare = plan_to_compare.screen_time - goals['screen_goal']
        compared_stats = {'sleep_compare': sleep_compare,
                          'exercise_compare': exercise_compare, 
                          'outside_compare': outside_compare, 
                          'productive_compare': productive_compare, 
                          'screen_time_compare': screen_time_compare}

        return compared_stats

    def compare_total_days_to_goal_from_db(self, total_plans, goals):
        """Comparing total days plan to goals

        Returns:
            dict: dictionary that contains the compared activites
        """
        plan_to_compare = total_plans
        compared_stats = {}

        sleep_compare = plan_to_compare['avg_sleep'] - goals['sleep_goal']
        outside_compare = plan_to_compare['avg_outside_time']  - goals['outside_goal']
        productive_compare = plan_to_compare['avg_productive_time']  - goals['productive_goal']
        exercise_compare = plan_to_compare['avg_exercise']  - goals['exercise_goal']
        screen_time_compare = plan_to_compare['avg_screen_time']  - goals['screen_goal']
        compared_stats = {'sleep_compare': sleep_compare,
                          'exercise_compare': exercise_compare, 
                          'outside_compare': outside_compare, 
                          'productive_compare': productive_compare, 
                          'screen_time_compare': screen_time_compare}

        return compared_stats
