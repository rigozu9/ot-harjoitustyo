import tkinter as tk

#Daily planner view for the application
class DailyPlanner:
    def __init__(self, master, user_id, user_service, daily_planner_service):
        self._master = master
        self._user_id = user_id
        self._activity_frames = []

        self._frame = tk.Frame(self._master)
        self._user_service = user_service
        self._daily_planner_service = daily_planner_service
        self._username = self._user_service.get_username(self._user_id)

        self._welcome_label = tk.Label(self._frame, text=f"Welcome, {self._username} ", font=('Arial', 18))
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
            self._daily_planner_service.create_activity(activity_description, self._user_id)
            self._display_activities()

    def _display_activities(self):
        # Clear existing activity frames
        for frame in self._activity_frames:
            frame.destroy()
        self._activity_frames.clear()  # Reset the list after clearing frames

        activities = self._daily_planner_service.show_activities(self._user_id)
        for activity in activities:
            activity_frame = tk.Frame(self._frame)
            self._activity_frames.append(activity_frame)
            activity_frame.pack()

            activity_label = tk.Label(activity_frame, text=activity.description)
            activity_label.pack(side=tk.LEFT)

            remove_button = tk.Button(activity_frame, text="Remove", command=lambda activity_id=activity.id: self._remove_activity(activity_id))
            remove_button.pack(side=tk.RIGHT)

    def _remove_activity(self, activity_id):
        self._daily_planner_service.remove_activity(activity_id)
        self._display_activities()