"""tkinter import, messagebox for error dailyplanner and surveyview"""
import tkinter as tk
from tkinter import messagebox
from datetime import date


class LoginForm:
    """"Sisäänkirjatumisen form. Kysyy nimeä ja salasanaa.
    Käyttää user_service, kun kirjatuu. """

    def __init__(self, master, user_service, daily_plan_service, views):

        self._master = master
        self._frame = tk.Frame(self._master)
        self._user_service = user_service
        self._daily_plan_service = daily_plan_service

        self._handle_show_registration_view = views['register']
        self._handle_show_today_view = views['today']
        self._handle_show_survey_view = views['survey']
        self._handle_show_daily_plan_view = views['daily_planner']

        self._date = date.today()

        self._username_label = tk.Label(self._frame, text="Username:")
        self._username_label.pack()
        self._username_entry = tk.Entry(self._frame)
        self._username_entry.pack()

        self._password_label = tk.Label(self._frame, text="Password:")
        self._password_label.pack()
        self._password_entry = tk.Entry(self._frame, show="*")
        self._password_entry.pack()

        self._login_button = tk.Button(
            self._frame, text="Login", command=self._login)
        self._login_button.pack()

        self._goto_register_button = tk.Button(
            self._frame, text="Don't have an account? Register", command=self._go_to_register)
        self._goto_register_button.pack()

        self._frame.pack()

    def _login(self):
        """login method"""
        username = self._username_entry.get()
        password = self._password_entry.get()

        user_id = self._user_service.login_user(username, password)
        plans = self._daily_plan_service.get_plans_by_id(user_id, self._date)
        if user_id:
            self._frame.destroy()
            first_login = self._user_service.is_first_login(user_id)
            if plans:
                self._handle_show_today_view(user_id)
            elif first_login:
                self._handle_show_survey_view(user_id)
            else:
                self._handle_show_daily_plan_view(user_id)
        else:
            # Display an error message if login fails
            messagebox.showerror(
                "Login failed", "Incorrect username or password.")

    def _go_to_register(self):
        """going to register method"""
        self._frame.destroy()
        self._handle_show_registration_view()
