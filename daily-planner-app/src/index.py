from tkinter import Tk
from ui.ui import UI

"""tkInterin alustaminen, joka kutsuu ui.ui UI luokkaa"""
def main():
    window = Tk()
    window.title("Daily Planner application")

    window.geometry("600x400") 

    ui_view = UI(window)
    ui_view.start()


    window.mainloop()


if __name__ == "__main__":
    main()