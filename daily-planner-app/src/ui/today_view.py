"""importing tkinter, datetime, userinfoview and messagebox"""
import tkinter as tk
from datetime import date

class TodayView:
    """Todays view for the application to see the days activities"""
    def __init__(self, master, user_id, user_service, daily_plan_service):
        self._master = master
        self._user_id = user_id
        self._activity_frames = []

        self._frame = tk.Frame(self._master)
        self._user_service = user_service
        self._daily_plan_service = daily_plan_service

        self._date = date.today()
        self._username = self._user_service.get_username(self._user_id)

        self._date_label = tk.Label(
            self._frame, text=f"{self._date}'s activities", font=('Arial', 18))
        self._date_label.pack()
      
        self._plans = self._daily_plan_service.get_plans_by_id(self._user_id, self._date)
       
        self._sleep_label = tk.Label(
            self._frame, text=f"You slept for: {self._plans.sleep} hours")
        self._sleep_label.pack()
      
        self._outside_label = tk.Label(
            self._frame, text=f"You spent {self._plans.outside_time} hours outside:")
        self._outside_label.pack()

        self._productivity_label = tk.Label(
            self._frame, text=f"You spent {self._plans.productive_time} hours productive things:")
        self._productivity_label.pack()

        self._exercise_label = tk.Label(
            self._frame, text=f"You spent {self._plans.exercise} hours exercising:")
        self._exercise_label.pack()

        self._screentime_label = tk.Label(
            self._frame, text=f"Your screentime was {self._plans.screen_time} hours:")
        self._screentime_label.pack()

        self._other_label = tk.Label(
            self._frame, text=f"You also did other stuff like: {self._plans.other_activities} ")
        self._other_label.pack()

        self._frame.pack()