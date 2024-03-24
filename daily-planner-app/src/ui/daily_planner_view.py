import tkinter as tk
# Adjust this import to match the location and name of your service class
from services.daily_planner_service import DailyPlannerService


""""Testi dailyplanner näyttämiseen."""
class DailyPlanner:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.service = DailyPlannerService()

        label = tk.Label(self.frame, text="You are now logged in", font=('Arial', 18))
        label.pack()

        self.activity_label = tk.Label(self.frame, text="Add new activity:")
        self.activity_label.pack()
        self.activity_entry = tk.Entry(self.frame, width=30)
        self.activity_entry.pack()

        self.submit_button = tk.Button(self.frame, text="Submit", command=self._submit)
        self.submit_button.pack()

        self.activities_label = tk.Label(self.frame, text="Activities:")
        self.activities_label.pack()

        self.frame.pack()
        
        self.display_activities()
        
    def _submit(self):
        activity_description = self.activity_entry.get()
        if activity_description:
            self.service.add_activity(activity_description)  # Use service to add activity
            print("Activity added successfully!")
            self.display_activities()  # Refresh the displayed activities

    def display_activities(self):
        # Clear existing activities display
        for widget in self.frame.winfo_children():
            if isinstance(widget, tk.Label) and widget != self.activity_label and widget != self.activities_label:
                widget.destroy()

        activities = self.service.show_activities()  # Use service to get activities
        for activity in activities:
            activity_label = tk.Label(self.frame, text=activity[1])
            activity_label.pack()