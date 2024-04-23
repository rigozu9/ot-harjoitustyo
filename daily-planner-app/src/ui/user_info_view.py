import tkinter as tk
from tkinter import Canvas
import math

class UserInfoView:
    """here you can see your own information"""
    def __init__(self, master, user_id, user_service, daily_plan_service):
        self._master = master
        self._user_id = user_id

        # Define colors for the pie chart
        self._col_v = ["red", "blue", "orange", "green", "black"]

        # Central frame for information and goals
        self._info_frame = tk.Frame(self._master)
        self._info_frame.pack(side=tk.TOP, fill=tk.BOTH)

        # Frame for pie charts
        self._chart_frame = tk.Frame(self._master)
        self._chart_frame.pack(side=tk.TOP, fill=tk.BOTH)

        # Configure canvases for the pie charts
        self._canvas = Canvas(self._chart_frame, width=350, height=350)
        self._canvas.pack(side=tk.LEFT, padx=40)

        self._avg_canvas = Canvas(self._chart_frame, width=350, height=350)
        self._avg_canvas.pack(side=tk.LEFT, padx=40)

        self._user_service = user_service
        self._daily_plan_service = daily_plan_service
        self._all_plans = self._daily_plan_service.calculate_average_attributes(self._user_id)
        self._username = self._user_service.get_username(self._user_id)

        self._welcome_label = tk.Label(
            self._info_frame, text=f"{self._username}'s information and goals", font=('Arial', 18))
        self._welcome_label.pack()

        self._goto_dailyplanner_button = tk.Button(
            self._info_frame, text="Today's view", command=self._goto_todayview)
        self._goto_dailyplanner_button.pack()

        self._info = self._user_service.show_info(self._user_id)
        self._display_info()

        self._info_summed = sum(self._info[2:7])
        self._create_piechart(self._info[2:7], self._canvas, "goal")
        self._create_piechart([self._all_plans['avg_sleep'], self._all_plans['avg_outside_time'],
                                self._all_plans['avg_productive_time'], self._all_plans['avg_exercise'],
                                self._all_plans['avg_screen_time']], self._avg_canvas, "avg")

    #generöity koodi alkaa
    def _create_piechart(self, values, canvas, chart_type):
        """create a piechart for the user info"""
        st = 0 
        coord = 110, 110, 250, 250
        if chart_type == "goal":
            activity_labels = [f"Sleep {values[0]/60:.1f} hours", f"Outside {values[1]/60:.1f} hours",
                               f"Productive {values[2]/60:.1f} hours", f"Exercise {values[3]/60:.1f} hours",
                               f"Screen Time {values[4]/60:.1f} hours"]
            values_summed = sum(values)
        else:
            activity_labels = [f"Avg Sleep {values[0]/60:.1f} hours", f"Avg Outside {values[1]/60:.1f} hours",
                               f"Avg Productive {values[2]/60:.1f} hours", f"Avg Exercise {values[3]/60:.1f} hours",
                               f"Avg Screen Time {values[4]/60:.1f} hours"]
            values_summed = sum(values)

        for val, col, label in zip(values, self._col_v, activity_labels):
            extent = (val / values_summed) * 360  # Calculate extent as a percentage of 360 degrees
            self._draw_pie_slice(canvas, coord, st, extent, col, label)
            st += extent  # Update the start angle for the next slice

    def _draw_pie_slice(self, canvas, coord, start, extent, fill_color, label):
        # Draw the arc (a slice of the pie chart)
        canvas.create_arc(coord, start=start, extent=extent, fill=fill_color, outline=fill_color)

        # Calculate the angle in the middle of the slice for text placement
        mid_angle = start + extent / 2
        angle_rad = math.radians(mid_angle)
        
        center_x = (coord[0] + coord[2]) / 2
        center_y = (coord[1] + coord[3]) / 2
        radius = (coord[2] - coord[0]) / 2
        text_offset = radius * 1.5
        
        # Text coordinates
        text_x = center_x + text_offset * math.cos(angle_rad)
        text_y = center_y - text_offset * math.sin(angle_rad)
        
        # Line end coordinates (on the pie slice)
        line_end_x = center_x + radius * math.cos(angle_rad) + 10
        line_end_y = center_y - radius * math.sin(angle_rad) + 10
        
        # Create the text
        canvas.create_text(text_x, text_y, text=label, fill="magenta")

        # Draw the line
        canvas.create_line(text_x, text_y, line_end_x, line_end_y, fill="white")
    #generöity koodi loppuu

    def _display_info(self):
        """displaying information in the info frame"""
        info_labels = [
            f"Age: {self._info[0]}",
            f"Gender: {self._info[1]}",
            f"Sleep goal: {self._info[2] / 60:.1f} hours",
            f"Average sleep: {self._all_plans['avg_sleep'] / 60:.1f} hours",
            f"Exercise goal: {self._info[3] / 60:.1f} hours",
            f"Average exercise time: {self._all_plans['avg_exercise'] / 60:.1f} hours",
            f"Outside goal: {self._info[4] / 60:.1f} hours",
            f"Average outside time: {self._all_plans['avg_outside_time'] / 60:.1f} hours",
            f"Productive goal: {self._info[5] / 60:.1f} hours",
            f"Average productive time: {self._all_plans['avg_productive_time'] / 60:.1f} hours",
            f"Screentime goal: {self._info[6] / 60:.1f} hours",
            f"Average screentime: {self._all_plans['avg_screen_time'] / 60:.1f} hours",
        ]
        for text in info_labels:
            self._create_and_pack_label(text, self._info_frame)

    def _create_and_pack_label(self, text, frame):
        """Helper function to create a label with the specified text and pack it into the given frame."""
        label = tk.Label(frame, text=text)
        label.pack()

    def _goto_todayview(self):
        """going to todayview button. Need to import here to avoid cross import"""
        # pylint: disable=import-outside-toplevel
        from ui.today_view import TodayView
        self._info_frame.destroy()
        self._chart_frame.destroy()
        self._canvas.destroy()
        self._avg_canvas.destroy()
        TodayView(self._master, self._user_id, self._user_service, self._daily_plan_service)
