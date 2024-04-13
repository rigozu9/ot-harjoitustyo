""""Rekisteröionnyn import """
from ui.registration_form import RegistrationForm

class UI:
    """"Näkymien hallinnan tiedosto """
    def __init__(self, root, user_service, daily_plan_service):
        self._root = root
        self._user_service = user_service
        self._daily_plan_service = daily_plan_service
        self._current_view = None

    def start(self):
        """start funktio rekisteröinty forumille"""
        RegistrationForm(self._root, 
                         self._user_service,
                         self._daily_plan_service)
