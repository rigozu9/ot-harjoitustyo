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

        #sleep time
        self._sleep_label = tk.Label(self._frame, text="How many hours and minutes would you like to sleep a night?:")
        self._sleep_label.pack()

        self._sleep_time_frame = tk.Frame(self._frame)
        self._sleep_time_frame.pack()

        self._sleep_hours_entry = tk.Entry(self._sleep_time_frame, width=5)
        self._sleep_hours_entry.pack(side=tk.LEFT)
        tk.Label(self._sleep_time_frame, text="hours").pack(side=tk.LEFT)

        self._sleep_minutes_entry = tk.Entry(self._sleep_time_frame, width=5)
        self._sleep_minutes_entry.pack(side=tk.LEFT)
        tk.Label(self._sleep_time_frame, text="minutes").pack(side=tk.LEFT)

        #exercise time
        self._exercise_label = tk.Label(self._frame, text="How many hours and minutes would you like to exercise in a day?:")
        self._exercise_label.pack()

        self._exercise_time_frame = tk.Frame(self._frame)
        self._exercise_time_frame.pack()

        self._exercise_hours_entry = tk.Entry(self._exercise_time_frame, width=5)
        self._exercise_hours_entry.pack(side=tk.LEFT)
        tk.Label(self._exercise_time_frame, text="hours").pack(side=tk.LEFT)

        self._exercise_minutes_entry = tk.Entry(self._exercise_time_frame, width=5)
        self._exercise_minutes_entry.pack(side=tk.LEFT)
        tk.Label(self._exercise_time_frame, text="minutes").pack(side=tk.LEFT)
        #generöity kooodi loppuu

        #outside time
        self._outside_label = tk.Label(self._frame, text="How many hours and minutes would you like to spend outside?:")
        self._outside_label.pack()

        self._outside_time_frame = tk.Frame(self._frame)
        self._outside_time_frame.pack()

        self._outside_hours_entry = tk.Entry(self._outside_time_frame, width=5)
        self._outside_hours_entry.pack(side=tk.LEFT)
        tk.Label(self._outside_time_frame, text="hours").pack(side=tk.LEFT)

        self._outside_minutes_entry = tk.Entry(self._outside_time_frame, width=5)
        self._outside_minutes_entry.pack(side=tk.LEFT)
        tk.Label(self._outside_time_frame, text="minutes").pack(side=tk.LEFT)

        #productive things
        self._productive_label = tk.Label(self._frame, text="How many hours and minutes would you like to spend doing productive things?:")
        self._productive_label.pack()

        self._productive_time_frame = tk.Frame(self._frame)
        self._productive_time_frame.pack()

        self._productive_hours_entry = tk.Entry(self._productive_time_frame, width=5)
        self._productive_hours_entry.pack(side=tk.LEFT)
        tk.Label(self._productive_time_frame, text="hours").pack(side=tk.LEFT)

        self._productive_minutes_entry = tk.Entry(self._productive_time_frame, width=5)
        self._productive_minutes_entry.pack(side=tk.LEFT)
        tk.Label(self._productive_time_frame, text="minutes").pack(side=tk.LEFT)

        #screentime
        self._screentime_label = tk.Label(self._frame, text="How many hours and minutes of screentime would you like to have?:")
        self._screentime_label.pack()

        self._screen_time_frame = tk.Frame(self._frame)
        self._screen_time_frame.pack()

        self._screen_hours_entry = tk.Entry(self._screen_time_frame, width=5)
        self._screen_hours_entry.pack(side=tk.LEFT)
        tk.Label(self._screen_time_frame, text="hours").pack(side=tk.LEFT)

        self._screen_minutes_entry = tk.Entry(self._screen_time_frame, width=5)
        self._screen_minutes_entry.pack(side=tk.LEFT)
        tk.Label(self._screen_time_frame, text="minutes").pack(side=tk.LEFT)

        self._submit_button = tk.Button(
            self._frame, text="Submit", command=self._submit)
        self._submit_button.pack()

        self._frame.pack()

    #generöity koodi alkaa
    def _submit(self):
        """Submit the information with validation for new time inputs."""
        try:
            age = int(self._age_entry.get())
            sex = self._sex_var.get()

            # Helper function to calculate total minutes from hours and minutes
            def get_total_minutes(hours_entry, minutes_entry):
                hours = int(hours_entry.get())
                minutes = int(minutes_entry.get())
                if not (0 <= hours <= 24 and 0 <= minutes < 60):
                    raise ValueError(f"Time must be a valid time of day for {hours_entry} and {minutes_entry}.")
                return hours * 60 + minutes

            # Calculate total minutes for all activities
            total_sleep_minutes = get_total_minutes(self._sleep_hours_entry, self._sleep_minutes_entry)
            total_exercise_minutes = get_total_minutes(self._exercise_hours_entry, self._exercise_minutes_entry)
            total_outside_minutes = get_total_minutes(self._outside_hours_entry, self._outside_minutes_entry)
            total_productive_minutes = get_total_minutes(self._productive_hours_entry, self._productive_minutes_entry)
            total_screen_minutes = get_total_minutes(self._screen_hours_entry, self._screen_minutes_entry)

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

