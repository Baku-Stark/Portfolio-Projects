# IMPORT [webbrowser]
import webbrowser

# IMPORT [tkinter]
from tkinter import *
from tkinter import CENTER

# IMPORT [pip3 install customtkinter]
import customtkinter

class Manage():
    def autor(self):
        gitHub = "https://github.com/Baku-Stark"
        webbrowser.open_new(gitHub)

    def project(self):
        gitHub = "https://github.com/Baku-Stark/Portfolio-Projects/tree/main/Projetos/Python/Login%20and%20CRUD"
        webbrowser.open_new(gitHub)
    
    def returnLogin(self):
        # ===================================================
        # destruir os blocos da aplicação
        # ================= DESTROY
        self.menu_bar.destroy()
        self.frameCENTER_MANAGE.destroy()

        # ===================================================
        # construir os blocos da aplicação
        # ================= ENGINE
        self.root.title("LOGIN | REGISTRO")
        self.framesForm()
        self.loginForm()

    def MenuManage(self):
        if self.GlobalUser == "admin":
            self.root.title(f"Servidor Administrativo")

        else:
            self.root.title(f"Welcome {self.GlobalUser}")

        self.menu_bar = Menu(self.root)
        self.root.configure(menu=self.menu_bar)

        self.Conta = Menu(self.menu_bar)
        self.Sobre = Menu(self.menu_bar)


        self.menu_bar.add_cascade(label=self.GlobalUser, menu=self.Conta)
        self.Conta.add_command(label="LOGOUT", command=self.returnLogin)

        self.menu_bar.add_cascade(label="Informações", menu=self.Sobre)
        self.Sobre.add_command(label="Autor do projeto", command=self.autor)
        self.Sobre.add_command(label="Sobre o projeto", command=self.project)

    def frameManage(self):
        self.frameCENTER_MANAGE = customtkinter.CTkFrame(
            self.root, fg_color=self.themePattern
        )

        self.frameLEFT_MANAGE = customtkinter.CTkFrame(self.frameCENTER_MANAGE, fg_color=self.themePattern2)
        self.frameRIGHT_MANAGE = customtkinter.CTkFrame(self.frameCENTER_MANAGE, fg_color=self.themePattern2)

        self.frameCENTER_MANAGE.place(relx=0.5, rely=0.53, relwidth=0.99, relheight=0.9, anchor=CENTER)
        self.frameLEFT_MANAGE.place(relx=0.005, rely=0.015,relwidth=0.65, relheight=0.97)
        self.frameRIGHT_MANAGE.place(relx=0.695, rely=0.015,relwidth=0.3, relheight=0.97)

    def widgets_frameLEFT_MANAGE(self):
        self.label_manageUSER = customtkinter.CTkLabel(
            self.frameLEFT_MANAGE, text=""
        )