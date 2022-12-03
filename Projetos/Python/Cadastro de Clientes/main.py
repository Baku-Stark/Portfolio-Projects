# ===============================================
# IMPORTAÇÕES [datetime]
from datetime import datetime

# ===============================================
# IMPORTAÇÕES [Tkinter]
from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter import messagebox

# ===============================================
# Gráficos[Matplotlib]
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ===============================================
# reportlab [PDF]
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image

# ===============================================
# IMPORTAÇÕES [functions.py n' database.py]
from functions import *
from database import cadastroCreate

# ===============================================
# CORES
bg_root = "#111111"
fg_root = "#111111"

bg_button = "#111111"
fg_button = "#f0f8ff"

frame_top_bottom = "#f0f8ff"
hl_bg = "#9C9FA6"

bg_aba1 = "#D7D9D9"
bg_aba2 = "#6F7372"

# ===============================================
# JANELA [config.]
root = tix.Tk()

class TableRead():
    # Ler banco de dados [cadastro.db]
    def readTable(self):
        lista = readCRUD()

        for item in lista:
            self.listaCli.insert('', 'end', values=item)
    
class Graph():
    def graphCity(self):
        # -------- GRÁFICO --------
        self.figura = plt.Figure(figsize=(8,4), dpi=60)
        self.ax = self.figura.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.figura, self.aba2)

        np.random.seed(19680801)
        self.cidades = ["Angra dos Reis", "Barra Mansa", "Volta Redonda", "Outros", "Não informada"]
        
        self.angra_reis = 0
        self.barra_mansa = 0
        self.volta_redonda = 0
        self.outros = 0
        self.n_info = 0

        list_data = ""
        c = 0

        for value in readCrudCity():
            list_data = value[0].upper()
            c+=1

            if list_data == "ANGRA DOS REIS":
                self.angra_reis += 1

            elif list_data == "BARRA MANSA":
                self.barra_mansa +=1

            elif list_data == "VOLTA REDONDA":
                self.volta_redonda += 1

            elif list_data == "CIDADE NÃO INFORMADA":
                self.n_info += 1
            
            else:
                self.outros += 1
        
        x_pos = 0
        y_pos = np.arange(len(self.cidades))
        self.count_cidade = [self.angra_reis, self.barra_mansa, self.volta_redonda, self.outros, self.n_info]
        self.ax.barh(y_pos, self.count_cidade, xerr=x_pos)
        self.ax.set_yticks(y_pos, labels=self.cidades)
        self.ax.invert_yaxis()
        self.ax.set_title('Qtd. de Cidades Cadastradas')
        # -------- GRÁFICO --------

        # -------- GRÁFICO --------
        self.canvas.get_tk_widget().place(relx=0, rely=0, relwidth=1, relheight=1)
        # -------- GRÁFICO --------

class Rede():
    def gitHub(self):
        gitHub = "https://github.com/Baku-Stark"
        webbrowser.open_new(gitHub)

    def twitter(self):
        twitter = "https://twitter.com/Walleemc2"
        webbrowser.open_new(twitter)

    def instagram(self):
        instagram = "https://www.instagram.com/wallace_emc2/"
        webbrowser.open_new(instagram)
    
    def linkedin(self):
        linkedin = "https://www.linkedin.com/in/wallace-freitas-92a2061b6/"
        webbrowser.open_new(linkedin)

class App(TableRead, Graph, Rede):
    def __init__(self):
        self.root = root
        self.tela()
        self.frame_tela()
        self.frameTop_Gadgets()
        self.frameBottom_Gadgets()

        self.readTable()
        self.Menu()
        self.graphCity()
        # =======================================
        # ROOT [mainloop]
        root.mainloop()
    
    # ===============================================
    # TELA [Frames > Gadgets]
    def tela(self):
        self.root.title("Python - Cadastro de Cliente")
        self.root.iconbitmap("_img/natural.ico")
        self.root.geometry("700x500")
        self.root.configure(background=bg_root)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=400)
        self.root.resizable(width='true', height='true')

    # ===========================================
    # CONFIGURAÇÃO [Menu]
    def Menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)
        filemenu3 = Menu(menubar)

        def Quit():
            self.root.destroy()

        menubar.add_cascade(label="Opções", menu=filemenu)
        menubar.add_cascade(label="Relatório", menu=filemenu2)
        menubar.add_cascade(label="Aplicação", menu=filemenu3)

        filemenu.add_command(label="Sair", command=Quit)
        filemenu.add_command(label="Limpar Cliente", command=self.limpar_tela)

        filemenu2.add_command(label="Ficha do Cliente(PDF)", command=self.gerarRelatClient)

        filemenu3.add_command(label="Sobre a aplicação", command=self.root2)

    # ===========================================
    # CONFIGURAÇÃO [Toplevel => Nova Janela]
    def root2(self):
        self.root2 = Toplevel()
        self.root2.grab_set()
        self.root2.focus_force()
        self.root2.geometry("400x200")
        self.root2.transient(self.root)
        self.root2.title("Sobre a aplicação")
        self.root2.configure(background=bg_root)
        self.root2.resizable(width='false', height='false')

        text_autor = "Autor do projeto: Wallace (Baku-Stark)"
        self.nome_autor = Label(
            self.root2, text=text_autor, font=('Arial 10 bold'),
            bg="#111111", fg="#f0f8ff"
        )
        self.nome_autor.place(x=5, y=10)

        # --- GITHUB
        self.gitHub_btn = Button(
            self.root2, text="GitHub", font=('Arial 10 bold'),
            bg="#111111", fg="#f0f8ff", relief="raised", overrelief="ridge"
        )
        self.gitHub_btn['command'] = self.gitHub
        self.gitHub_btn.place(x=5, y=40)

        # --- TWITTER
        self.twitter_btn = Button(
            self.root2, text="Twitter", font=('Arial 10 bold'),
            bg="#111111", fg="#f0f8ff", relief="raised", overrelief="ridge"
        )
        self.twitter_btn['command'] = self.twitter
        self.twitter_btn.place(x=65, y=40)

        # --- INSTAGRAM
        self.instagram_btn = Button(
            self.root2, text="Instagram", font=('Arial 10 bold'),
            bg="#111111", fg="#f0f8ff", relief="raised", overrelief="ridge"
        )
        self.instagram_btn['command'] = self.instagram
        self.instagram_btn.place(x=125, y=40)

        # --- LINKEDIN
        self.linkedin_btn = Button(
            self.root2, text="LinkedIN", font=('Arial 10 bold'),
            bg="#111111", fg="#f0f8ff", relief="raised", overrelief="ridge"
        )
        self.linkedin_btn['command'] = self.linkedin
        self.linkedin_btn.place(x=205, y=40)

    # ===========================================
    # FRAMES [top - bottom]
    def frame_tela(self):
        self.frameTop = Frame(
            self.root, bg=frame_top_bottom, bd=4,
            highlightbackground=hl_bg, highlightthickness=3
        )

        self.frameBottom = Frame(
            self.root, bg=frame_top_bottom, bd=4,
            highlightbackground=hl_bg, highlightthickness=3
        )
        # =======================================
        # INSERÇÃO DE FRAME
        self.frameTop.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)  
        self.frameBottom.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
        # INSERÇÃO DE FRAME
        # =======================================

    # ===============================================
    # CONFIGURAÇÃO [Double Click]
    def OnDoubleClick(self, event):
        try:
            self.limpar_tela()
            self.listaCli.selection()

            list_data = self.listaCli.focus()
            list_dic = self.listaCli.item(list_data)
            list_set = list_dic['values']
            self.codigo_entry.insert(0, list_set[1])
            self.nome_entry.insert(0, list_set[2])
            self.telefone_entry.insert(0, list_set[3])
            self.cidade_entry.insert(0, list_set[4])

        except IndexError:
            messagebox.showerror(
                title="Nenhuma dado encontrado",
                message="A lista está limpa. Nenhum dado pode ser selecionado."
            )

    # ===============================================
    # CONFIGURAÇÃO [reportlab PDF]
    # === FUNÇÕES

    # === CONFIGURAÇÃO [caminho do arquivo]
    def printClient(self):
        self.nomeArq = self.nome_entry.get()
        webbrowser.open(f"clientPDF/{self.nomeArq}.pdf")

    # === CONFIGURAÇÃO [gerar PDF]
    def gerarRelatClient(self):
        self.codigoRel = self.codigo_entry.get()
        self.nomeRel = self.nome_entry.get()
        self.telefoneRel = self.telefone_entry.get()
        self.cidadeRel = self.cidade_entry.get().upper()

        self.c = canvas.Canvas(f"clientPDF/{self.nomeRel}.pdf")

        # MARGEM
        self.c.rect(20, 10, 550, 820, fill=False, stroke=True)
        #self.<variável canvas>.rect(x, y, largura, altura)
        # MARGEM

        # TÍTULO
        self.c.setFont(psfontname="Helvetica-Bold", size=24)
        self.c.drawString(200, 790, f'Ficha do(a) {self.nomeRel}')
        # TÍTULO

        # CONTEÚDO [pdf => dados do usuário]
        self.c.rect(20, 770, 550, 2, fill=True, stroke=False)
        self.c.setFont(psfontname="Helvetica-Bold", size=18)
        self.c.drawString(50, 700, f"Código: {self.codigoRel}")
        self.c.drawString(50, 670, f"Nome: {self.nomeRel}")
        self.c.drawString(50, 630, f"Telefone: {self.telefoneRel[0:5]}-{self.telefoneRel[5:]}")
        self.c.drawString(50, 600, f"Cidade: {self.cidadeRel}")
        if self.cidadeRel == "BARRA MANSA":
            self.c.drawString(50, 570, f"Coordenadas de {self.cidadeRel}: -22.54, -44.17")
        elif self.cidadeRel == "ANGRA DOS REIS":
            self.c.drawString(50, 570, f"Coordenadas de {self.cidadeRel}: -23.00, -44.31")
        elif self.cidadeRel == "VOLTA REDONDA":
            self.c.drawString(50, 570, f"Coordenadas de {self.cidadeRel}: -22.50, -44.09")
        else:
            self.c.drawString(50, 570, f"As coordenadas de {self.cidadeRel} não estão no sistema.")
        self.c.rect(20, 550, 540, 2, fill=True, stroke=False)
        # CONTEÚDO [pdf => dados do usuário]

        # DADOS [pdf => último acesso ao servidor]
        mes_translate = {
            1:"Janeiro", 2:"Fevereiro", 3:"Março", 4:"Abril", 5:"Maio", 6:"Junho",
            7:"Julho", 8:"Agosto", 9:"Setembro", 10:"Outubro", 11:"Novembro", 12:"Dezembro"
        }

        tempo_atual = datetime.now()
        dia_atual = tempo_atual.day
        mes_atual = tempo_atual.month
        ano_atual = tempo_atual.year

        hora_atual = tempo_atual.hour
        minuto_atual = tempo_atual.minute

        self.c.setFont(psfontname="Helvetica-Bold", size=18)
        self.c.drawString(50, 490, f"Último acesso: {dia_atual}/{mes_translate[mes_atual]}/{ano_atual}")
        if minuto_atual < 10:
            self.c.drawString(50, 470, f"Horas: {hora_atual}:0{minuto_atual}")
        else:
            self.c.drawString(50, 470, f"Horário: {hora_atual}:{minuto_atual}")
        
        # DADOS [pdf => último acesso ao servidor]
        
        self.c.showPage()
        self.c.save()
        self.printClient()

    # ===============================================
    # Funções [main.py > functions.py]
    # Limpar Conteúdo [st_Limpar]
    def limpar_tela(self):
        self.codigo_entry.delete(0, 'end')
        self.nome_entry.delete(0, 'end')
        self.telefone_entry.delete(0, 'end')
        self.cidade_entry.delete(0, 'end')

    # Inserir Usuário [st_Novo]
    def novo_usuario(self):
        codigoUser = self.codigo_entry.get()
        nomeUser = self.nome_entry.get()
        telefoneUser = self.telefone_entry.get()
        cidadeUser = self.cidade_entry.get()

        # ---- [CÓDIGO]
        if codigoUser == "" and nomeUser == "":
            messagebox.showwarning(
                title="Código e/ou Nome",
                message="CÓDIGO e NOME são obrigados para o registro."
            )

        elif codigoUser == "":
            messagebox.showwarning(
                title="Inserção de código vazia",
                message="O usuário precisa preencher a opção CÓDIGO para fazer um novo cadastro."
            )
        # ---- [CÓDIGO]

        # ---- [NOME]
        elif nomeUser == "":
            messagebox.showwarning(
                title="Inserção de nome vazia",
                message="O usuário precisa preencher a opção Nome para fazer um novo cadastro."
            )
        # ---- [NOME]

        # ---- [TELEFONE]
        elif len(telefoneUser) > 9:
            messagebox.showwarning(
                title="Inserção de telefone inválida",
                message="O número de telefone ultrapassou o limite de dígitos."
            )
            self.telefone_entry.delete(0, 'end')

        elif len(telefoneUser) < 8:
            messagebox.showwarning(
                title="Inserção de telefone inválida",
                message="O telefone precisa (no máximo) de 8 dígitos para a autocorreção funcionar."
            )
            self.telefone_entry.delete(0, 'end')

        elif len(telefoneUser) == 8:
            messagebox.showwarning(
                title="Correção no número de telefone",
                message="O número de telefone possui 8 dígitos. Então, o programa adicionou um '9' na frente."
            )

            telefoneUser = f"9{telefoneUser}"

            lista = [codigoUser, nomeUser, telefoneUser, cidadeUser]
            createCRUD(lista)

            messagebox.showinfo(
                title="Sucesso!",
                message="Um novo cadastro foi efetuado com sucesso!"
            )
            self.limpar_tela()
        # ---- [TELEFONE]
        
        # ---- [CIDADE]
        elif cidadeUser == "":
            cidadeUser = "Cidade não informada"

            lista = [codigoUser, nomeUser, telefoneUser, cidadeUser]
            createCRUD(lista)

            messagebox.showinfo(
                title="Sucesso!",
                message="Um novo cadastro foi efetuado com sucesso!"
            )
            self.limpar_tela()
        # ---- [CIDADE]

        # ---- [EFETUADO COM SUCESSO (sem interrupções)]
        else:
            lista = [codigoUser, nomeUser, telefoneUser, cidadeUser]
            createCRUD(lista)

            messagebox.showinfo(
                title="Sucesso!",
                message="Um novo cadastro foi efetuado com sucesso!"
            )
            self.limpar_tela()
        # ---- [EFETUADO COM SUCESSO (sem interrupções)]
    
    # Atualizar Usuário [st_Alterar]
    def atualizar_usuario(self):
        try:
            list_data = self.listaCli.focus()
            list_dic = self.listaCli.item(list_data)
            list_set = list_dic['values']

            valorID = list_set[0]

            self.limpar_tela()

            self.codigo_entry.insert(0, list_set[1])
            self.nome_entry.insert(0, list_set[2])
            self.telefone_entry.insert(0, list_set[3])
            self.cidade_entry.insert(0, list_set[4])

            #UPDATE FUNCTION
            def updateCheck():
                new_codigo = self.codigo_entry.get()
                new_nome = self.nome_entry.get()
                new_telefone = self.telefone_entry.get()
                new_cidade = self.cidade_entry.get()

                lista = [new_codigo, new_nome, new_telefone, new_cidade, valorID]


                    
                if new_nome == "":
                    messagebox.showwarning(
                            title="Erro na atualização",
                            message="Um nome precisa ser inserido!"
                    )
                else:
                    updateCRUD(lista)
                    messagebox.showinfo(
                        title="Atualização",
                        message="Atualização feita com sucesso!"
                    )
                    self.limpar_tela()
                    self.btn_confirm.destroy()
                    
            self.btn_confirm = Button(
                    self.aba1, text="Confirmar",
                    font=('Arial 8 bold'), overrelief="raised", relief="ridge"
                )
            self.btn_confirm['command'] = updateCheck

            self.btn_confirm.place(relx=0.7, rely=0.10, relwidth=0.1, relheight=0.15)

        except IndexError:
            messagebox.showerror("Erro", "Selecione um dos dados na tabela!")

    # Deletar Usuário [st_Apagar]
    def deletar_usuario(self):
        list_data = self.listaCli.focus()
        list_dic = self.listaCli.item(list_data)
        list_set = list_dic['values']

        valorID = [list_set[0]]

        deleteCRUD(valorID)

        messagebox.showinfo(
            title="Usuário deletado",
            message="O usuário foi deletado com sucesso!"
        )

    # Buscar Usuário [st_Buscar]
    def buscar_usuario(self):
        self.listaCli.delete(*self.listaCli.get_children())

        self.nome_entry.insert('end', '%')
        nome = self.nome_entry.get()
        
        for i in buscarCRUD(nome):
            self.listaCli.insert("", 'end', values=i)
        
        self.limpar_tela()
    # Funções [main.py > functions.py]
    # ===============================================
    
    # ===========================================
    # Gadgets [Top_Frame]
    def frameTop_Gadgets(self):
        # -------- ABAS ----------
        self.abas = ttk.Notebook(self.frameTop)
        self.aba1 = Frame(self.abas)
        self.aba2 = Frame(self.abas)

        self.abas.add(self.aba1, text="Registro")
        self.abas.add(self.aba2, text="Gráfico")

        self.aba1.configure(background=bg_aba1)
        self.aba2.configure(background=bg_aba2)
        # -------- ABAS -----------

        # -------- BUTTONS --------
        self.st_Limpar = tix.Button(
            self.aba1, text="Limpar",
            font=('Arial 8 bold'), bg=bg_button, fg=fg_button,
            overrelief="ridge", relief='raised'
        )
        self.st_Limpar['command'] = self.limpar_tela
        self.balao_limpar = tix.Balloon(self.frameTop)
        self.balao_limpar.bind_widget(self.st_Limpar, balloonmsg="Limpar os campos.")

        self.st_Buscar = tix.Button(
            self.aba1, text="Buscar",
            font=('Arial 8 bold'), bg=bg_button, fg=fg_button,
            overrelief="ridge", relief='raised'
        )
        self.st_Buscar['command'] = self.buscar_usuario
        self.balao_buscar = tix.Balloon(self.frameTop)
        self.balao_buscar.bind_widget(self.st_Buscar, balloonmsg="Procurar por um usuário desejado na lista.")

        self.st_Novo = tix.Button(
            self.aba1, text="Novo",
            font=('Arial 8 bold'), bg=bg_button, fg=fg_button,
            overrelief="ridge", relief='raised'
        )
        self.st_Novo['command'] = self.novo_usuario
        self.balao_novo = tix.Balloon(self.frameTop)
        self.balao_novo.bind_widget(self.st_Novo, balloonmsg="Adicionar novo usuário ao banco de dados.")

        self.st_Alterar = tix.Button(
            self.aba1, text="Alterar",
            font=('Arial 8 bold'), bg=bg_button, fg=fg_button,
            overrelief="ridge", relief='raised'
        )
        self.st_Alterar['command'] = self.atualizar_usuario
        self.balao_alterar = tix.Balloon(self.frameTop)
        self.balao_alterar.bind_widget(self.st_Alterar, balloonmsg="Atualizar informações do usuário.")

        self.st_Apagar = tix.Button(
            self.aba1, text="Apagar",
            font=('Arial 8 bold'), bg=bg_button, fg=fg_button,
            overrelief="ridge", relief='raised'
        )
        self.st_Apagar['command'] = self.deletar_usuario
        self.balao_apagar = tix.Balloon(self.frameTop)
        self.balao_apagar.bind_widget(self.st_Apagar, balloonmsg="Apagar usuário.")
        # -------- BUTTONS --------

        # -------- LABELS N' INPUTS --------
        self.codigo = Label(
            self.aba1, text="Código",
            font=('Arial 10 bold'), bg=bg_aba1
        )
        self.codigo_entry = Entry(self.aba1)

        # ----- NOME
        self.nome = Label(
            self.aba1, text="Nome",
            font=('Arial 10 bold'), bg=bg_aba1
        )
        self.nome_entry = Entry(self.aba1)
        # ----- NOME

        # ----- TELEFONE
        self.telefone = Label(
            self.aba1, text="Telefone",
            font=('Arial 10 bold'), bg=bg_aba1
        )
        self.telefone_entry = Entry(self.aba1)
        # ----- TELEFONE

        # ----- CIDADE
        self.cidade = Label(
            self.aba1, text="Cidade",
            font=('Arial 10 bold'), bg=bg_aba1
        )
        self.cidade_entry = Entry(self.aba1)
        # ----- CIDADE
        # -------- LABELS N' INPUTS --------

        # =======================================
        # INSERÇÃO DOS GADGETS
        # -------- ABAS --------
        self.abas.place(relx=0, rely=0, relwidth=0.98, relheight=0.98)
        # -------- ABAS --------

        # -------- BUTTONS --------
        self.st_Limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        self.st_Buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)

        self.st_Novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        self.st_Alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

        self.st_Apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)
        # -------- BUTTONS --------

        # -------- LABELS N' INPUTS --------
        self.codigo.place(relx=0.05, rely=0.02)
        self.codigo_entry.place(relx=0.05, rely=0.12, relwidth=0.1, relheight=0.13)

        self.nome.place(relx=0.05, rely=0.40)
        self.nome_entry.place(relx=0.05, rely=0.52, relwidth=0.80, relheight=0.13)

        self.telefone.place(relx=0.05, rely=0.7)
        self.telefone_entry.place(relx=0.05, rely=0.8, relwidth=0.30)

        self.cidade.place(relx=0.45, rely=0.7)
        self.cidade_entry.place(relx=0.45, rely=0.8, relwidth=0.30)
        # -------- LABELS N' INPUTS --------
    
    # ===========================================
    # Gadgets [Bottom_Frame]
    def frameBottom_Gadgets(self):
        colunas = ("ID", "Código", "Nome", "Telefone", "Cidade")
        self.listaCli = ttk.Treeview(
            self.frameBottom, height=3, columns=colunas, show='headings'
        )

        self.scrollY = ttk.Scrollbar(
            self.frameBottom, orient='vertical'
        )
        self.scrollY['command'] = self.listaCli.yview
        self.listaCli.configure(yscrollcommand=self.scrollY)

        listaWidth = [1, 50, 200, 125, 125]
        c = 0
        
        for col in colunas:
            self.listaCli.heading(c, text=col)
            self.listaCli.column(c, width=listaWidth[c], anchor='center')
            c += 1

        self.listaCli.bind("<Double-1>", self.OnDoubleClick)
        # =======================================
        # INSERÇÃO DA LISTA
        self.listaCli.place(relx=0.01, rely=0.01, relwidth=0.96, relheight=0.98)
        self.scrollY.place(relx=0.97, rely=0.01, relwidth=0.03, relheight=0.98)
        # TELA [Frames > Gadgets] ===============

# ===============================================
# EXECUÇÃO DA JANELA
if __name__ == '__main__':
    cadastroCreate()
    App()
    