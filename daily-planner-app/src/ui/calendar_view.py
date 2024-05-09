"""importing tkinter, datetime, userinfoview and messagebox"""
import tkinter as tk
from datetime import datetime
from tkcalendar import Calendar


class CalendarView:
    """Daily planner view for the application"""

    def __init__(self, master, user_id, user_service, daily_plan_service, views):
        self._master = master
        self._user_id = user_id
        self._user_service = user_service
        self._daily_plan_service = daily_plan_service

        self._handle_show_user_info_view = views['user_info']
        self._handle_show_today_view = views['today']

        self._frame = tk.Frame(self._master)

        # generöity koodi alkaa
        self._today = datetime.today()
        self.cal = Calendar(self._frame, selectmode='day',
                            year=self._today.year, month=self._today.month, day=self._today.day)
        self.cal.pack(pady=20)

        # Button to choose date
        self.my_button = tk.Button(
            self._frame, text="Go to this day", command=self._go_to_date)
        self.my_button.pack(pady=20)

        # generöity koodi loppuu
        self._info_button = tk.Button(
            self._frame, text="Your profile", command=self._go_to_userpage)
        self._info_button.pack()

        self._frame.pack()

    def _go_to_date(self):
        """Function to go to selected date"""
        selected_date_str = self.cal.get_date()
        try:
            # error handling for possible date problems
            selected_date = datetime.strptime(
                selected_date_str, '%d/%m/%Y').date()
        except ValueError:
            try:
                selected_date = datetime.strptime(
                    selected_date_str, '%d/%m/%y').date()
            except ValueError:
                try:
                    selected_date = datetime.strptime(
                        selected_date_str, '%m/%d/%Y').date()
                except ValueError:
                    selected_date = datetime.strptime(
                        selected_date_str, '%m/%d/%y').date()

        self._frame.destroy()
        self._handle_show_today_view(self._user_id, selected_date)

    def _go_to_userpage(self):
        """go to userinfoview"""
        self._frame.destroy()
        self._handle_show_user_info_view(self._user_id)
