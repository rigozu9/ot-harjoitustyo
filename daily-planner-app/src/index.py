"""tkInterin alustaminen, joka kutsuu ui.ui UI luokkaa"""
from tkinter import Tk
from ui.ui import UI
from database_connection import init_db, Session
from repositories.user_repository import UserRepository
from repositories.activity_repository import ActivityRepository
from services.user_service import UserService
from services.daily_planner_service import DailyPlannerService

def on_app_exit():
    Session.remove()  # Close the session

def main():
    init_db()

    user_repository = UserRepository(Session())
    activity_repository = ActivityRepository(Session())
    user_service = UserService(user_repository)
    daily_planner_service = DailyPlannerService(activity_repository)

    window = Tk()
    window.title("Daily Planner application")
    window.geometry("600x400") 

    ui_view = UI(window, user_service, daily_planner_service)
    ui_view.start()

    window.mainloop()
    window.protocol("WM_DELETE_WINDOW", on_app_exit)

if __name__ == "__main__":
    main()