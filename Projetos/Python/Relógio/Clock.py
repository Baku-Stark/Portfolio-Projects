from datetime import datetime
from tkinter import *
import tkinter

# importando fonte
import pyglet
pyglet.font.add_file("digital-7.ttf")


# Cores "color picker"
cor1 = "#2a2c2e" # cinza escuro "fundo"
cor2 = "#03d3fc" # azul claro "numero"

# Janela
janela = Tk()
janela.title("Relógio Digital")
janela.geometry("440x180")
janela.resizable(width=FALSE, height=FALSE)
janela.config(bg=cor1)

# Relógio
def relogio():
    tempo = datetime.now()
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%B")
    ano = tempo.year
    
    l1.config(text=hora)
    l1.after(200, relogio)
    l2.config(text=dia_semana + " " +
     str(dia) + " - " + str(mes) + " - " + str(ano))

l1 = Label(janela, text="XX:XX:xx", font=("digital-7 100"), bg=cor1, fg=cor2)
l1.grid(row=0, column=0, sticky=NW, padx=5)

l2 = Label(janela, text="Dia - Mês - Ano", font=("digital-7 17"), bg=cor1, fg=cor2)
l2.grid(row=1, column=0, sticky=NW, padx=5)

# Função para abrir janela (necessária)
relogio()
janela.mainloop()