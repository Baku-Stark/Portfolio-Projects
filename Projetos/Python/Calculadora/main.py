# ============================================================
# TKinter
from tkinter import *

# ============================================================
# Importando uma fonte
import pyglet
pyglet.font.add_file("font/digital-7.ttf") #font=("digital-7 100")


# ============================================================
# APPLICAÇÃO

# [CORES]
lightBlack = "#111111"
darkGreen = "#001a1f"
freshGreen = "#00536b"
oceanGreen = "#00b9a1"
lightGreen = "#c5fb88"
aliceBlue = "#f0f8ff"
# [CORES]

# [VARIÁVEIS]
todosValores = ""
# [VARIÁVEIS]

class Calculo():
    def enter_valores(self, simbol: str):
        """
            Inserir valores no painel.

            Args:
                simbol(str) -> Convertido para string

            Return:
                self.valorTexto -> Delvolve o texto alterado no painel.
        """
        global todosValores
        todosValores = todosValores + simbol
        self.valorTexto.set(todosValores)

    def resultadoCalculo(self):
        """
            Apresenta o resultado no painel

            Return:
                todosValores = "" -> Devolve o resultado o resultado vazio 
                                    para a realização de outro problema matemático.
        """
        global todosValores
        resultado = eval(todosValores)
        self.valorTexto.set(str(resultado))
        todosValores = ""

    def clearCalculo(self):
        """
            Limpa todos os valores inseridos no painel.
        """
        global todosValores
        todosValores = ""
        self.valorTexto.set("")

    def deleteLastCarac(self):
        """
            Exclui o último valor inserido no painel.

            Return:
                self.valorTexto -> Último valor já apagado.
        """
        global todosValores
        todosValores = str(todosValores[0:-1])
        self.valorTexto.set(todosValores)

class AppCalculator(Calculo):
    def __init__(self):
        """
            Componente principal da aplicação.
        """
        self.root = Tk()
        self.appScreen()
        self.framesScreen()
        self.labelScreen()
        self.keyboard()
        self.positionGadgets()
        self.root.mainloop()
    
    def appScreen(self):
        """
            Configuração da janela.

            Return:
                title..................-> Título da aplicação
                geometry...............-> Largura e Altura : `300x450`
                resizable..............-> Reajustar dimensão [desabilitada]
                configure(background)..-> Preto : `#000`
        """
        self.root.title("Calculadora")
        self.root.geometry("300x450")
        self.root.resizable(width='false', height='false')
        self.root.configure(background="#000")
    
    def framesScreen(self):
        """
            Frames da janela principal.

            Return:
                frameTop -> Frame de tela dos números.
                frameBot -> Frame de teclado.
        """
        self.frameTop = Frame(self.root, bg=darkGreen)
        self.frameBot = Frame(self.root, bg=lightBlack)

    def labelScreen(self):
        """
            Layout label onde é mostrado o cálculo e seu resultado.

            Return:
                labelTelaCalculo -> Tela do desenvolvimento do cálculo
        """
        self.valorTexto = StringVar()
        self.labelTelaCalculo = Label(
            self.frameTop, textvariable=self.valorTexto, font=('digital-7 35'), bg=lightBlack, fg=lightGreen, anchor='e'
        )

    def keyboard(self):
        """
            Teclado da aplicação calculadora.

            Return:
                [Botões - números]  -> Botões com os números
                [Botões - símbolos] -> Botões com os símbolos matemáticos
        """
        # [Botões - números]
        self.buttom_0 = Button(self.frameBot, command=lambda:self.enter_valores("0"), text="0", font=('Impact 15'), bd=1, bg=darkGreen, fg=aliceBlue, overrelief="raised", relief="ridge")
        self.buttom_1 = Button(self.frameBot, command=lambda:self.enter_valores("1"), text="1", font=('Impact 15'), bd=1, bg=darkGreen, fg=aliceBlue, overrelief="raised", relief="ridge")
        self.buttom_2 = Button(self.frameBot, command=lambda:self.enter_valores("2"), text="2", font=('Impact 15'), bd=1, bg=darkGreen, fg=aliceBlue, overrelief="raised", relief="ridge")
        self.buttom_3 = Button(self.frameBot, command=lambda:self.enter_valores("3"), text="3", font=('Impact 15'), bd=1, bg=darkGreen, fg=aliceBlue, overrelief="raised", relief="ridge")
        self.buttom_4 = Button(self.frameBot, command=lambda:self.enter_valores("4"), text="4", font=('Impact 15'), bd=1, bg=darkGreen, fg=aliceBlue, overrelief="raised", relief="ridge")
        self.buttom_5 = Button(self.frameBot, command=lambda:self.enter_valores("5"), text="5", font=('Impact 15'), bd=1, bg=darkGreen, fg=aliceBlue, overrelief="raised", relief="ridge")
        self.buttom_6 = Button(self.frameBot, command=lambda:self.enter_valores("6"), text="6", font=('Impact 15'), bd=1, bg=darkGreen, fg=aliceBlue, overrelief="raised", relief="ridge")
        self.buttom_7 = Button(self.frameBot, command=lambda:self.enter_valores("7"), text="7", font=('Impact 15'), bd=1, bg=darkGreen, fg=aliceBlue, overrelief="raised", relief="ridge")
        self.buttom_8 = Button(self.frameBot, command=lambda:self.enter_valores("8"), text="8", font=('Impact 15'), bd=1, bg=darkGreen, fg=aliceBlue, overrelief="raised", relief="ridge")
        self.buttom_9 = Button(self.frameBot, command=lambda:self.enter_valores("9"), text="9", font=('Impact 15'), bd=1, bg=darkGreen, fg=aliceBlue, overrelief="raised", relief="ridge")

        # [Botões - símbolos]
        self.buttom_AC = Button(self.frameBot, command=self.clearCalculo, text="AC", font=('Impact 15'), bd=1, bg=lightGreen, fg=lightBlack, overrelief="raised", relief="ridge")
        self.buttom_leftParen = Button(self.frameBot, command=lambda:self.enter_valores("("), text="(", font=('Impact 15'), bd=1, bg=oceanGreen, fg=aliceBlue, overrelief="raised", relief="ridge")
        self.buttom_rightParen = Button(self.frameBot, command=lambda:self.enter_valores(")"), text=")", font=('Impact 15'), bd=1, bg=oceanGreen, fg=aliceBlue, overrelief="raised", relief="ridge")
        self.buttom_Porcentagem = Button(self.frameBot, command=lambda:self.enter_valores("%"), text="%", font=('Impact 15'), bd=1, bg=oceanGreen, fg=aliceBlue, overrelief="raised", relief="ridge")
        self.buttom_Divisao = Button(self.frameBot, command=lambda:self.enter_valores("/"), text="÷", font=('Impact 15'), bd=1, bg=oceanGreen, fg=aliceBlue, overrelief="raised", relief="ridge")
        self.buttom_Multi = Button(self.frameBot, command=lambda:self.enter_valores("*"), text="x", font=('Impact 15'), bd=1, bg=oceanGreen, fg=aliceBlue, overrelief="raised", relief="ridge")
        self.buttom_Menos = Button(self.frameBot, command=lambda:self.enter_valores("-"), text="-", font=('Impact 15'), bd=1, bg=oceanGreen, fg=aliceBlue, overrelief="raised", relief="ridge")
        self.buttom_Mais = Button(self.frameBot, command=lambda:self.enter_valores("+"), text="+", font=('Impact 15'), bd=1, bg=oceanGreen, fg=aliceBlue, overrelief="raised", relief="ridge")
        self.buttom_Equal = Button(self.frameBot, command=self.resultadoCalculo, text="=", font=('Impact 15'), bd=1, bg=freshGreen, fg=aliceBlue, overrelief="raised", relief="ridge")
        self.buttom_Virgula = Button(self.frameBot, command=lambda:self.enter_valores("."), text=",", font=('Impact 15'), bd=1, bg=darkGreen, fg=aliceBlue, overrelief="raised", relief="ridge")
        self.buttom_Delete = Button(self.frameBot, command=self.deleteLastCarac, text="Del", font=('Impact 15'), bd=1, bg=darkGreen, fg=aliceBlue, overrelief="raised", relief="ridge")

    def positionGadgets(self):
        """
            Função de posicionamento dos frames e gadgets.

            Return:
                place -> utilzando o método de coordenadas (x, y, width, height).
        """
        # [framesScreen]
        self.frameTop.place(relwidth=1, relheight=0.20)
        self.frameBot.place(rely=0.2, relwidth=1, relheight=0.80)

        # [labelScreen]
        self.labelTelaCalculo.place(relx=0.025, rely=0.08, relwidth=0.95, relheight=0.85)

        # [keyboard]
        # ---[números]
        self.buttom_0.place(relx=0.21, rely=0.80, relwidth=0.20, relheight=0.20)
        self.buttom_1.place(relx=0.21, rely=0.60, relwidth=0.20, relheight=0.20)
        self.buttom_2.place(relx=0.41, rely=0.60, relwidth=0.20, relheight=0.20)
        self.buttom_3.place(relx=0.61, rely=0.60, relwidth=0.20, relheight=0.20)
        self.buttom_4.place(relx=0.21, rely=0.40, relwidth=0.20, relheight=0.20)
        self.buttom_5.place(relx=0.41, rely=0.40, relwidth=0.20, relheight=0.20)
        self.buttom_6.place(relx=0.61, rely=0.40, relwidth=0.20, relheight=0.20)
        self.buttom_7.place(relx=0.21, rely=0.20, relwidth=0.20, relheight=0.20)
        self.buttom_8.place(relx=0.41, rely=0.20, relwidth=0.20, relheight=0.20)
        self.buttom_9.place(relx=0.61, rely=0.20, relwidth=0.20, relheight=0.20)

        # ---[símbolos]
        self.buttom_AC.place(relx=0, rely=0, relwidth=0.21, relheight=0.20)
        self.buttom_leftParen.place(relx=0.21, rely=0, relwidth=0.20, relheight=0.20)
        self.buttom_rightParen.place(relx=0.41, rely=0, relwidth=0.20, relheight=0.20)
        self.buttom_Porcentagem.place(relx=0.61, rely=0, relwidth=0.20, relheight=0.20)
        self.buttom_Divisao.place(relx=0.81, rely=0, relwidth=0.20, relheight=0.20)
        self.buttom_Multi.place(relx=0.81, rely=0.20, relwidth=0.20, relheight=0.20)
        self.buttom_Menos.place(relx=0.81, rely=0.40, relwidth=0.20, relheight=0.20)
        self.buttom_Mais.place(relx=0.81, rely=0.60, relwidth=0.20, relheight=0.20)
        self.buttom_Equal.place(relx=0.81, rely=0.80, relwidth=0.20, relheight=0.20)
        self.buttom_Virgula.place(relx=0.41, rely=0.80, relwidth=0.20, relheight=0.20)
        self.buttom_Delete.place(relx=0.61, rely=0.80, relwidth=0.20, relheight=0.20)

# ============================================================
# APPLICAÇÃO [ativda]
try:
    if __name__ == '__main__':
        letSet = "\033[47m  \033[m"
        statusSucess = "\033[46m Aplicação efetuada com sucesso!!! \033[m" #Cyan Background
        newSetSucess = f"\033[1m{statusSucess}\033[m"
        print(f"{letSet}{newSetSucess}")
    AppCalculator()


except AttributeError as e:
    letSet = "\033[47m  \033[m"
    statusError = f"\033[41m Error \033[m {e}" #Red Background
    newSetError = f"\033[1m{statusError}\033[m"
    print(f"{letSet}{newSetError}")