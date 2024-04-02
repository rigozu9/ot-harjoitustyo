#Class for dailyplanner application logic
#Now receives the repository when app starting or testing

class DailyPlannerService:
    def __init__(self, activity_repository):
        self._activity_repository = activity_repository

    def create_activity(self, description, user_id):
        self._activity_repository.add_activity(description, user_id)
        return True

    def remove_activity(self, activity_id):
        self._activity_repository.delete_activity(activity_id)
        return True

    def show_activities(self, user_id):
        return self._activity_repository.get_all_activities_by_user(user_id)
