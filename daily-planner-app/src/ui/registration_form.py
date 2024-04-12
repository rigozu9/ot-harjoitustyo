# pylint: disable=all
import tkinter as tk
from tkinter import messagebox  # Import messagebox for showing error messages
from ui.login_form import LoginForm


class RegistrationForm:
    def __init__(self, master, user_service, daily_planner_service, daily_plan_service):
        self._master = master
        self._frame = tk.Frame(self._master)
        self._user_service = user_service
        self._daily_planner_service = daily_planner_service
        self._daily_plan_service = daily_plan_service

        self._username_label = tk.Label(self._frame, text="Username:")
        self._username_label.pack()
        self._username_entry = tk.Entry(self._frame)
        self._username_entry.pack()

        self._password_label = tk.Label(self._frame, text="Password:")
        self._password_label.pack()
        self._password_entry = tk.Entry(self._frame, show="*")
        self._password_entry.pack()

        self._password_confirm_label = tk.Label(
            self._frame, text="Confirm Password:")  # Add confirmation label
        self._password_confirm_label.pack()
        self._password_confirm_entry = tk.Entry(
            self._frame, show="*")  # Add confirmation entry
        self._password_confirm_entry.pack()

        self._register_button = tk.Button(
            self._frame, text="Register", command=self._register)
        self._register_button.pack()

        self._goto_login_button = tk.Button(
            self._frame, text="Already have an account? Go to Login", command=self._go_to_login)
        self._goto_login_button.pack()

        self._frame.pack()

    def _register(self):
        username = self._username_entry.get()
        password = self._password_entry.get()
        password_confirm = self._password_confirm_entry.get()

        if password != password_confirm:
            # Show error if passwords don't match
            messagebox.showerror("Error", "Passwords do not match.")
            return

        registration_result = self._user_service.register_user(
            username, password)
        if registration_result == "success":
            self._frame.destroy()
            LoginForm(self._master, self._user_service,
                      self._daily_planner_service,
                      self._daily_plan_service)
        elif registration_result == "username_exists":
            # Show error if username is in use
            messagebox.showerror("Error", "Username already exists.")
        elif registration_result == "password_short":
            # Show error if username is in use
            messagebox.showerror("Error", "Password too short.")
        else:
            messagebox.showerror(
                "Error", "Registration failed for an unknown reason.")

    def _go_to_login(self):
        self._frame.destroy()
        LoginForm(self._master, self._user_service,
                  self._daily_planner_service,
                  self._daily_plan_service)
