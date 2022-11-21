import os
from tkinter import *
from PIL import Image, ImageTk

#pygame
import pygame
from pygame import mixer

janela = Tk()
janela.geometry("352x255")
janela.title("Music Player")
janela.resizable(width=FALSE, height=FALSE)

# ----------------------------------------
# função
user = os.getlogin()
os.chdir(rf'C:\Users\{user}\Documents\Portfólio Git\Portfolio-Projects\Projetos\Python\Player de Musica\music')
musicas = os.listdir()

def show():
    for i in musicas:
        listbox.insert(END, i)

def previous_music():
    tocando = l_rolls['text']
    index = musicas.index(tocando)

    novo_index = index - 1

    tocando = musicas[novo_index]

    mixer.music.load(tocando)
    mixer.music.play()

    listbox.delete(0, END)
    show()
    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    l_rolls['text'] = tocando

def play_music():
    rolls = listbox.get(ACTIVE)
    l_rolls['text'] = rolls
    mixer.music.load(rolls)
    mixer.music.play()

def next_music():
    tocando = l_rolls['text']
    index = musicas.index(tocando)

    novo_index = index + 1

    tocando = musicas[novo_index]

    mixer.music.load(tocando)
    mixer.music.play()

    listbox.delete(0, END)
    show()
    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    l_rolls['text'] = tocando

def pause_music():
    mixer.music.pause()

def resume_music():
    mixer.music.unpause()

def stop_music():
    mixer.music.stop()

# ----------------------------------------
# widget
frame_esquerda = Frame(
    janela, width=150, height=150, bg="#111111"
)

# ----- imagem LOGO
img_player =  Image.open('../btn/ondas-sonoras.png')
img_player = img_player.resize((130, 130))
img_player = ImageTk.PhotoImage(img_player)

l_logo = Label(
    frame_esquerda, height=130, image=img_player, compound=LEFT, padx=10, anchor=NW, font=('Ivy 16 bold'), bg="#111111", fg="#111111"
)
# ----- imagem LOGO

# ----- frame direita
frame_direita = Frame(
    janela, width=250, height=150, bg="#111111"
)

listbox = Listbox(
    frame_direita, selectmode=SINGLE, width=22, height=10,
    font=('Arial 9 bold'), bg="#111111", fg="#dedcdc"
)


scroll = Scrollbar(frame_direita)
# ----- frame direita

# ----- frame baixo
frame_baixo = Frame(
    janela, width=404, height=100, bg="#111111"
)

l_rolls = Label(
    frame_baixo, text="Escolha uma música na lista", width=44, justify=LEFT, anchor=NW,
    font=('Ivy 10'), bg="#dedcdc", fg="#111111"
)

img_previous = Image.open('../btn/button-previous.png')
img_previous = img_previous.resize((30, 30))
img_previous = ImageTk.PhotoImage(img_previous)
b_previous = Button(
    frame_baixo, command=previous_music, width=40, height=40, justify=LEFT,
    font=('Ivy 10 bold'), image=img_previous, bg="#111111", relief=RAISED, overrelief=RIDGE
)

img_play = Image.open('../btn/button-play.png')
img_play = img_play.resize((30, 30))
img_play = ImageTk.PhotoImage(img_play)
b_play = Button(
    frame_baixo, width=40, command=play_music, height=40, justify=LEFT,
    font=('Ivy 10 bold'), image=img_play, bg="#111111", relief=RAISED, overrelief=RIDGE
)

img_next = Image.open('../btn/button-next.png')
img_next = img_next.resize((30, 30))
img_next = ImageTk.PhotoImage(img_next)
b_next = Button(
    frame_baixo, command=next_music, width=40, height=40, justify=LEFT,
    font=('Ivy 10 bold'), image=img_next, bg="#111111", relief=RAISED, overrelief=RIDGE
)

img_pause = Image.open('../btn/button-pause.png')
img_pause = img_pause.resize((30, 30))
img_pause = ImageTk.PhotoImage(img_pause)
b_pause = Button(
    frame_baixo, command=pause_music, width=40, height=40, justify=LEFT,
    font=('Ivy 10 bold'), image=img_pause, bg="#111111", relief=RAISED, overrelief=RIDGE
)

img_resume = Image.open('../btn/button-resume.png')
img_resume = img_resume.resize((30, 30))
img_resume = ImageTk.PhotoImage(img_resume)
b_resume = Button(
    frame_baixo, command=resume_music, width=40, height=40, justify=LEFT,
    font=('Ivy 10 bold'), image=img_resume, bg="#111111", relief=RAISED, overrelief=RIDGE
)

img_stop = Image.open('../btn/button-stop.png')
img_stop = img_stop.resize((30, 30))
img_stop = ImageTk.PhotoImage(img_stop)
b_stop = Button(
    frame_baixo, command=stop_music, width=40, height=40, justify=LEFT,
    font=('Ivy 10 bold'), image=img_stop, bg="#111111", relief=RAISED, overrelief=RIDGE
)
# ----------------------------------------
# painel
frame_esquerda.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
l_logo.place(x=24, y=15)

# ----- frame direita
frame_direita.grid(row=0, column=1, pady=1, padx=0, sticky=NSEW)

listbox.grid(row=0, column=0)
listbox.config(yscrollcommand=scroll.set)

scroll.grid(row=0, column=1, sticky=NSEW)
scroll.config(command=listbox.yview)
# ----- frame direita

# ----- frame baixo
frame_baixo.grid(row=1, column=0, columnspan=3,pady=1, padx=0, sticky=NSEW)
l_rolls.place(x=0, y=1)

# ----- Botões (espaçamento: x=44)
b_previous.place(x=38, y=35)
b_play.place(x=82, y=35)
b_next.place(x=126, y=35)
b_pause.place(x=170, y=35)
b_resume.place(x=214, y=35)
b_stop.place(x=258, y=35)
# ----- Botões (espaçamento: x=44)

# ----- frame baixo

show()
mixer.init()
janela.mainloop()
