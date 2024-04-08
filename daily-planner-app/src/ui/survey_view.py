import tkinter as tk

#Daily planner view for the application
class SurveyView:
    def __init__(self, master, user_id, user_service, daily_planner_service):
        self._master = master
        self._user_id = user_id

        self._frame = tk.Frame(self._master)
        self._user_service = user_service
        self._daily_planner_service = daily_planner_service
        self._username = self._user_service.get_username(self._user_id)

        self._user_service.complete_first_login(user_id)
        
        self._welcome_label = tk.Label(self._frame, text=f"Welcome, {self._username} answer this survey to get started", font=('Arial', 18))
        self._welcome_label.pack()

        self._frame.pack()