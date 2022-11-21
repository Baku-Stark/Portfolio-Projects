# ===============================================
# IMPORTAÇÕES [Tkinter]
from tkinter import *
from tkinter import tix
from tkinter import messagebox

# IMPORTAÇÕES [datetime]
from datetime import *

# IMPORTAÇÕES [pygame]
import pygame
from pygame import mixer

# ===============================================
# CONFIGURAÇÃO [CORES]
lightBlack = "#111111"
aliceBlue = "#f0f8ff"
lemonGreen = "#35FF1E"
freshRed = "#AA202D"

# ===============================================
# CONFIGURAÇÃO [APLICAÇÃO]
class Functions():
    def hours(self):
        date_now = datetime.now()
        dia = date_now.day
        mes = date_now.month
        ano = date_now.year
        horas = date_now.strftime('%H:%M')

        self.horas.config(text=horas)
        self.horas.after(200, self.hours)
        self.date['text'] = f"{dia}/{mes}/{ano}"
        
    def saveHorario(self):
        self.situation_situa['fg'] = lemonGreen
        self.situation_situa['text'] = "Ativado!"
    
    def consult(self):
        self.root_consult = Toplevel()
        self.root_consult.grab_set()
        self.root_consult.focus_force()
        self.root_consult.geometry("400x200")
        self.root_consult.transient(self.root)
        self.root_consult.title("Horários")
        self.root_consult.resizable(width='false', height='false')

        self.root_frame = Frame(self.root_consult, bg=lightBlack)
        self.border = Frame(self.root_frame, bg=aliceBlue)
        self.container = Frame(self.border, bg=lightBlack)

        self.label_horario = Label(
            self.container, text="00:00", font=('Impact 20'),
            bg=lightBlack, fg=aliceBlue, bd=0
        )

        # CONFIGURAÇÃO [PLACE]
        self.root_frame.place(relwidth=1, relheight=1)
        self.border.place(relx=0, rely=0.01, relwidth=1, relheight=0.4)
        self.container.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
        self.label_horario.place(relx=0.02, rely=0.01)

class Alarm(Functions):
    def __init__(self):
        self.root = tix.Tk()
        self.telaApp()
        self.menuBar()
        self.framesApp()
        self.buttons()
        self.contentLeft()
        self.contentRight()
        # ------------------
        self.hours()
        self.root.mainloop()

    def telaApp(self):
        self.root.title("Alarme - Despertador")
        self.root.geometry("500x300")
        self.root.resizable(width='false', height='false')
        self.root.iconbitmap("icon/alarm-bell.ico")

    def menuBar(self):
        self.menubar = Menu(self.root)
        self.file_menu = Menu(self.menubar)
        self.root.config(menu=self.menubar)
        self.menubar.add_cascade(label="Alarmes Definidos", menu=self.file_menu)
        self.file_menu.add_command(label="Horários", command=self.consult)

    def framesApp(self):
        self.frameLeft = Frame(self.root, bg=aliceBlue)

        self.frameRight = Frame(self.root, bg=lightBlack)

        # CONFIGURAÇÃO [PLACE > FRAMES]
        self.frameLeft.place(relx=0, rely=0, relheight=1, relwidth=0.5)
        self.frameRight.place(relx=0.5, rely=0, relheight=1, relwidth=0.5)
        
    def buttons(self):
        self.btn_save = tix.Button(
            self.frameLeft, text="Salvar", font='Arial 10 bold', bg=lightBlack, fg=aliceBlue,
            relief='raised', overrelief='ridge'
        )
        self.btn_save['command'] = self.saveHorario
        self.save_ballon = tix.Balloon(self.frameLeft)
        self.save_ballon.bind_widget(self.btn_save, balloonmsg="Definir horário para o alarme.")

        # CONFIGURAÇÃO [PLACE > Botões]
        self.btn_save.place(relx=0.01, rely=0.85)

    def contentLeft(self):
        self.label_horas = Label(
            self.frameLeft, text="Definir horas*",
            font=('Arial 10'), bg=aliceBlue, fg=lightBlack
        )

        # CONFIGURAÇÃO [PLACE]
        self.label_horas.place(relx=0.01, rely=0.01)

    def contentRight(self):
        self.horas = Label(
            self.frameRight, text="00:00", font=('Impact 13'), bg=lightBlack, fg=aliceBlue
        )

        self.date = Label(
            self.frameRight, text="--/--/--", font=('Impact 13'), bg=lightBlack, fg=aliceBlue
        )

        self.situation_title = Label(
            self.frameRight, text="Alarme:", font=('Impact 13'),
            bg=lightBlack, fg=aliceBlue
        )
        self.situation_situa = Label(
            self.frameRight, text="Desativado!", font=('Impact 13'),
            bg=lightBlack, fg=freshRed
        )

        # CONFIGURAÇÃO [PLACE > LABEL]
        self.horas.place(relx=0.8, rely=0)
        self.date.place(relx=0.02, rely=0)
        self.situation_title.place(relx=0.07, rely=0.7)
        self.situation_situa.place(relx=0.35, rely=0.7)

# ===============================================
# CONFIGURAÇÃO [APLICAÇÃO > ATIVAÇÃO]
if __name__ == '__main__':
    Alarm()