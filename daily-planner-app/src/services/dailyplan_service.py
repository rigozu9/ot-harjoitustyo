class DailyPlanService:
    """Class for daily plan application logic."""

    def __init__(self, dailyplan_repository):
        self._dailyplan_repository = dailyplan_repository

    def create_plans(self,
                     user_id,
                     date,
                     sleep,
                     outsidetime,
                     productivetime,
                     exercisetime,
                     screentime,
                     other
                     ):
        """Calls daily plan repository to add new plans"""
        self._dailyplan_repository.add_plans(
            user_id,
            date,
            sleep,
            outsidetime,
            productivetime,
            exercisetime,
            screentime,
            other
        )

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
