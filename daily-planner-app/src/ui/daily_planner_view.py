"""importing tkinter, datetime, userinfoview and messagebox"""
import tkinter as tk
from datetime import date
from ui.user_info_view import UserInfoView
from ui.today_view import TodayView

class DailyPlanner:
    """Daily planner view for the application"""
    def __init__(self, master, user_id, user_service, daily_plan_service):
        self._master = master
        self._user_id = user_id
        self._activity_frames = []

        self._frame = tk.Frame(self._master)
        self._user_service = user_service
        self._daily_plan_service = daily_plan_service

        self._date = date.today()
        self._username = self._user_service.get_username(self._user_id)

        self._welcome_label = tk.Label(
            self._frame, text=f"Welcome, {self._username} ", font=('Arial', 18))
        self._welcome_label.pack()

        self._date_label = tk.Label(
            self._frame, text=f"Todays date, {self._date} ", font=('Arial', 18))
        self._date_label.pack()

        self._info_button = tk.Button(
            self._frame, text="Your profile", command=self._go_to_userpage)
        self._info_button.pack()

        self._sleep_label = tk.Label(
            self._frame, text="How many hours did you sleep?:")
        self._sleep_label.pack()

        self._sleep_entry = tk.Spinbox(self._frame, from_=0, to=24, wrap=True)
        self._sleep_entry.pack()
        
        self._outside_label = tk.Label(
            self._frame, text="How many hours did you spent outside?:")
        self._outside_label.pack()

        self._outside_entry = tk.Spinbox(self._frame, from_=0, to=24, wrap=True)
        self._outside_entry.pack()

        self._productivity_label = tk.Label(
            self._frame, text="How many hours did you spent on productive things. School, work, cleaning etc?:")
        self._productivity_label.pack()

        self._productivity_entry = tk.Spinbox(self._frame, from_=0, to=24, wrap=True)
        self._productivity_entry.pack()

        self._exercise_label = tk.Label(
            self._frame, text="How many hours did you spent exercising?:")
        self._exercise_label.pack()

        self._exercise_entry = tk.Spinbox(self._frame, from_=0, to=24, wrap=True)
        self._exercise_entry.pack()

        self._screentime_label = tk.Label(
            self._frame, text="What was your screentime?:")
        self._screentime_label.pack()

        self._screentime_entry = tk.Spinbox(self._frame, from_=0, to=24, wrap=True)
        self._screentime_entry.pack()

        self._other_label = tk.Label(
            self._frame, text="What other activities did you do?:")
        self._other_label.pack()

        self._other_entry = tk.Entry(self._frame, width=30)
        self._other_entry.pack()

        self._submit_button = tk.Button(
            self._frame, text="Submit", command=self._submit)
        self._submit_button.pack()

        self._frame.pack()


    def _submit(self):
        self._daily_plan_service.create_plans(
            self._user_id,
            self._date,
            self._sleep_entry.get(),
            self._outside_entry.get(),
            self._productivity_entry.get(),
            self._exercise_entry.get(),
            self._screentime_entry.get(),
            self._other_entry.get()
        )
        self._frame.destroy()
        TodayView(self._master,
                     self._user_id,
                     self._user_service,
                     self._daily_plan_service)


    def _go_to_userpage(self):
        """go to userinfoview"""
        self._frame.destroy()
        UserInfoView(self._master,
                     self._user_id,
                     self._user_service,
                     self._daily_plan_service)
