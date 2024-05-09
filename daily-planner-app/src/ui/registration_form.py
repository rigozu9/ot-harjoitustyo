"""importing tkinter, messagebox for errors and loginform."""
import tkinter as tk
from tkinter import messagebox


class RegistrationForm:
    """Registration form view"""

    def __init__(self, master, user_service, daily_plan_service, views):
        self._master = master
        self._frame = tk.Frame(self._master)
        self._user_service = user_service
        self._daily_plan_service = daily_plan_service

        self._handle_show_login_view = views['login']

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
        """function for registering."""
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
            self._go_to_login()
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
        """method for goign back to login"""
        self._frame.destroy()
        self._handle_show_login_view()
