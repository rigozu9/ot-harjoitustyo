"""importing tkinter, datetime and messagebox"""
import tkinter as tk

class AdvicePageView:
    """Daily planner view for the application"""
    def __init__(self, master, user_id, user_service, daily_plan_service, views):
        self._master = master
        self._user_id = user_id
    
        self._frame = tk.Frame(self._master)

        self._user_service = user_service
        self._daily_plan_service = daily_plan_service

        self._username = self._user_service.get_username(self._user_id)

        self._welcome_label = tk.Label(
            self._frame, text=f"Tailored daily habit improvements for {self._username}",
                                font=('Arial', 18))
        self._welcome_label.pack()

        self._goals_label = tk.Label(
            self._frame, text="Based on your goals:",
                                font=('Arial', 13))
        self._goals_label.pack()

        self._show_goals_improvements()

        self._welcome_label = tk.Label(
            self._frame, text="Based on your averages:",
                                font=('Arial', 13))
        self._welcome_label.pack()

        self._show_average_improvements()

        self._frame.pack()

    def _create_and_pack_label(self, text, frame):
        """
            Helper function to create a label with the 
            specified text and pack it into the given frame.
        """
        label = tk.Label(frame, text=text, anchor="w")
        label.pack(fill='x', padx=150)

    def _show_goals_improvements(self):
        goals = self._user_service.show_info(self._user_id)
        print("goal advice", self._user_service.get_advice(goals)[0])
        #print(goals)
        #{'age': 22, 'sex': 'Male', 'sleep_goal': 480, 'exercise_goal': 60,
        #'outside_goal': 60, 'productive_goal': 480, 'screen_goal': 360}

    def _show_average_improvements(self):
        averages = self._daily_plan_service.calculate_average_attributes(
            self._user_id)
        print("averages advice", self._user_service.get_advice(None, averages)[1])
        #print(all_plans)
        #prints:
        #{'avg_sleep': 471.42857142857144, 'avg_outside_time': 72.85714285714286,
        #'avg_productive_time': 248.57142857142858, 'avg_exercise': 47.142857142857146, 'avg_screen_time': 364.2857142857143}
