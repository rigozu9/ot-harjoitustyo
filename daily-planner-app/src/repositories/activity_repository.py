"""Activity entity class import"""
from entities.activity import Activity


class ActivityRepository:
    """Activity repository for database actions"""
    def __init__(self, session):
        self._session = session

    def add_activity(self, description, user_id):
        """Adding an activity to the database"""
        new_activity = Activity(description=description, user_id=user_id)
        self._session.add(new_activity)
        self._session.commit()
        return new_activity

    def get_all_activities_by_user(self, user_id):
        """Retrieving user's activities"""
        activities = self._session.query(
            Activity).filter_by(user_id=user_id).all()
        return activities

    def delete_activity(self, activity_id):
        """delete an activity"""
        activity_to_delete = self._session.query(
            Activity).filter_by(id=activity_id).first()
        if activity_to_delete:
            self._session.delete(activity_to_delete)
            self._session.commit()
            return True
        return False
