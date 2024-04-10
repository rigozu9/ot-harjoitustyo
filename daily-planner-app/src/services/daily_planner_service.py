class DailyPlannerService:
    """Class for dailyplanner application logic"""
    def __init__(self, activity_repository):
        self._activity_repository = activity_repository

    def create_activity(self, description, user_id):
        """calls activity repo's add_activity to create an activity with desc and user id"""
        self._activity_repository.add_activity(description, user_id)
        return True

    def remove_activity(self, activity_id):
        """calls activity repo's delete_activity to delete an activity with activity id"""
        self._activity_repository.delete_activity(activity_id)
        return True

    def show_activities(self, user_id):
        """calls activity repo's get_all_activities_by_user"""
        return self._activity_repository.get_all_activities_by_user(user_id)
