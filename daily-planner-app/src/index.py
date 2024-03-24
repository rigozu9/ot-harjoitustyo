from tkinter import Tk
from ui.ui import UI
from ui.daily_planner_view import DailyPlanner

"""tkInterin alustaminen, joka kutsuu ui.ui UI luokkaa"""
def main():
    window = Tk()
    window.title("Daily Planner application")

    window.geometry("600x400") 

    ui_view = UI(window)
    ui_view.start()
    #DailyPlanner(window)

    window.mainloop()


if __name__ == "__main__":
    main()