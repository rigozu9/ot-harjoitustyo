#Repository for survey database methods and functions
from entities.user import User
class SurveyRepository:
    def __init__(self, session):
        self._session = session