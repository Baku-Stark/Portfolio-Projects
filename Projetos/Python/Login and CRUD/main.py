# IMPORT os
import os

# IMPORT[sqlite3]
import sqlite3 as lite

# IMPORT [pip install rich]
from rich import print as rprint

# IMPORT [pip3 install customtkinter]
import customtkinter

# IMPORT [functions > *]
from functions.system import MainForm
from functions.manage import Manage

class MainApp(MainForm):
    def __init__(self):
        # self.color_title = (ligth-mode, dark-mode)
        self.color_title = ("#0E2F73", "#00C8FA")
        self.color_letter = ("#111111", "#f0f8ff")
        self.themePattern = ("#CFCFCF", "#333333")
        self.themePattern2 = ("#86848c", "#111111")
        self.color_success = "#22ca4b"
        self.color_warning = "#ff4336"

        self.connection = lite.connect('database/accounts.db')

        try:
            cur = self.connection.cursor()
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS accounts(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user TEXT,
                    password TEXT,
                    email TEXT
                )
                """
            )

            status_title = "[VALID]"
            status_message = "[bold green]SQLite 3[/bold green] Banco de Dados (accounts) criado com sucesso!"
            rprint(f'[on white] [black] {status_title} [/black] [/on white][on blue] [bold]{status_message}[/bold] [/on blue]')
        
        except (Exception, AttributeError) as e:
            status_title = "[ERROR]"
            status_message = f"[orange]SQLite 3[/orange] {e}"
            rprint(f'[on white] [black] {status_title} [/black] [/on white][on red] [bold]{status_message}[/bold] [/on red]')

        self.theme = "Light"
        self.root = customtkinter.CTk()
        self.windowApp()
        self.theme_widgets()
        self.theme_function()

        # Class [LOGIN REGISTER]
        self.framesForm()
        self.loginForm()

        # Class [Manage]
        # self.frameManage()
        # self.MenuManage()

        # start app
        self.root.mainloop()

    def windowApp(self):
        self.root.title("LOGIN | REGISTRO")
        self.root.geometry("1200x650")
        self.root.iconbitmap('img/ciberespaco.ico')
        self.root.resizable(width='false', height='false')
    
    def theme_function(self):
        if self.theme == "Light":
            self.theme_btn.configure(text="Light Mode")
            self.theme = "Dark"
            customtkinter.set_appearance_mode(self.theme)
        
        else:
            self.theme_btn.configure(text="Dark Mode")
            self.theme = "Light"
            customtkinter.set_appearance_mode(self.theme)

    def theme_widgets(self):
        self.theme_btn = customtkinter.CTkButton(
            self.root, text="Light Mode", font=('Impact', 15), text_color=("#111111", "#f0f8ff"),
            fg_color=("#ABABAB", "#111111"), hover_color=("#D9D9D9", "#000000")
        )
        self.theme_btn.configure(command=self.theme_function)

        self.theme_btn.place(relx=0.01, rely=0.01)



if __name__ == '__main__':
    os.system('cls')

    status_title = "[ON-MODE]"
    status_message = "[bold green]CustomTkinter[/bold green] application successfully created!"
    rprint(f'[on white] [black] {status_title} [/black] [/on white][on blue] [bold]{status_message}[/bold] [/on blue]')

    MainApp()