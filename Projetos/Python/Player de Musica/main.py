#  ======================================================
# IMPORTAÇÃO [os]
import os
# IMPORTAÇÃO [tkinter, messagebox]
from tkinter import *
from tkinter import messagebox
# IMPORTAÇÃO [PIL]
from PIL import Image, ImageTk
# IMPORTAÇÃO [pygame]
from pygame import mixer


#  ======================================================
# CORES
bg_screen = "#0e0e0e"
bg_frame = "#151515"
letter = "#eaeaea"
dest = "#ff0055"

#  ======================================================
# APP [CONSTRUCTOR]
class Music():
    def showMusic(self):
        '''
            Mostrar as músicas ('song') em na list box.

            Return:
                diretorio_atual: Caminho atual do arquivo
                arq_music: Lista das músicas na pasta 'song'

                listMusic.insert: Inserindo as músicas na list box
        '''

        self.diretorio_atual = os.getcwd()
        self.arq_music = os.listdir(rf"{self.diretorio_atual}\song")
        
        for music_item in self.arq_music:
            if (".wav") in music_item:
                # Será mostrado apenas os arquivos de áudio '.wav'
                self.listMusic.insert('end', music_item)
    
    def prevMusic(self):
        '''
            Tocar música ANTERIOR

            Vars:
                playing_music: Música atual
                index_list: Index do arquivo de música na pasta 'song'
                new_index_list: Novo index (retonar o valor do arquivo)
                self.arq_music[-1]: Retorna o último valor da pasta 'song'
        '''

        try:
            self.diretorio_atual = os.getcwd()
            self.arq_music = os.listdir(rf"{self.diretorio_atual}\song")
            
            playing_music = self.set_music['text']
            index_list = self.arq_music.index(playing_music)
            new_index_list = index_list - 1
            self.set_music['text'] = self.arq_music[new_index_list]

            mixer.music.load(rf"{self.diretorio_atual}\song\{self.set_music['text']}")
            mixer.music.play()

        except IndexError:
            self.diretorio_atual = os.getcwd()
            self.arq_music = os.listdir(rf"{self.diretorio_atual}\song")
            self.set_music['text'] = self.arq_music[-1]

            mixer.music.load(rf"{self.diretorio_atual}\song\{self.set_music['text']}")
            mixer.music.play()

    def playMusic(self):
        '''
            Tocar a música selecionada
        '''
        self.set_music['text'] = self.listMusic.get(ACTIVE)
        self.set_music['anchor'] = 'w'
        mixer.music.load(rf"{self.diretorio_atual}\song\{self.listMusic.get(ACTIVE)}")
        mixer.music.play()
        
    def nextMusic(self):
        '''
            Tocar música SEGUINTE

            Vars:
                playing_music: Música atual
                index_list: Index do arquivo de música na pasta 'song'
                new_index_list: Novo index (retonar o valor do arquivo)
                self.arq_music[0]: Retorna o último valor da pasta 'song'
        '''

        try:
            self.diretorio_atual = os.getcwd()
            self.arq_music = os.listdir(rf"{self.diretorio_atual}\song")
            
            playing_music = self.set_music['text']
            index_list = self.arq_music.index(playing_music)
            new_index_list = index_list + 1
            self.set_music['text'] = self.arq_music[new_index_list]

            mixer.music.load(rf"{self.diretorio_atual}\song\{self.set_music['text']}")
            mixer.music.play()

        except IndexError:
            self.diretorio_atual = os.getcwd()
            self.arq_music = os.listdir(rf"{self.diretorio_atual}\song")
            self.set_music['text'] = self.arq_music[0]

            mixer.music.load(rf"{self.diretorio_atual}\song\{self.set_music['text']}")
            mixer.music.play()

class App(Music):
    def __init__(self):
        '''
            Função principal para a
            exibição da janela.
        '''
        self.root = Tk()
        self.screen()
        self.frameScreen()
        self.labelScreen()
        self.gadgetsFrame()
        self.position()
        self.showMusic()
        # -----
        self.root.mainloop()

    def screen(self):
        '''
            Configuração principal da aplicação

            Return:
                title: Título da aplicação

                geometry: Dimensão da janela (width x height)

                resizable: Ajustar tamanho da página (opção negada)

                configure [background]: Cor de fundo

                iconbitmap: Ícone da janela
        '''
        self.root.title("Music Player 2.0")
        self.root.geometry("450x300")
        self.root.resizable(width='false', height='false')
        self.root.configure(background=bg_screen)
        self.root.iconbitmap('img/music_dk_icon_128980.ico')
    
    def frameScreen(self):
        '''
            Frames da aplicação

            Return:
                frame_TopLeft: Icon de música\n
                frame_BotLeft: Botões de ação\n
                frame_Right: Lista de músicas [pasta: 'song']
        '''
        self.frame_TopLeft = Frame(self.root, bg=bg_frame)
        self.frame_BotLeft = Frame(self.root, bg=bg_screen)
        self.frame_Right = Frame(self.root, bg=bg_screen)

    def labelScreen(self):
        '''
            Labels da aplicação

                set_image: Label da imagem mixer.
                set_music: Label onde será mostrada a música que está tocando.
        '''
        self.image_Label = Image.open('img/mixer-de-dj.png')
        self.image_Label = self.image_Label.resize((134, 134))
        self.image_Label = ImageTk.PhotoImage(self.image_Label)
        self.set_image = Label(
            self.frame_TopLeft, bg=bg_screen, image= self.image_Label
        )

        self.set_music = Label(
            self.frame_BotLeft, font=('Ivy 10 italic'), bg="#dedcdc", fg="#111111",
            text="Escolha uma música...", anchor='c'
        )

    def gadgetsFrame(self):
        '''
            Gadgets para aplicar as funções.

            Return:
                listMusic: Lista para armazenar as músicas da pasta 'song'
                scrollBar: Scroll unificada à list box de músicas.
                \n
                bottom_Prev: Botão Previous
                bottom_Play: Botão Play
                bottom_Next: Botão Next
                    |\n
                    |\n
                    [---> Todos para música
        '''
        self.listMusic = Listbox(self.frame_Right, font=('Arial 8 bold'))
        self.scrollBar = Scrollbar(self.frame_Right)

        self.image_Prev = Image.open('img/prev.png')
        self.image_Prev = self.image_Prev.resize((34, 34))
        self.image_Prev = ImageTk.PhotoImage(self.image_Prev)
        self.bottom_Prev = Button(
            self.frame_BotLeft, image=self.image_Prev, bd=0,
            bg=bg_screen
        )
        self.bottom_Prev['command'] = self.prevMusic

        self.image_Play = Image.open('img/play.png')
        self.image_Play = self.image_Play.resize((34, 34))
        self.image_Play = ImageTk.PhotoImage(self.image_Play)
        self.bottom_Play = Button(
            self.frame_BotLeft, image=self.image_Play, bd=0,
            bg=bg_screen
        )
        self.bottom_Play['command'] = self.playMusic

        self.image_Next = Image.open('img/next.png')
        self.image_Next = self.image_Next.resize((34, 34))
        self.image_Next = ImageTk.PhotoImage(self.image_Next)
        self.bottom_Next = Button(
            self.frame_BotLeft, image=self.image_Next, bd=0,
            bg=bg_screen
        )
        self.bottom_Next['command'] = self.nextMusic

    def position(self):
        '''
            Posições dos gadgets da aplicação.
        '''
        # def [frameScreen]
        self.frame_TopLeft.place(relx=0, rely=0, relwidth=0.45, relheight=0.5)
        self.frame_BotLeft.place(relx=0, rely=0.5, relwidth=0.45, relheight=0.5)
        self.frame_Right.place(relx=0.45, rely=0, relwidth=0.55, relheight=1)

        # def [labelScreen]
        self.set_image.place(relwidth=1, relheight=1)
        self.set_music.place(relx=0, rely=0.8, relwidth=1, relheight=0.13)

        # def [gadgetsFrame]
        self.listMusic.place(relx=0, rely=0, relwidth=0.9, relheight=1)
        self.scrollBar.place(relx=0.9, rely=0, relwidth=0.1, relheight=1)
        self.bottom_Prev.place(relx=0.01, rely=0.25, relwidth=0.33, relheight=0.45)
        self.bottom_Play.place(relx=0.34, rely=0.25, relwidth=0.33, relheight=0.45)
        self.bottom_Next.place(relx=0.66, rely=0.25, relwidth=0.33, relheight=0.45)
        
#  ======================================================
# APP [ativação]
try:
    if __name__ == '__main__':
        mixer.init()
        App()
    letSet = "\033[47m  \033[m"
    statusSucess = "\033[46m Ativação feita com sucesso! \033[m" #Cyan Background
    newSetSucess = f"\033[1m{statusSucess}\033[m"
    print(f"{letSet}{newSetSucess}")
        

except AttributeError as e:
    letSet = "\033[47m [ERROR] \033[m"
    statusError = f"\033[41m {e} \033[m" #Red Background
    newSetError = f"\033[1m{statusError}\033[m"
    print(f"{letSet}{newSetError}")

    messagebox.showerror(
        title='[ERROR] - Ativação',
        message=f'{e}'
    )