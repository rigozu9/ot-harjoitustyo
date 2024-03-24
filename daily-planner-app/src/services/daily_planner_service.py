from repositories.activity_repository import ActivityRepository
from database_connection import get_database_connection

class DailyPlannerService:
    def __init__(self):
        self._activity_repository = ActivityRepository(get_database_connection())

    def add_activity(self, description):
        self._activity_repository.add_activity(description)
        return True

    def show_activities(self):
        return self._activity_repository.get_all_activities()
