"""importing tkinter, messagebox and ttk. Also the dailyplanner"""
import tkinter as tk
from tkinter import messagebox, ttk
from ui.daily_planner_view import DailyPlanner

class SurveyView:
    """Daily planner view for the application"""
    def __init__(self, master, user_id, user_service, daily_plan_service):
        self._master = master
        self._user_id = user_id

        self._frame = tk.Frame(self._master)
        self._user_service = user_service
        self._daily_plan_service = daily_plan_service
        self._username = self._user_service.get_username(self._user_id)

        self._user_service.complete_first_login(user_id)

        self._welcome_label = tk.Label(
            self._frame, text=f"Welcome, {self._username} answer this survey to get started", font=('Arial', 16))
        self._welcome_label.pack()

        self._age = tk.Label(self._frame, text="Age:")
        self._age.pack()
        # generöity koodi alkaa
        self._age_entry = tk.Spinbox(self._frame, from_=0, to=120, wrap=True)
        self._age_entry.pack()

        self._sex = tk.Label(self._frame, text="Sex:")
        self._sex.pack()

        self._sex_var = tk.StringVar()
        self._sex_entry = ttk.Combobox(
            self._frame, textvariable=self._sex_var, state="readonly", values=['Male', 'Female', 'Other'])
        self._sex_entry.pack()

        self._goal_label = tk.Label(
            self._frame, text="What are your goals?", font=('Arial', 16))
        self._goal_label.pack()

        #generöity koodi alkaa
        self._create_time_entry("Sleep", "How many hours and minutes dou you want to sleep a night?")
        # Outside time
        self._create_time_entry("Outside", "How many hours and minutes would you like to spend outside a day?")
        # Productive time
        self._create_time_entry("Productive", "How many hours and minutes would you like to spend productive things (work, school, etc.)?")
        # Exercise time
        self._create_time_entry("Exercise", "How many hours and minutes would you like to exercise a day?")
        # Screentime
        self._create_time_entry("Screen", "What would you like your screentime to be a day?")
        #generöity koodi loppuu

        self._submit_button = tk.Button(
            self._frame, text="Submit", command=self._submit)
        self._submit_button.pack()

        self._frame.pack()

    def _create_time_entry(self, activity_name, label_text):
        """
        Helper method to create hour and minute entries for an activity.
        """
        setattr(self, f"_{activity_name.lower()}_label", tk.Label(self._frame, text=label_text))
        getattr(self, f"_{activity_name.lower()}_label").pack()

        time_frame = tk.Frame(self._frame)
        time_frame.pack()

        setattr(self, f"_{activity_name.lower()}_hours_entry", tk.Entry(time_frame, width=5))
        getattr(self, f"_{activity_name.lower()}_hours_entry").pack(side=tk.LEFT)
        tk.Label(time_frame, text="hours").pack(side=tk.LEFT)

        setattr(self, f"_{activity_name.lower()}_minutes_entry", tk.Entry(time_frame, width=5))
        getattr(self, f"_{activity_name.lower()}_minutes_entry").pack(side=tk.LEFT)
        tk.Label(time_frame, text="minutes").pack(side=tk.LEFT)

    #generöity koodi alkaa
    def _submit(self):
        """Submit the information with validation for new time inputs."""
        try:
            age = int(self._age_entry.get())
            sex = self._sex_var.get()

            # Helper function to calculate total minutes from hours and minutes entries
            def get_total_minutes(activity_name):
                hours = int(getattr(self, f"_{activity_name.lower()}_hours_entry").get())
                minutes = int(getattr(self, f"_{activity_name.lower()}_minutes_entry").get())
                if not (0 <= hours <= 24 and 0 <= minutes < 60):
                    raise ValueError(f"{activity_name} time must be a valid time of day.")
                return hours * 60 + minutes
            
            # Calculate total minutes for all activities
            total_sleep_minutes = get_total_minutes("Sleep")
            total_outside_minutes = get_total_minutes("Outside")
            total_productive_minutes = get_total_minutes("Productive")
            total_exercise_minutes = get_total_minutes("Exercise")
            total_screen_minutes = get_total_minutes("Screen")

            # Validate all fields are filled
            if not all([age, sex, total_sleep_minutes, total_exercise_minutes,
                        total_outside_minutes, total_productive_minutes, total_screen_minutes]):
                messagebox.showerror("Error", "All fields are required and must be valid numbers!")
                return

            # Assuming your user_service.add_info method can handle these new parameters
            self._user_service.add_info(age, sex, total_sleep_minutes, total_exercise_minutes,
                                        total_outside_minutes, total_productive_minutes, total_screen_minutes, self._user_id)

            messagebox.showinfo("Success", "Your information has been submitted successfully!")
            self._frame.destroy()
            DailyPlanner(self._master, self._user_id, self._user_service, self._daily_plan_service)

        except ValueError as e:
            messagebox.showerror("Submission Error", str(e))

        #generöity koodi loppuu

