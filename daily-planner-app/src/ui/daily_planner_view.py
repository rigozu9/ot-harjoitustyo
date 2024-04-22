"""importing tkinter, datetime, userinfoview and messagebox"""
import tkinter as tk
from tkinter import messagebox
from datetime import date
from ui.user_info_view import UserInfoView
from ui.today_view import TodayView
from ui.calendar_view import CalendarView


class DailyPlanner:
    """Daily planner view for the application"""

    def __init__(self, master, user_id, user_service, daily_plan_service, selected_date=None):
        self._master = master
        self._user_id = user_id

        self._frame = tk.Frame(self._master)

        self._user_service = user_service
        self._daily_plan_service = daily_plan_service

        if selected_date:
            self._date = selected_date
        else:
            self._date = date.today()

        self._formatted_date = self._date.strftime('%d-%m-%Y')

        self._username = self._user_service.get_username(self._user_id)

        self._welcome_label = tk.Label(
            self._frame, text=f"Welcome, {self._username} ", font=('Arial', 18))
        self._welcome_label.pack()

        self._date_label = tk.Label(
            self._frame, text=f"Date: {self._formatted_date} ", font=('Arial', 18))
        self._date_label.pack()

        self._info_button = tk.Button(
            self._frame, text="Your profile", command=self._go_to_userpage)
        self._info_button.pack()

        self._go_to_calender_button = tk.Button(
            self._frame, text="Go to calendar", command=self._go_to_calender)
        self._go_to_calender_button.pack()

        # generöity koodi alkaa
        self._create_time_entry("Sleep", "How many hours did you sleep?")
        # Outside time
        self._create_time_entry(
            "Outside", "How many hours did you spend outside?")
        # Productive time
        self._create_time_entry(
            "Productive", "How many hours were you productive (work, school, etc.)?")
        # Exercise time
        self._create_time_entry("Exercise", "How many hours did you exercise?")
        # Screentime
        self._create_time_entry(
            "Screen", "What was your screentime (hours and minutes)?")
        # generöity koodi loppuu

        self._other_label = tk.Label(
            self._frame, text="What other activities did you do?:")
        self._other_label.pack()

        self._other_entry = tk.Entry(self._frame, width=30)
        self._other_entry.pack()

        self._submit_button = tk.Button(
            self._frame, text="Submit", command=self._submit)
        self._submit_button.pack()

        self._frame.pack()

    # generöity koodi alkaa
    def _create_time_entry(self, activity_name, label_text):
        """
        Helper method to create hour and minute entries for an activity.
        """
        setattr(self, f"_{activity_name.lower()}_label",
                tk.Label(self._frame, text=label_text))
        getattr(self, f"_{activity_name.lower()}_label").pack()

        time_frame = tk.Frame(self._frame)
        time_frame.pack()

        setattr(self, f"_{activity_name.lower()}_hours_entry",
                tk.Entry(time_frame, width=5))
        getattr(self, f"_{activity_name.lower()}_hours_entry").pack(
            side=tk.LEFT)
        tk.Label(time_frame, text="hours").pack(side=tk.LEFT)

        setattr(self, f"_{activity_name.lower()}_minutes_entry",
                tk.Entry(time_frame, width=5))
        getattr(self, f"_{activity_name.lower()}_minutes_entry").pack(
            side=tk.LEFT)
        tk.Label(time_frame, text="minutes").pack(side=tk.LEFT)

    def _submit(self):
        """Submit the information with validation for new time inputs."""
        try:
            # Helper function to calculate total minutes from hours and minutes entries
            def get_total_minutes(activity_name):
                hours = int(
                    getattr(self, f"_{activity_name.lower()}_hours_entry").get())
                minutes = int(
                    getattr(self, f"_{activity_name.lower()}_minutes_entry").get())
                if not (0 <= hours <= 24 and 0 <= minutes < 60):
                    raise ValueError(
                        f"{activity_name} time must be a valid time of day.")
                return hours * 60 + minutes

            # Calculate total minutes for all activities
            total_sleep_minutes = get_total_minutes("Sleep")
            total_outside_minutes = get_total_minutes("Outside")
            total_productive_minutes = get_total_minutes("Productive")
            total_exercise_minutes = get_total_minutes("Exercise")
            total_screen_minutes = get_total_minutes("Screen")

            # Call the daily_plan_service to create or update the plan
            self._daily_plan_service.create_plans(
                self._user_id,
                self._date,
                total_sleep_minutes,
                total_outside_minutes,
                total_productive_minutes,
                total_exercise_minutes,
                total_screen_minutes,
                self._other_entry.get()  # Assuming you're keeping the other activity as a simple entry
            )

            messagebox.showinfo(
                "Success", "Your daily plan has been submitted successfully!")
            self._frame.destroy()
            TodayView(self._master, self._user_id,
                      self._user_service, self._daily_plan_service)

        except ValueError as e:
            messagebox.showerror("Submission Error", str(e))
    # generöity koodi loppuu

    def _go_to_userpage(self):
        """go to userinfoview"""
        self._frame.destroy()
        UserInfoView(self._master,
                     self._user_id,
                     self._user_service,
                     self._daily_plan_service)

    def _go_to_calender(self):
        """method for going to calendar"""
        self._frame.destroy()
        CalendarView(self._master,
                     self._user_id,
                     self._user_service,
                     self._daily_plan_service)
