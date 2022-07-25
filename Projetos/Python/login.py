from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

# Cores -------------------------------
cor0 = "#f0f3f5"  # Preta / black
cor1 = "#feffff"  # branca / white
cor2 = "#3fb5a3"  # verde / green
cor3 = "#38576b"  # valor / value
cor4 = "#403d3d"   # letra / letters

# Janela -------------------------------
janela = Tk()
janela.title("")
janela.geometry("310x300")
janela.configure(background=cor1)
janela.resizable(width=FALSE, height=FALSE)

# Layout (cima) -------------------------------
frame_cima = Frame(janela, width=210, height=50, bg=cor1, relief=FLAT)
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

# Layout (baixo) -------------------------------
frame_baixo = Frame(janela, width=310, height=250, bg=cor1, relief=FLAT)
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# Configuração (frame cima) -------------------------------
l_nome = Label(frame_cima, text="Sistema Friday", anchor=NE, font=('Ivy 25'), bg=cor1, fg=cor4)
l_nome.place(x=5, y=5)
l_linha = Label(frame_cima, text='', width=275, anchor=NW, font=('Ivy 25'), bg=cor2, fg=cor4)
l_linha.place(x=10, y=45)

credenciais = ['Tony Stark', 'ironmanbd']

def check_pass():
    nome = e_user.get()
    senha = e_pass.get()

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('Login Aceito', 'Seja bem-vindo, admin!')
    
    elif credenciais[0] == nome and credenciais[1] == senha:
        messagebox.showinfo('Check!','Seja bem-vindo de volta, {}!'.format(credenciais[0]))
        for widget in frame_baixo.winfo_children():
            widget.destroy()  
        
        for  widget in frame_cima.winfo_children():
            widget.destroy()

        nova_janela()
    
    else:
        messagebox.showwarning('Error - Ultron','[ERRO] Verifique novamente o usuário e/ou senha!')

def nova_janela():
    l_nome = Label(frame_cima, text="Usuário: " + credenciais[0], anchor=NE, font=('Ivy 20'), bg=cor1, fg=cor4)
    l_nome.place(x=5, y=5)

    l_linha = Label(frame_cima, text='', width=275, anchor=NW, font=('Ivy 25'), bg=cor2, fg=cor4)
    l_linha.place(x=10, y=45)

    l_nome = Label(frame_baixo, text="Seja bem-vindo! \n"+ credenciais[0], anchor=NE, font=('Ivy 20'), bg=cor1, fg=cor4)
    l_nome.place(x=55, y=105)

# Configuração (frame baixo) -------------------------------
l_user = Label(frame_baixo, text="Nome De Usuário *", anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
l_user.place(x=10, y=20)
e_user = Entry(frame_baixo, width=25, justify='left', font=("", 15), highlightthickness=1, relief='solid')
e_user.place(x=14, y=50)

l_pass = Label(frame_baixo, text="Senha *", anchor=NW, font=('Ivy 10'), bg=cor1, fg=cor4)
l_pass.place(x=10, y=95)
e_pass = Entry(frame_baixo, width=25, justify='left', show="*", font=("", 15), highlightthickness=1, relief='solid')
e_pass.place(x=14, y=130)

l_send = Button(frame_baixo, text="Enviar", command= check_pass, width= 39, height=2,font=('Ivy 8 bold'), 
bg=cor2, fg=cor1, relief=RAISED, overrelief=RIDGE)
l_send.place(x=10, y=180)

janela.mainloop()