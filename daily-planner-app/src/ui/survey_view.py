# pylint: disable=all
import tkinter as tk
from tkinter import messagebox, ttk
from ui.daily_planner_view import DailyPlanner

# Daily planner view for the application


class SurveyView:
    def __init__(self, master, user_id, user_service, daily_planner_service):
        self._master = master
        self._user_id = user_id

        self._frame = tk.Frame(self._master)
        self._user_service = user_service
        self._daily_planner_service = daily_planner_service
        self._username = self._user_service.get_username(self._user_id)

        self._user_service.complete_first_login(user_id)

        self._welcome_label = tk.Label(
            self._frame, text=f"Welcome, {self._username} answer this survey to get started", font=('Arial', 18))
        self._welcome_label.pack()

        self._age = tk.Label(self._frame, text="Age:")
        self._age.pack()
        # generöity koodi alkaa
        self._age_entry = tk.Spinbox(self._frame, from_=15, to=120, wrap=True)
        self._age_entry.pack()

        self._sex = tk.Label(self._frame, text="Sex:")
        self._sex.pack()

        self._sex_var = tk.StringVar()
        self._sex_entry = ttk.Combobox(
            self._frame, textvariable=self._sex_var, state="readonly", values=['Male', 'Female', 'Other'])
        self._sex_entry.pack()

        self._sleep = tk.Label(
            self._frame, text="How many hours in average do you sleep in a night:")
        self._sleep.pack()

        self._sleep_entry = tk.Spinbox(self._frame, from_=1, to=16, wrap=True)
        self._sleep_entry.pack()
        # generöity koodi loppuu

        self._submit_button = tk.Button(
            self._frame, text="Submit", command=self._submit)
        self._submit_button.pack()

        self._frame.pack()

    def _submit(self):
        age = self._age_entry.get()
        sex = self._sex_var.get()
        sleep = self._sleep_entry.get()

        if not age or not sex or not sleep:
            messagebox.showerror("Error", "All fields are required!")
            return

        try:
            self._user_service.add_info(age, sex, sleep, self._user_id)
        except Exception as e:
            messagebox.showerror("Submission Error", str(e))
            return

        messagebox.showinfo(
            "Success", "Your information has been submitted successfully!")

        self._frame.destroy()
        DailyPlanner(self._master, self._user_id,
                     self._user_service, self._daily_planner_service)
