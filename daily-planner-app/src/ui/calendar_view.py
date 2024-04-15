"""importing tkinter, datetime, userinfoview and messagebox"""
import tkinter as tk
from datetime import datetime
from tkcalendar import Calendar

class CalendarView:
    """Daily planner view for the application"""
    def __init__(self, master, user_id, user_service, daily_plan_service):
        self._master = master
        self._user_id = user_id
        self._user_service = user_service
        self._daily_plan_service = daily_plan_service

        self._frame = tk.Frame(self._master)

        #generöity koodi alkaa
        self.cal = Calendar(self._frame, selectmode='day', year=2024, month=4, day=15)
        self.cal.pack(pady=20)

        # Button to choose date
        self.my_button = tk.Button(self._frame, text="Go to this day", command=self._go_to_date)
        self.my_button.pack(pady=20)

        #generöity koodi loppuu

        self._frame.pack()

    def _go_to_date(self):
        """
            Function to print selected date
            need to import here to avoid cross imports.
        """
        # pylint: disable=import-outside-toplevel
        from ui.today_view import TodayView

        selected_date_str = self.cal.get_date()
        # try:
        #     # Try parsing as 'month/day/four-digit-year'
        #     selected_date = datetime.strptime(selected_date_str, '%m/%d/%Y').date()
        # except ValueError:
        #     # If there's an error, it might be because the year is two digits.
        #     # Try 'month/day/two-digit-year' if your calendar gives you a two-digit year.
        selected_date = datetime.strptime(selected_date_str, '%m/%d/%y').date()

        print("this is the selected_date:", selected_date)
        self._frame.destroy()
        TodayView(self._master,
                self._user_id,
                self._user_service,
                self._daily_plan_service,
                choosen_date=selected_date)

