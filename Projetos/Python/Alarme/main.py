# ===============================================
# IMPORTAÇÕES [Tkinter]
from tkinter import *
from tkinter import tix
from tkinter import messagebox

# IMPORTAÇÕES [pygame]
import pygame
from pygame import mixer

# IMPORTAÇÕES [datetime e time]
from datetime import *
from time import sleep

# IMPORTAÇÕES [imagens]
from PIL import Image, ImageTk

# ===============================================
# CONFIGURAÇÃO [CORES]
lightBlack = "#111111"
aliceBlue = "#f0f8ff"
lightGray = "#737373"
lemonGreen = "#35FF1E"
freshRed = "#AA202D"
check_in = "No-Check!"

# ===============================================
# CONFIGURAÇÃO [APLICAÇÃO]
class Functions():
    def horaAtual(self):
        self.date_now = datetime.now()
        self.hora_atual= self.date_now.strftime('%H:%M')

        # CONFIGURAÇÃO [LABEL - self.horas]
        self.horas.after(1000, self.horaAtual)
        self.horas['text'] = self.hora_atual

        dia = self.date_now.day
        mes = self.date_now.month
        ano = self.date_now.year
        self.date['text'] = f"{dia}/{mes}/{ano}"
        
    def saveHorario(self):
        self.semana_set = self.spin_semana.get()
        self.horas_set = int(self.spin_horas.get())
        self.minutos_set = int(self.spin_minutos.get())
        
        if self.semana_set not in self.semanas_list:
            messagebox.showerror(
                title="Semana Incorreta",
                message="A semana selecionada não está na lista."
            )
        
        elif self.horas_set > 23 or self.horas_set < 0:
            messagebox.showerror(
                title="Horário Incorreto",
                message="A hora selecionada está errada. Por favor, faça novamente."
            )
        
        elif self.minutos_set > 60 or self.minutos_set < 0:
            messagebox.showerror(
                title="Minuto Incorreto",
                message="A definição para o minuto está incorreta."
            )
        
        else:
            messagebox.showinfo(
                title="Alarme Definido",
                message="O alarme foi definido com sucesso!"
            )

            self.playAlarm()
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
    
        if self.horas_set < 10 and self.minutos_set < 10:
            self.label_horario['text'] = f"0{str(self.horas_set)}:0{str(self.minutos_set)}"
        elif self.horas_set < 10 and self.minutos_set > 10:
            self.label_horario['text'] = f"0{str(self.horas_set)}:{str(self.minutos_set)}"
        elif self.horas_set > 10 and self.minutos_set < 10:
            self.label_horario['text'] = f"{str(self.horas_set)}:0{str(self.minutos_set)}"
        else:
            self.label_horario['text'] = f"{str(self.horas_set)}:{str(self.minutos_set)}"
        
        self.label_semana = Label(
            self.container, text="Dia da semana", font=('Arial 8 italic'),
            bg=lightBlack, fg=lightGray, bd=0
        )
        self.label_semana['text'] = self.semana_set

        # CONFIGURAÇÃO [PLACE]
        self.root_frame.place(relwidth=1, relheight=1)
        self.border.place(relx=0, rely=0.01, relwidth=1, relheight=0.4)
        self.container.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
        self.label_horario.place(relx=0.02, rely=0.01)
        self.label_semana.place(relx=0.02, rely=0.45)

    def playAlarm(self):
        self.root.after(1000, self.playAlarm)
        try:
            self.hoursNow_set = self.date_now.strftime('%H:%M')
            self.alarmtime = f"{str(self.horas_set)}:{str(self.minutos_set)}"
            print(F'\033[40mAlarme não foi definido.\n Hora Definida: {self.hoursNow_set}\033[m')
            if self.hoursNow_set == self.alarmtime:
                mixer.music.load('alarm-music/alarm.wav')
                mixer.music.play()
        
        except AttributeError:
            print('\033[40mAlarme não foi definido.\033[m')
        

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
        self.horaAtual()
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
            font=('Arial 10 bold'), bg=aliceBlue, fg=lightBlack
        )
        self.spin_horas = Spinbox(
            self.frameLeft, from_=0, to=23, font=('Arial 13 bold')
        )

        self.label_minutos = Label(
            self.frameLeft, text="Definir minutos*",
            font=('Arial 10 bold'), bg=aliceBlue, fg=lightBlack
        )
        self.spin_minutos = Spinbox(
            self.frameLeft, from_=0, to=59, font=('Arial 13 bold')
        )

        self.bar_div = Label(
            self.frameLeft, bg=lightBlack
        )

        self.semanas_list = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo"]
        self.spin_semana = Spinbox(
            self.frameLeft, values=self.semanas_list, font=('Arial 15 bold')
        )

        # CONFIGURAÇÃO [PLACE]
        self.label_horas.place(relx=0.01, rely=0.04)
        self.spin_horas.place(relx=0.01, rely=0.10)
        self.label_minutos.place(relx=0.01, rely=0.25)
        self.spin_minutos.place(relx=0.01, rely=0.31)
        self.bar_div.place(relx=0, rely=0.46, relwidth=1, relheight=0)
        self.spin_semana.place(relx=0, rely=0.55, relwidth=1, relheight=0.25)

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

        self.img = Image.open('img/alarme.png')
        self.img = self.img.resize((130, 130))
        self.img = ImageTk.PhotoImage(self.img)
        self.set_image = Label(
            self.frameRight, image=self.img, bg=lightBlack
        )

        # CONFIGURAÇÃO [PLACE > LABEL]
        self.horas.place(relx=0.8, rely=0)
        self.date.place(relx=0.02, rely=0)
        self.situation_title.place(relx=0.22, rely=0.7)
        self.situation_situa.place(relx=0.45, rely=0.7)
        self.set_image.place(relx=0.25, rely=0.15)

# ===============================================
# CONFIGURAÇÃO [APLICAÇÃO > ATIVAÇÃO]
if __name__ == '__main__':
    mixer.init()
    Alarm()