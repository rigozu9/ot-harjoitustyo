import tkinter as tk
from services.user_service import UserService
from ui.daily_planner_view import DailyPlanner
""""Sisäänkirjatumisen form. Kysyy nimeä ja salasanaa.
    Käyttää user_service, kun kirjatuu. """

class LoginForm:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.user_service = UserService()

        self.username_label = tk.Label(self.frame, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.pack()

        self.username_label = tk.Label(self.frame, text="Password:")
        self.username_label.pack()
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.frame, text="Login", command=self._login)
        self.login_button.pack()

        self.frame.pack()

    def _login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.user_service.login_user(username, password):
            self.frame.destroy()
            DailyPlanner(self.master)
        else:
            pass