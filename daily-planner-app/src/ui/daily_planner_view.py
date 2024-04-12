# pylint: disable=all   
import tkinter as tk
from datetime import date
from ui.user_info_view import UserInfoView
from tkinter import messagebox  # Import messagebox for showing error messages


# Daily planner view for the application


class DailyPlanner:
    def __init__(self, master, user_id, user_service, daily_planner_service, daily_plan_service):
        self._master = master
        self._user_id = user_id
        self._activity_frames = []

        self._frame = tk.Frame(self._master)
        self._user_service = user_service
        self._daily_planner_service = daily_planner_service
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

        self._activities_label = tk.Label(self._frame, text="Your activities:")
        self._activities_label.pack()

        self._frame.pack()

        #self._display_activities()

    def _submit(self):
        try:
            self._daily_plan_service.create_plans(
                self._user_id, self._date, self._sleep_entry.get(), self._outside_entry.get(),
                self._productivity_entry.get(), self._exercise_entry.get(), self._screentime_entry.get(),
                self._other_entry.get()
            )
            #self._display_activities()  # Refresh or update the UI as needed
        except ValueError as error:
            messagebox.showerror("Error", str(error))
        #self._display_activities()

    def _go_to_userpage(self):
        self._frame.destroy()
        UserInfoView(self._master, self._user_id,
                     self._user_service, self._daily_planner_service)

    def _display_activities(self):
        # Clear existing activity frames
        for frame in self._activity_frames:
            frame.destroy()
        self._activity_frames.clear()  # Reset the list after clearing frames

        activities = self._daily_planner_service.show_activities(self._user_id)
        for activity in activities:
            activity_frame = tk.Frame(self._frame)
            self._activity_frames.append(activity_frame)
            activity_frame.pack()

            activity_label = tk.Label(
                activity_frame, text=activity.description)
            activity_label.pack(side=tk.LEFT)

            remove_button = tk.Button(
                activity_frame, text="Remove", command=lambda activity_id=activity.id: self._remove_activity(activity_id))
            remove_button.pack(side=tk.RIGHT)

    def _remove_activity(self, activity_id):
        self._daily_planner_service.remove_activity(activity_id)
        self._display_activities()
