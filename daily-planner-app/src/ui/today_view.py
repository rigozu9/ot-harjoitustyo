"""importing tkinter, datetime, userinfoview and messagebox"""
import tkinter as tk
from datetime import date
from ui.calendar_view import CalendarView

class TodayView:
    """Todays view for the application to see the days activities"""
    def __init__(self, master, user_id, user_service, daily_plan_service, choosen_date=None):
        self._master = master
        self._user_id = user_id

        self._frame = tk.Frame(self._master)
        self._user_service = user_service
        self._daily_plan_service = daily_plan_service

        if choosen_date:
            self._date = choosen_date
        else:
            self._date = date.today()

        self._formatted_date = self._date.strftime('%d-%m-%Y')

        self._username = self._user_service.get_username(self._user_id)

        self._date_label = tk.Label(
            self._frame, text=f"{self._username}'s activities on {self._formatted_date}", font=('Arial', 18))
        self._date_label.pack()
      
        self._plans = self._daily_plan_service.get_plans_by_id(self._user_id, self._date)
       
        if self._plans:
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

            self._go_to_calender_button = tk.Button(
                self._frame, text="Go to calendar", command=self._go_to_calender)
            self._go_to_calender_button.pack()

        else:
            self._no_plan_label = tk.Label(
                self._frame, text="NO PLANS HERE!!")
            self._no_plan_label.pack()

        self._frame.pack()

    def _go_to_calender(self):
        """method for going to calendar"""
        self._frame.destroy()
        CalendarView(self._master,
                    self._user_id,
                    self._user_service,
                    self._daily_plan_service)
        