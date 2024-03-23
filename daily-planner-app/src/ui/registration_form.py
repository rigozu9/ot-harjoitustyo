import tkinter as tk
from services.user_service import register_user
from ui.login_form import LoginForm

""""Rekisteröitymisen form. Kysyy nimeä ja salasanaa.
    Käyttää user_service, kun kirjatuu. 
    Nappi myös kirjatumiselle, jos on jo käyttäjä """

class RegistrationForm:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.username_label = tk.Label(self.frame, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.pack()

        self.password_label = tk.Label(self.frame, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.pack()

        self.register_button = tk.Button(self.frame, text="Register", command=self._register)
        self.register_button.pack()

        self.goto_login_button = tk.Button(self.frame, text="Go to Login", command=self.go_to_login)
        self.goto_login_button.pack()


        self.frame.pack()

    def _register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if register_user(username, password):
            self.frame.destroy()
            LoginForm(self.master) 
        else:
            pass

    def go_to_login(self):
        self.frame.destroy()
        LoginForm(self.master) 