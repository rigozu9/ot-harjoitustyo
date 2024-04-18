"""tkinter import"""
import tkinter as tk

class UserInfoView:
    """here you can see your own information"""
    def __init__(self, master, user_id, user_service, daily_plan_service):
        self._master = master
        self._user_id = user_id

        self._frame = tk.Frame(self._master)
        self._user_service = user_service
        self._daily_plan_service = daily_plan_service

        self._username = self._user_service.get_username(self._user_id)

        self._welcome_label = tk.Label(
            self._frame, text=f"{self._username}'s information and goals", font=('Arial', 18))
        self._welcome_label.pack()

        self._goto_dailyplanner_button = tk.Button(
            self._frame, text="Home", command=self._goto_dailyplanner)
        self._goto_dailyplanner_button.pack()

        self._display_info()

        self._frame.pack()

    def _display_info(self):
        """displaying information"""
        info = self._user_service.show_info(self._user_id)

        self._age_label = tk.Label(self._frame, text=f"Age: {info[0]}")
        self._age_label.pack()

        self._gender_label = tk.Label(self._frame, text=f"Gender: {info[1]}")
        self._gender_label.pack()

        self._sleep_label = tk.Label(self._frame, text=f"Sleep goal: {info[2]/60} hours")
        self._sleep_label.pack()

        self._exericse_label = tk.Label(self._frame, text=f"Exercise goal: {info[3]/60} hours")
        self._exericse_label.pack()

        self._outside_label = tk.Label(self._frame, text=f"Outside goal: {info[4]/60} hours")
        self._outside_label.pack()

        self._productive_label = tk.Label(self._frame, text=f"Productive goal: {info[5]/60} hours")
        self._productive_label.pack()

        self._screentime_label = tk.Label(self._frame, text=f"Screentime goal: {info[6]/60} hours")
        self._screentime_label.pack()

    def _goto_dailyplanner(self):
        """going to dailyplanner button. Need to import here to avoid cross import"""
        # pylint: disable=import-outside-toplevel
        from ui.daily_planner_view import DailyPlanner
        self._frame.destroy()
        DailyPlanner(self._master,
                     self._user_id,
                     self._user_service,
                     self._daily_plan_service)
