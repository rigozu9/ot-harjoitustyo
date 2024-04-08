import tkinter as tk

#Daily planner view for the application
class SurveyView:
    def __init__(self, master, user_id, user_service, daily_planner_service, survey_service):
        self._master = master
        self._user_id = user_id

        self._frame = tk.Frame(self._master)
        self._user_service = user_service
        self._daily_planner_service = daily_planner_service
        self._survey_service = survey_service
        self._username = self._user_service.get_username(self._user_id)

        self._user_service.complete_first_login(user_id)
        
        self._welcome_label = tk.Label(self._frame, text=f"Welcome, {self._username} answer this survey to get started", font=('Arial', 18))
        self._welcome_label.pack()

        self._age = tk.Label(self._frame, text="Age:")
        self._age.pack()
        self._age_entry = tk.Entry(self._frame)
        self._age_entry.pack()

        self._sex = tk.Label(self._frame, text="Sex:")
        self._sex.pack()
        self._sex_entry = tk.Entry(self._frame)
        self._sex_entry.pack()

        self._sleep = tk.Label(self._frame, text="How many hours in average do you sleep in a night:")
        self._sleep.pack()
        self._sleep_entry = tk.Entry(self._frame)
        self._sleep_entry.pack()

        self._submit_button = tk.Button(self._frame, text="Submit", command=self._submit)
        self._submit_button.pack()

        self._frame.pack()

    def _submit(self):
        age = self._age_entry.get()
        sex = self._sex_entry.get()
        sleep = self._sleep_entry.get()

        self._user_service.add_info(age, sex, sleep, self._user_id)