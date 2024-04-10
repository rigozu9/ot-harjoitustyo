from ui.registration_form import RegistrationForm

""""Näkymien hallinnan tiedosto """


class UI:
    def __init__(self, root, user_service, daily_planner_service):
        self._root = root
        self._user_service = user_service
        self._daily_planner_service = daily_planner_service
        self._current_view = None

    # Aloittaa rekisteröinti formilla
    def start(self):
        RegistrationForm(self._root, self._user_service,
                         self._daily_planner_service)
