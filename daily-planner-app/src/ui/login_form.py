import tkinter as tk
from tkinter import messagebox
from ui.daily_planner_view import DailyPlanner
from ui.survey_view import SurveyView
""""Sisäänkirjatumisen form. Kysyy nimeä ja salasanaa.
    Käyttää user_service, kun kirjatuu. """

class LoginForm:
    def __init__(self, master, user_service, daily_planner_service, survey_service):
        self._master = master
        self._frame = tk.Frame(self._master)
        self._user_service = user_service
        self._daily_planner_service = daily_planner_service
        self._survey_service = survey_service

        self._username_label = tk.Label(self._frame, text="Username:")
        self._username_label.pack()
        self._username_entry = tk.Entry(self._frame)
        self._username_entry.pack()

        self._password_label = tk.Label(self._frame, text="Password:")
        self._password_label.pack()
        self._password_entry = tk.Entry(self._frame, show="*")
        self._password_entry.pack()

        self._login_button = tk.Button(self._frame, text="Login", command=self._login)
        self._login_button.pack()

        self._frame.pack()

    def _login(self):
        username = self._username_entry.get()
        password = self._password_entry.get()

        user_id = self._user_service.login_user(username, password)
        if user_id:
            self._frame.destroy()
            first_login = self._user_service.is_first_login(user_id)
            if first_login:
                SurveyView(self._master, user_id, self._user_service, self._daily_planner_service, self._survey_service)
            else:
                DailyPlanner(self._master, user_id, self._user_service, self._daily_planner_service)

        else:
            # Display an error message if login fails
            messagebox.showerror("Login failed", "Incorrect username or password.")