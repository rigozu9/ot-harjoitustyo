from ui.registration_form import RegistrationForm

""""Näkymien hallinnan tiedosto """

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        RegistrationForm(self._root)