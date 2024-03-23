import tkinter as tk

""""Testi dailyplannerview näyttämiseen."""
class DailyPlannerView:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.username_label = tk.Label(self.frame, text="You are now logged in")
        self.username_label.pack()

        self.frame.pack()