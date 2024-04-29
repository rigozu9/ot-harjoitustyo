"""importing tkinter, datetime, userinfoview and messagebox"""
import tkinter as tk
from tkinter import Canvas, messagebox
import math
from datetime import date
from ui.calendar_view import CalendarView
from ui.user_info_view import UserInfoView


class TodayView:
    """Todays view for the application to see the days activities"""

    def __init__(self, master, user_id, user_service, daily_plan_service, choosen_date=None):
        self._master = master
        self._user_id = user_id

        self._frame = tk.Frame(self._master)

        self._canvas = Canvas(self._master, width=500, height=500)
        self._canvas.place(x=190, y=260)

        self._user_service = user_service
        self._daily_plan_service = daily_plan_service

        if choosen_date:
            self._date = choosen_date
        else:
            self._date = date.today()

        self._formatted_date = self._date.strftime('%d-%m-%Y')

        self._username = self._user_service.get_username(self._user_id)

        self._info_button = tk.Button(
            self._frame, text="Your profile", command=self._go_to_userpage)
        self._info_button.pack()

        self._date_label = tk.Label(
            self._frame, text=f"{self._username}'s activities on {self._formatted_date}", font=('Arial', 18))
        self._date_label.pack()

        self._plans = self._daily_plan_service.get_plans_by_id(
            self._user_id, self._date)

        if self._plans:
            self._create_and_pack_label(f"You slept for: {self._plans.sleep/60:.1f} hours", self._frame)
            self._create_and_pack_label(f"You spent {self._plans.outside_time/60:.1f} hours outside:", self._frame)
            self._create_and_pack_label(f"You spent {self._plans.productive_time/60:.1f} hours productive things:", self._frame)
            self._create_and_pack_label(f"You spent {self._plans.exercise/60:.1f} hours exercising:", self._frame)
            self._create_and_pack_label(f"Your screentime was {self._plans.screen_time/60:.1f} hours:", self._frame)
            self._create_and_pack_label(f"You also did other stuff like: {self._plans.other_activities}", self._frame)

            self._delete_plan_button = tk.Button(
                self._frame, text="Delete daily plan", command=self._delete_plan)
            self._delete_plan_button.pack()

            self._go_to_calender_button = tk.Button(
                self._frame, text="Go to calendar", command=self._go_to_calender)
            self._go_to_calender_button.pack()

            self._plans_summed = self._plans.sleep+self._plans.outside_time + \
                self._plans.productive_time+self._plans.exercise+self._plans.screen_time

            self._sleep_fraction = self._plans.sleep/self._plans_summed*100
            self._outside_timefraction = self._plans.outside_time/self._plans_summed*100
            self._productive_time_fraction = self._plans.productive_time/self._plans_summed*100
            self._exercise_fraction = self._plans.exercise/self._plans_summed*100
            self._screen_time_fraction = self._plans.screen_time/self._plans_summed*100

            self._pie_v = [self._sleep_fraction, self._outside_timefraction,
                           self._productive_time_fraction, self._exercise_fraction, self._screen_time_fraction]

            self._col_v = ["red", "blue", "orange", "green", "black"]
            self._create_piechart(self._pie_v, self._col_v)

        else:
            self._no_plan_label = tk.Label(
                self._frame, text="There are no plans for this date.")
            self._no_plan_label.pack()

            self._go_to_planner_button = tk.Button(
                self._frame, text="Add plan here", command=self._go_to_planner)
            self._go_to_planner_button.pack()

        self._frame.pack()

    def _create_and_pack_label(self, text, frame):
        """Helper function to create a label with the specified text and pack it into the given frame."""
        label = tk.Label(frame, text=text, anchor="w")
        label.pack(fill='x', padx=10)

    def _create_piechart(self, pie_v, col_v):
        """create a piechart for the user info"""
        st = 0  # Start angle for the first segment
        coord = 100, 100, 300, 300  # The bounding coordinates of the pie chart
        activity_labels = [
            f"Sleep {self._plans.sleep / 60:.1f} hours",
            f"Outside {self._plans.outside_time / 60:.1f} hours",
            f"Productive {self._plans.productive_time / 60:.1f} hours",
            f"Exercise {self._plans.exercise / 60:.1f} hours",
            f"Screen Time {self._plans.screen_time / 60:.1f} hours"
        ]

        center_x = (coord[0] + coord[2]) / 2
        center_y = (coord[1] + coord[3]) / 2
        radius = (coord[2] - coord[0]) / 2
        text_offset = radius * 1.2  # Position the text slightly outside the pie chart

        for val, col, label in zip(pie_v, col_v, activity_labels):
            # generöity koodi alkaa
            # Calculate extent as a percentage of 360 degrees
            extent = val * 3.6
            # Draw the arc (a slice of the pie chart)
            self._canvas.create_arc(
                coord, start=st, extent=extent, fill=col, outline=col)

            # Calculate the angle in the middle of the slice
            mid_angle = st + extent / 2
            # Convert the angle to radians for text placement
            angle_rad = math.radians(mid_angle)
            # Calculate the text coordinates using polar coordinates
            text_x = center_x + text_offset * math.cos(angle_rad)
            # Minus because the y-coordinates go down
            text_y = center_y - text_offset * math.sin(angle_rad)

            # Create the text with a contrasting color
            self._canvas.create_text(text_x, text_y, text=label, fill="white")

            # Optionally, draw a line from the text to the slice
            line_end_x = center_x + radius * 0.5 * math.cos(angle_rad)
            line_end_y = center_y - radius * 0.5 * math.sin(angle_rad)
            self._canvas.create_line(
                text_x, text_y, line_end_x, line_end_y, fill="cyan")

            # Update the start angle for the next slice
            st += extent
            # generöity koodi loppuu

    def _go_to_calender(self):
        """method for going to calendar"""
        self._frame.destroy()
        self._canvas.destroy()
        CalendarView(self._master,
                     self._user_id,
                     self._user_service,
                     self._daily_plan_service)
        
    def _delete_plan(self):
        """
            method for deleting a dailyplan
            if deleted goes to dailyplanner so you can make new plan
            need to import here to avoid cross imports.
        """
        # pylint: disable=import-outside-toplevel
        if messagebox.askyesno("Confirm", "Do you want to delete this plan?"):
            plan_id = self._plans.id
            self._daily_plan_service.remove_plan(plan_id)
            messagebox.showinfo("Success", "Plan deleted successfully.")
            from ui.daily_planner_view import DailyPlanner
            self._frame.destroy()
            self._canvas.destroy()
            DailyPlanner(self._master,
                        self._user_id,
                        self._user_service,
                        self._daily_plan_service,
                        self._date)
        else:
            messagebox.showinfo("Cancelled", "Plan deletion cancelled.")

    def _go_to_planner(self):
        """
            method for going to calendar
            need to import here to avoid cross imports.
        """
        # pylint: disable=import-outside-toplevel
        from ui.daily_planner_view import DailyPlanner
        self._frame.destroy()
        self._canvas.destroy()
        DailyPlanner(self._master,
                     self._user_id,
                     self._user_service,
                     self._daily_plan_service,
                     self._date)

    def _go_to_userpage(self):
        """go to userinfoview"""
        self._frame.destroy()
        self._canvas.destroy()
        UserInfoView(self._master,
                     self._user_id,
                     self._user_service,
                     self._daily_plan_service)
