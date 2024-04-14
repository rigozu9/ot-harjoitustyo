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
