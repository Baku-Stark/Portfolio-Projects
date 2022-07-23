# importando tkinter
from tkinter import *
from tkinter import ttk

# cores do programa
cor1 = "#2a2c2e" # cinza escuro
cor2 = "#059da8" # azul claro
cor3 = "#f5a905" # amarelo sol
cor4 = "#d2d4d2" # cinza claro
cor5 = "#034f91" # azul marinho
cor6 = "#ffffff" # branco

# janela da calculadora
janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=235, height=50, bg=cor1)
frame_tela.grid(row=0, column=0)

frame_teclado = Frame(janela, width=235, height=268)
frame_teclado.grid(row=1, column=0)

# logica da calculadora
todos_valores = ''

def enter_valores(event):

    global todos_valores

    todos_valores = todos_valores + str(event)

    # ---
    valor_texto.set(todos_valores)

def calcular():

    global todos_valores

    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

def clean():

    global todos_valores

    todos_valores = ""
    valor_texto.set("")

# label 
valor_texto = StringVar()

app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Arial 18'), bg=cor1, fg=cor6)
app_label.place(x=0, y=0)


# botões
b_c = Button(frame_teclado, command = clean, text="C", width=11, height=2, bg=cor4, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_c.place(x=0, y=0)
b_por = Button(frame_teclado, command = lambda: enter_valores('%'), text="%", width=5, height=2, bg=cor4, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_por.place(x=118, y=0)

# --OPERADORES--
b_div = Button(frame_teclado, command = lambda: enter_valores('/'), text="/", width=5, height=2, bg=cor3, fg=cor6, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_div.place(x=177, y=0)
b_multi = Button(frame_teclado, command = lambda: enter_valores('*'), text="x", width=5, height=2, bg=cor3, fg=cor6, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_multi.place(x=177, y=51)
b_sub = Button(frame_teclado, command = lambda: enter_valores('-'), text="-", width=5, height=2, bg=cor3, fg=cor6, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_sub.place(x=177, y=102)
b_plus = Button(frame_teclado, command = lambda: enter_valores('+'), text="+", width=5, height=2, bg=cor3, fg=cor6, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_plus.place(x=177, y=153)
b_equal = Button(frame_teclado, command = calcular, text = "=", width=5, height=3, bg=cor3, fg=cor6, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_equal.place(x=177, y=204)
b_vir = Button(frame_teclado, command = lambda: enter_valores('.'), text=",",  width=5, height=3, bg=cor4, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_vir.place(x=118, y=204)

# --NUMEROS--
b_0 = Button(frame_teclado, command = lambda: enter_valores('0'), text="0", width=11, height=3, bg=cor4, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_0.place(x=-1, y=204)
b_1 = Button(frame_teclado, command = lambda: enter_valores('1'), text="1", width=5, height=2, bg=cor4, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=153)
b_2 = Button(frame_teclado, command = lambda: enter_valores('2'), text="2", width=5, height=2, bg=cor4, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=59, y=153)
b_3 = Button(frame_teclado, command = lambda: enter_valores('3'), text="3", width=5, height=2, bg=cor4, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=118, y=153)
b_4 = Button(frame_teclado, command = lambda: enter_valores('4'), text="4", width=5, height=2, bg=cor4, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=102)
b_5 = Button(frame_teclado, command = lambda: enter_valores('5'), text="5", width=5, height=2, bg=cor4, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=102)
b_6 = Button(frame_teclado, command = lambda: enter_valores('6'), text="6", width=5, height=2, bg=cor4, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=102)
b_7 = Button(frame_teclado, command = lambda: enter_valores('7'), text="7", width=5, height=2, bg=cor4, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=51)
b_8 = Button(frame_teclado, command = lambda: enter_valores('8'), text="8", width=5, height=2, bg=cor4, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=59, y=51)
b_9 = Button(frame_teclado, command = lambda: enter_valores('9'), text="9", width=5, height=2, bg=cor4, font=('Arial 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=118, y=51)


janela.mainloop()