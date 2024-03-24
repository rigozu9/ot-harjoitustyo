import tkinter as tk
from services.daily_planner_service import DailyPlannerService

#Daily planner view for the application
class DailyPlanner:
    def __init__(self, master, user_id):
        self._master = master
        self._user_id = user_id

        self._frame = tk.Frame(self._master)
        self._service = DailyPlannerService()
        self._username = self._service.get_username(self._user_id)

        self._welcome_label = tk.Label(self._frame, text=f"Welcome, {self._username['username']}", font=('Arial', 18))
        self._welcome_label.pack()

        self._activity_label = tk.Label(self._frame, text="Add new activity:")
        self._activity_label.pack()

        self._activity_entry = tk.Entry(self._frame, width=30)
        self._activity_entry.pack()

        self._submit_button = tk.Button(self._frame, text="Submit", command=self._submit)
        self._submit_button.pack()

        self._activities_label = tk.Label(self._frame, text="Your activities:")
        self._activities_label.pack()

        self._frame.pack()
        
        self._display_activities()
        
    def _submit(self):
        activity_description = self._activity_entry.get()
        if activity_description:
            self._service.add_activity(activity_description, self._user_id)
            print("Activity added successfully!")
            self._display_activities()

    def _display_activities(self):
        # Clear existing activities display
        for widget in self._frame.winfo_children():
            if isinstance(widget, tk.Label) and widget != self._activity_label and widget != self._activities_label and widget != self._welcome_label:
                widget.destroy()

        activities = self._service.show_activities(self._user_id)  # Use service to get activities
        for activity in activities:
            activity_label = tk.Label(self._frame, text=activity[1])
            activity_label.pack()