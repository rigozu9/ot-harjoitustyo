class DailyPlanService:
    """Class for daily plan application logic."""

    def __init__(self, dailyplan_repository):
        self._dailyplan_repository = dailyplan_repository

    def create_plans(self, activity_dict):
        """Calls daily plan repository to add new plans using a dictionary"""
        self._dailyplan_repository.add_plans(activity_dict)

    def get_plans_by_id(self, user_id, date):
        """gets users plans from repository"""
        return self._dailyplan_repository.get_plan_from_db(user_id, date)

    def calculate_average_attributes(self, user_id):
        """Calculate averages of all plan attributes for a user."""
        plans = self._dailyplan_repository.get_all_plans_for_user_db(user_id)
        if not plans:
            return None
        totals, count = self.calculate_totals(plans)
        if count == 0:
            return None
        return self.calculate_averages(totals, count)

    def calculate_totals(self, plans):
        """Calculate total values from plans."""
        totals = {'sleep': 0, 'outside_time': 0, 'productive_time': 0, 'exercise': 0,
                  'screen_time': 0}
        count = 0
        for plan in plans:
            for attr in totals:
                value = getattr(plan, attr)
                if value is not None:
                    totals[attr] += value
            count += 1
        return totals, count

    def calculate_averages(self, totals, count):
        """Calculate average values from totals."""
        return {f"avg_{key}": total / count for key, total in totals.items()}


    def remove_plan(self, plan_id):
        """Calculate average values from totals."""
        self._dailyplan_repository.delete_plan(plan_id)

    def count_user_plans(self, user_id):
        """Returns the count of all daily plans for a specific user."""
        plans = self._dailyplan_repository.get_all_plans_for_user_db(user_id)
        return len(plans) if plans else 0

    def compare_day_to_goal(self, plan_id, goals):
        """Comparing a days plan to goals"""
        return self._dailyplan_repository.compare_day_to_goal_from_db(plan_id, goals)

    def compare_total_days_to_goal(self, total_plans, goals):
        """Comparing a days plan to goals"""
        return self._dailyplan_repository.compare_total_days_to_goal_from_db(total_plans, goals)
