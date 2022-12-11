# ============================================================
# TKinter
from tkinter import *

# ============================================================
# Importando uma fonte
import pyglet
pyglet.font.add_file("font/digital-7.ttf") #font=("digital-7 100")

# ============================================================
# Datetime
from datetime import datetime

# ============================================================
# APLICAÇÃO

Black = "#000"
lightBlack = "#111111"
lightBlue = "#1676DE"
iceBlue = "#19C1FA"

class time():
    def ClockHours(self):
        """
            Função de horas e data ATUAIS.

            Return:
                self.root.after(200, self.ClockHours) -> Função sendo chamada a cada 2 milésimos.
        """
        horaDateTime = datetime.now()

        # [Horário]
        horaAtual = horaDateTime.strftime("%H:%M:%S")
        self.labelClock['text'] = horaAtual
        
        # [Calendário]
        diaAtual = horaDateTime.day
        mesAtual = horaDateTime.month
        anoAtual = horaDateTime.year
        semanaSet = horaDateTime.weekday()
        semanaAtual = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-Feira', 'Sexta-feira', 'Sábado', 'Domingo']
        self.labelCalendario['text'] = f"{diaAtual}/{mesAtual}/{anoAtual}"
        self.labelDiaSemana['text'] = f"{semanaAtual[semanaSet]}"

        # -----
        self.root.after(200, self.ClockHours)

class AppClock(time):
    def __init__(self):
        """
            Função para armazenar as funções ativadas.

            Return:
                "root"    -> Janela
                rootMain()
                framesFunction()
                GadgetsClock()
                positionContent()
                ClockHours()
                mainloop  -> Ativação em looping
        """
        self.root = Tk()
        self.rootMain()
        self.framesFunction()
        self.GadgetsClock()
        self.positionContent()
        self.ClockHours()
        self.root.mainloop()
    
    def rootMain(self):
        """
            Janela principal da aplicação.

            Return:
                "root"    -> Janela
                title     -> Título da aplicação
                geometry  -> Dimensão da janela (width=400, height=200)
                resizable -> Ajustar a altura de largura da janela (função desabilitada)
                configure -> Configuração da janela (background)
                mainloop  -> Ativação em looping
        """
        self.root.title("Relógio")
        self.root.geometry("400x200")
        self.root.resizable(width='false', height='false')
        self.root.configure(background="#000")
    
    def framesFunction(self):
        """
            Frames da aplicação, todos localizados na janela `root`

            Return:
                frameTop -> Frame que armazena a label de horário
                frameBot -> Frame do label de calendário
        """
        self.frameTop = Frame(self.root, bg=lightBlack)
        self.frameBot = Frame(self.root, bg=Black)

    def GadgetsClock(self):
        """
            Gadgets referente ao horário[frameTop] e calendário[frameBot]

            Horário:
                `self.labelClock`    -> Label das horas
                `self.labelHoras`    -> Label text "Horas"
                `self.labelMinutos`  -> Label text "Minutos"
                `self.labelSegundos` -> Label text "Minutos"
            
            Calendário:
        """
        # Horário
        self.labelClock = Label(
            self.frameTop, text="00:00:00", font=("digital-7 85"), fg=lightBlue, bg=lightBlack, justify="center"
        )
        self.labelHoras = Label(
            self.frameTop, text="Horas", font=('Impact 13'), fg=lightBlue, bg=lightBlack
        )
        self.labelMinutos = Label(
            self.frameTop, text="Minutos", font=('Impact 13'), fg=lightBlue, bg=lightBlack
        )
        self.labelSegundos = Label(
            self.frameTop, text="Segundos", font=('Impact 13'), fg=lightBlue, bg=lightBlack
        )

        # Calendário
        self.labelCalendario = Label(
            self.frameBot, text="00/00/0000", font=('Impact 25'), fg=iceBlue, bg=lightBlack, anchor="center"
        )
        self.labelDiaSemana = Label(
            self.frameBot, text="Friday", font=('Impact 20'), fg=iceBlue, bg=lightBlack, anchor="center"
        )

    def positionContent(self):
        """
            Posição de todo o conteúdo imposto na aplicação.
        """
        # CONFIGURAÇÃO [framesFunction]
        self.frameTop.place(relwidth=1, relheight=0.70)
        self.frameBot.place(rely=0.70, relwidth=1, relheight=0.30)

        # CONFIGURAÇÃO [GadgetsClock]
        # [Horário]
        self.labelClock.place(relwidth=1)
        self.labelHoras.place(relx=0.10, rely=0.8)
        self.labelMinutos.place(relx=0.42, rely=0.8)
        self.labelSegundos.place(relx=0.74, rely=0.8)
        # [Calendário]
        self.labelCalendario.place(relwidth=0.5, relheight=1)
        self.labelDiaSemana.place(relx=0.5, relwidth=0.5, relheight=1)

# ============================================================
# APLICAÇÃO [ativada]
if __name__ == '__main__':
    letSet = "\033[47m  \033[m"
    statusSucess = "\033[46mAplicação ativada com sucesso!!\033[m" 
    print(f'{letSet}{statusSucess}')
    AppClock()

else:
    letSet = "\033[47m  \033[m"
    statusError = "\033[41mAlgo deu errado...\033[m"
    print(f'{letSet}{statusError}')