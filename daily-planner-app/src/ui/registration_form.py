import tkinter as tk
from ui.login_form import LoginForm

""""Rekisteröitymisen form. Kysyy nimeä ja salasanaa.
    Käyttää user_service, kun kirjatuu. 
    Nappi myös kirjatumiselle, jos on jo käyttäjä """

class RegistrationForm:
    def __init__(self, master, user_service, daily_planner_service):
        self._master = master
        self._frame = tk.Frame(self._master)
        self._user_service = user_service
        self._daily_planner_service = daily_planner_service

        self._username_label = tk.Label(self._frame, text="Username:")
        self._username_label.pack()
        self._username_entry = tk.Entry(self._frame)
        self._username_entry.pack()

        self._password_label = tk.Label(self._frame, text="Password:")
        self._password_label.pack()
        self._password_entry = tk.Entry(self._frame, show="*")
        self._password_entry.pack()

        self._register_button = tk.Button(self._frame, text="Register", command=self._register)
        self._register_button.pack()

        self._goto_login_button = tk.Button(self._frame, text="Already have an account? Go to Login", command=self._go_to_login)
        self._goto_login_button.pack()

        self._frame.pack()

    def _register(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        
        if self._user_service.register_user(username, password):
            self._frame.destroy()
            LoginForm(self._master, self._user_service, self._daily_planner_service) 
        else:
            pass

    def _go_to_login(self):
        self._frame.destroy()
        LoginForm(self._master, self._user_service, self._daily_planner_service)