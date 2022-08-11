from tkinter import *
from tkinter import ttk

import pyglet
pyglet.font.add_file("digital-7.ttf")

cor_bg = "#111111" # preto
cor_tx = "#ffffff" # branco
cor_nu = "#0574f2" # azul claro

janela = Tk()
janela.title('')
janela.geometry('310x180')
janela.resizable(width=FALSE, height=FALSE)
janela.configure(bg=cor_bg)


global tempo
global rodar
global contador
global limitador


tempo = "00:00:00"
rodar = False
contador = -5
limitador = 59


# ===== FUNÇÕES =====
def iniciar():
    global tempo
    global contador
    global limitador

    if rodar:
        if contador <= -1:
            inicio = 'Começando em...' + str(contador)
            label_crono['text'] = inicio
            label_crono['font'] = 'Arial 10 bold'

        else:
            print('\033[34mContador iniciado!\033[m')

            temporaria = str(tempo)
            h,m,s = map(int,temporaria.split(":"))
            h = int(h)
            m = int(m)
            s = int(contador)

            if (s >=limitador):
                contador = 0
                m += 1
            h = str(0)+str(h)
            m = str(0)+str(m)
            s = str(0)+str(s)

            temporaria = str(h[-2:]) + ":" + str(m[-2:]) + ":" + str(s[-2:])
            label_crono['text'] = temporaria
            label_crono['font'] = 'digital-7 50 bold'
            tempo = temporaria

        label_crono.after(1000, iniciar)
        contador += 1

def start():
    global rodar
    rodar = True

    iniciar()

def pause():
    global rodar
    rodar = False
    print('')
    print('\033[31mContador pausado!\033[m')
    print('')

def reset():
    global contador
    global tempo

    contador = 0
    tempo = "00:00:00"
    print('')
    print('\033[33mContador resetado!\033[m')
    print('')
    label_crono['text'] = tempo
    label_crono['font'] = 'digital-7 50 bold'


# ===== JANELA =====
label_app = Label(janela, text="Cronômetro", font=('Arial 10'), bg=cor_bg, fg=cor_tx)
label_app.place(x=20, y=5)

label_crono = Label(janela, text=tempo, font=('digital-7 50 bold'), bg=cor_bg, fg=cor_nu)
label_crono.place(x=20, y=25)

# ===== BOTÕES =====
button_start = Button(janela, command=start, text="Iniciar", font=('Times 10 bold'), width=10, height=2, bg=cor_bg, fg=cor_tx, relief='raised', overrelief='ridge')
button_start.place(x=20, y=130)

button_pause = Button(janela, command=pause, text="Pausar", font=('Times 10 bold'), width=10, height=2, bg=cor_bg, fg=cor_tx, relief='raised', overrelief='ridge')
button_pause.place(x=100, y=130)


button_reset = Button(janela, command=reset, text="Reiniciar", font=('Times 10 bold'), width=10, height=2, bg=cor_bg, fg=cor_tx, relief='raised', overrelief='ridge')
button_reset.place(x=180, y=130)

janela.mainloop()
