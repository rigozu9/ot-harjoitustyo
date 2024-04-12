class DailyPlanService:
    """Class for daily plan application logic."""

    def __init__(self, dailyplan_repository):
        self._dailyplan_repository = dailyplan_repository

    def create_plans(self, user_id, date, sleep, outsidetime, productivetime, 
                     exercisetime, screentime, other=None):
        """
            Calls daily plan repository to add new plans, ensuring all required fields are 
            provided and valid.
        """
        #generöity koodi alkaa
        try:
            sleep = int(sleep)
            outsidetime = int(outsidetime)
            productivetime = int(productivetime)
            exercisetime = int(exercisetime)
            screentime = int(screentime)

            required_params = [sleep, outsidetime, productivetime, exercisetime, screentime]
            if any(param < 0 for param in required_params):
                raise ValueError("All time values must be non-negative integers.")

        except ValueError as ve:
            raise ValueError(f"Input validation error: {str(ve)}") from ve
        #generöity koodi loppuu
        self._dailyplan_repository.add_plans(
            user_id, date, sleep, outsidetime, productivetime, exercisetime, screentime, other
        )
