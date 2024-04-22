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

    # def get_all_plans_by_id(self, user_id):
    #     """gets users plans from repository"""
    #     return self._dailyplan_repository.get_all_plans_for_user_db(user_id)

    def calculate_average_attributes(self, user_id):
        """get all plans from user and calcualte averages"""
        plans = self._dailyplan_repository.get_all_plans_for_user_db(user_id)
        if not plans:
            return None

        total_sleep = 0
        total_outside_time = 0
        total_productive_time = 0
        total_exercise = 0
        total_screen_time = 0
        count = 0

        for plan in plans:
            if plan.sleep is not None:
                total_sleep += plan.sleep
            if plan.outside_time is not None:
                total_outside_time += plan.outside_time
            if plan.productive_time is not None:
                total_productive_time += plan.productive_time
            if plan.exercise is not None:
                total_exercise += plan.exercise
            if plan.screen_time is not None:
                total_screen_time += plan.screen_time
            count += 1

        if count == 0:
            return None

        average_sleep = total_sleep / count
        average_outside_time = total_outside_time / count
        average_productive_time = total_productive_time / count
        average_exercise = total_exercise / count
        average_screen_time = total_screen_time / count

        return {
            "avg_sleep": average_sleep,
            "avg_outside_time": average_outside_time,
            "avg_productive_time": average_productive_time,
            "avg_exercise": average_exercise,
            "avg_screen_time": average_screen_time
        }
