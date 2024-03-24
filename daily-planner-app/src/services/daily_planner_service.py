#Class for dailyplanner application logic

from repositories.activity_repository import ActivityRepository
from database_connection import get_database_connection

class DailyPlannerService:
    #initializing database for ActivityRepository
    def __init__(self):
        self._activity_repository = ActivityRepository(get_database_connection())

    def add_activity(self, description, user_id):
        self._activity_repository.add_activity(description, user_id)
        return True

    def show_activities(self, user_id):
        return self._activity_repository.get_all_activities_by_user(user_id)
    
    def get_username(self, user_id):
        return self._activity_repository.get_username_by_user(user_id)
