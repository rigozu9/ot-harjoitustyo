#Changed to use sqlaclhemy instead of raw sql commands
#Repository for activity database methods and functions
from entities.activity import Activity

class ActivityRepository:
    def __init__(self, session):
        self._session = session

    # Adding an activity to the database
    def add_activity(self, description, user_id):
        new_activity = Activity(description=description, user_id=user_id)
        self._session.add(new_activity)
        self._session.commit()
        return new_activity

    # Retrieving user's activities
    def get_all_activities_by_user(self, user_id):
        activities = self._session.query(Activity).filter_by(user_id=user_id).all()
        return activities

    def delete_activity(self, activity_id):
        # Find the activity by ID
        activity_to_delete = self._session.query(Activity).filter_by(id=activity_id).first()
        if activity_to_delete:
            # If the activity exists, delete it
            self._session.delete(activity_to_delete)
            self._session.commit()
            return True
        else:
            # If the activity does not exist, return False or handle as needed
            return False