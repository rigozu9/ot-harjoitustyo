"""tkinter import"""
import tkinter as tk
from tkinter import Canvas
import math


class UserInfoView:
    """here you can see your own information"""

    def __init__(self, master, user_id, user_service, daily_plan_service):
        self._master = master
        self._user_id = user_id

        self._frame = tk.Frame(self._master)

        self._canvas = Canvas(self._master, width=500, height=500)
        self._canvas.place(x=190, y=190)

        self._user_service = user_service
        self._daily_plan_service = daily_plan_service

        self._username = self._user_service.get_username(self._user_id)

        self._welcome_label = tk.Label(
            self._frame, text=f"{self._username}'s information and goals", font=('Arial', 18))
        self._welcome_label.pack()

        self._goto_dailyplanner_button = tk.Button(
            self._frame, text="Todays view", command=self._goto_todayview)
        self._goto_dailyplanner_button.pack()

        self._info = self._user_service.show_info(self._user_id)
        self._display_info()
        self._info_summed = sum(self._info[2:])

        self._sleep_fraction = self._info[2]/self._info_summed*100
        self._outside_timefraction = self._info[3]/self._info_summed*100
        self._productive_time_fraction = self._info[4]/self._info_summed*100
        self._exercise_fraction = self._info[5]/self._info_summed*100
        self._screen_time_fraction = self._info[6]/self._info_summed*100

        self._pie_v = [self._sleep_fraction, self._outside_timefraction,
                       self._productive_time_fraction, self._exercise_fraction, self._screen_time_fraction]

        self._col_v = ["red", "blue", "orange", "green", "black"]
        self._create_piechart(self._pie_v, self._col_v)

        self._frame.pack()

    def _create_piechart(self, pie_v, col_v):
        """create a piechart for the user info"""
        st = 0  # Start angle for the first segment
        coord = 100, 100, 300, 300  # The bounding coordinates of the pie chart
        activity_labels = [f"Sleep {self._info[2]/60} hours", f"Outside {self._info[3]/60} hours",
                           f"Productive {self._info[4]/60} hours", f"Exercise {self._info[5]/60} hours",
                           f"Screen Time {self._info[6]/60} hours"]

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

            # Create the text with a contrasting color, say white
            self._canvas.create_text(text_x, text_y, text=label, fill="white")

            # Optionally, draw a line from the text to the slice
            line_end_x = center_x + radius * 0.5 * math.cos(angle_rad)
            line_end_y = center_y - radius * 0.5 * math.sin(angle_rad)
            self._canvas.create_line(
                text_x, text_y, line_end_x, line_end_y, fill="white")

            # Update the start angle for the next slice
            st += extent
            # generöity koodi loppuu

    def _display_info(self):
        """displaying information"""
        self._age_label = tk.Label(self._frame, text=f"Age: {self._info[0]}")
        self._age_label.pack()

        self._gender_label = tk.Label(
            self._frame, text=f"Gender: {self._info[1]}")
        self._gender_label.pack()

        self._sleep_label = tk.Label(
            self._frame, text=f"Sleep goal: {self._info[2]/60} hours")
        self._sleep_label.pack()

        self._exericse_label = tk.Label(
            self._frame, text=f"Exercise goal: {self._info[3]/60} hours")
        self._exericse_label.pack()

        self._outside_label = tk.Label(
            self._frame, text=f"Outside goal: {self._info[4]/60} hours")
        self._outside_label.pack()

        self._productive_label = tk.Label(
            self._frame, text=f"Productive goal: {self._info[5]/60} hours")
        self._productive_label.pack()

        self._screentime_label = tk.Label(
            self._frame, text=f"Screentime goal: {self._info[6]/60} hours")
        self._screentime_label.pack()

    def _goto_todayview(self):
        """going to todayview button. Need to import here to avoid cross import"""
        # pylint: disable=import-outside-toplevel
        from ui.today_view import TodayView
        self._frame.destroy()
        self._canvas.destroy()
        TodayView(self._master,
                  self._user_id,
                  self._user_service,
                  self._daily_plan_service)
