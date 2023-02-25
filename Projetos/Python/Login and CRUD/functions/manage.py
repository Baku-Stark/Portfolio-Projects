# IMPORT os
import os

# IMPORT[sqlite3]
import sqlite3 as lite

# IMPORT [webbrowser]
import webbrowser

# IMPORT [pip3 install customtkinter]
import customtkinter

# IMPORT [pip install rich]
from rich import print as rprint

# IMPORT [tkinter]
from tkinter import *
from tkinter import ttk
from tkinter import messagebox, CENTER

# Gráficos[Matplotlib]
import numpy as np #[pip install numpy]
import matplotlib.pyplot as plt #[python -m pip install -U matplotlib]
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class ManageGRAPH():
    def countStatus(self):
        connection = lite.connect(rf"database_content/{self.GlobalUser}.db")
        with connection:
            cur = connection.cursor()
            command = "SELECT status FROM tasks"
            cur.execute(command)
            
            lista = []

            for item in cur.fetchall():
                lista.append(item[0])

        return lista

    def showGraph(self):
        # Bar color demo
        self.figura = plt.Figure(figsize=(8,4), dpi=60)
        self.ax = self.figura.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.figura, self.frameRIGHT_MANAGE)

        np.random.seed(19680801)

        c_andamento = 0
        c_finalizado = 0
        for item in self.countStatus():
            if item == "EM ANDAMENTO":
                c_andamento += 1
            else:
                c_finalizado += 1
        count_tasks = [c_andamento, c_finalizado]

        tasks_status = ["Em Andamento", "Finalizadas"]
        bar_labels = ['red', 'blue']
        bar_colors = ['tab:red', 'tab:blue']

        self.ax.bar(tasks_status, count_tasks, label=bar_labels, color=bar_colors)
        self.ax.set_title(f'Gráfico do(a) {self.GlobalUser}')
        # -------- GRÁFICO --------

        # -------- GRÁFICO --------
        self.canvas.get_tk_widget().place(relx=0, rely=0, relwidth=1, relheight=1)

class ManageCRUD(ManageGRAPH):
    def createDB_USER(self):
        try:
            connection = lite.connect(rf"database_content/{self.GlobalUser}.db")
            cur = connection.cursor()
            cur.execute(
                """
                CREATE TABLE IF NOT EXISTS tasks(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    status TEXT,
                    description TEXT
                )
                """
            )
        
            if os.path.exists(rf'database_content/{self.GlobalUser}.db') == True:
                self.status_db.configure(text="[ONLINE]", text_color=self.color_success)

            else:
                self.status_db.configure(text="[OFFLINE]", text_color=self.color_warning)
        
        except (Exception, AttributeError) as e:
            status_title = "[ERROR - SQLite 3]"
            status_message = f"{e}"
            rprint(f'[on white] [black] {status_title} [/black] [/on white][on red] [bold]{status_message}[/bold] [/on red]')

    def readMANAGECRUD(self):
        connection = lite.connect(rf"database_content/{self.GlobalUser}.db")
        with connection:
            cur = connection.cursor()
            command = "SELECT * FROM tasks"
            cur.execute(command)

            lista = []
            
            for item in cur.fetchall():
                lista.append(item)
                
            for row in self.listTreeView.get_children():
                self.listTreeView.delete(row)

            for value in lista:
                self.listTreeView.insert('', 'end', values=value)

            self.showGraph()

    def createCRUD(self):
        connection = lite.connect(rf"database_content/{self.GlobalUser}.db")
        with connection:
            self.manage_title = self.entry_manageTITLE.get().strip()
            self.manage_description = self.entry_manageDESCRIPTION.get().strip()

            if self.manage_title == "" and self.manage_description == "":
                messagebox.showerror(
                    title="Error de criação",
                    message="Os campos precisam ser preenchidos."
                )

            elif self.manage_title == "" or self.manage_description == "":
                messagebox.showerror(
                    title="Error de criação",
                    message="Preencha os campos de TÍTULO E DESCRIÇÃO."
                )

            else:
                cur = connection.cursor()
                command = f'INSERT INTO tasks (title, status, description) VALUES ("{self.manage_title}","EM ANDAMENTO", "{self.manage_description}")'
                cur.execute(command)

                self.entry_manageTITLE.delete(0, 'end')
                self.entry_manageDESCRIPTION.delete(0, 'end')

                messagebox.showinfo(
                    title="Nova Tarefa",
                    message="Uma nova tarefa foi adicionada."
                )

                connection.commit()
                self.readMANAGECRUD()
    
    def updateCRUD(self):
        connection = lite.connect(rf"database_content/{self.GlobalUser}.db")

        with connection:
            try:
                list_data = self.listTreeView.focus()
                list_dic = self.listTreeView.item(list_data)
                list_set = list_dic['values']

                self.task_id = list_set[0]
                self.task_status = list_set[2]

                cur = connection.cursor()

                if self.task_status[2] == "EM ANDAMENTO":
                    new_status = "FINALIZADA"
                    command = f'UPDATE tasks SET status="{new_status}" WHERE id={self.task_id}'

                else:
                    new_status = "EM ANDAMENTO"
                    command = f'UPDATE tasks SET status="{new_status}" WHERE id={self.task_id}'
                
                cur.execute(command)

            except IndexError:
                messagebox.showerror(
                    title="Erro",
                    message="Selecione a tarefa na tabela!"
                )
        
        connection.commit()
        self.readMANAGECRUD()

    def deleteCRUD(self):
        connection = lite.connect(rf"database_content/{self.GlobalUser}.db")

        with connection:
            try:
                list_data = self.listTreeView.focus()
                list_dic = self.listTreeView.item(list_data)
                list_set = list_dic['values']
                self.task_id = list_set[0]
                self.task_title = list_set[1]

                msg_box = messagebox.askquestion(
                    title="Apagar Tarefa", message=f"Deseja MESMO apagar a tarefa {self.task_title}?",
                    icon='warning'
                )

                if msg_box == 'yes':
                    cur = connection.cursor()
                    command = f'DELETE FROM tasks WHERE id={self.task_id}'
                    cur.execute(command)

                    messagebox.showinfo(
                        title="Apagar Tarefa",
                        message=f"Tarefa {self.task_title} DELETADA com sucesso!"
                    )
                
                self.readMANAGECRUD()

            except IndexError:
                messagebox.showerror(
                    title="Erro",
                    message="Selecione a tarefa na tabela!"
                )

        connection.commit()
        self.readMANAGECRUD()

class Manage(ManageCRUD):
    def autor(self):
        gitHub = "https://github.com/Baku-Stark"
        webbrowser.open_new(gitHub)

    def project(self):
        gitHub = "https://github.com/Baku-Stark/Portfolio-Projects/tree/main/Projetos/Python/Login%20and%20CRUD"
        webbrowser.open_new(gitHub)
    
    def returnLogin(self):
        # ===================================================
        # destruir os blocos da aplicação
        # ================= DESTROY
        self.menu_bar.destroy()
        self.frameCENTER_MANAGE.destroy()

        # ===================================================
        # construir os blocos da aplicação
        # ================= ENGINE
        self.root.title("LOGIN | REGISTRO")
        self.framesForm()
        self.loginForm()

    def MenuManage(self):
        self.menu_bar = Menu(self.root)
        self.root.configure(menu=self.menu_bar)

        self.Conta = Menu(self.menu_bar)
        self.Sobre = Menu(self.menu_bar)


        self.menu_bar.add_cascade(label=self.GlobalUser, menu=self.Conta)
        self.Conta.add_command(label="Recarregar Gráfico", command=self.showGraph)
        self.Conta.add_command(label="LOGOUT", command=self.returnLogin)

        self.menu_bar.add_cascade(label="Informações", menu=self.Sobre)
        self.Sobre.add_command(label="Autor do projeto", command=self.autor)
        self.Sobre.add_command(label="Sobre o projeto", command=self.project)

    def frameManage(self):
        self.frameCENTER_MANAGE = customtkinter.CTkFrame(
            self.root, fg_color=self.themePattern
        )

        self.frameLEFT_MANAGE = customtkinter.CTkFrame(self.frameCENTER_MANAGE, fg_color=self.themePattern2)
        self.frameRIGHT_MANAGE = customtkinter.CTkFrame(self.frameCENTER_MANAGE, fg_color=self.themePattern2)

        self.frameCENTER_MANAGE.place(relx=0.5, rely=0.53, relwidth=0.99, relheight=0.9, anchor=CENTER)
        self.frameLEFT_MANAGE.place(relx=0.005, rely=0.015,relwidth=0.49, relheight=0.97)
        self.frameRIGHT_MANAGE.place(relx=0.505, rely=0.015,relwidth=0.49, relheight=0.97)

    def widgets_frameLEFT_MANAGE(self):
        self.label_db = customtkinter.CTkLabel(
            self.frameLEFT_MANAGE, text="Banco de Dados:", font=('Arial', 10)
        )
        self.status_db = customtkinter.CTkLabel(
            self.frameLEFT_MANAGE, text="[reading...]", text_color=self.color_waiting
        )

        self.label_manageTITLE = customtkinter.CTkLabel(
            self.frameLEFT_MANAGE, text="Título da Tarefa", font=('Impact', 20)
        )
        self.entry_manageTITLE = customtkinter.CTkEntry(
            self.frameLEFT_MANAGE, placeholder_text="Compras, Consertar, etc..."
        )

        self.label_manageDESCRIPTION = customtkinter.CTkLabel(
            self.frameLEFT_MANAGE, text="Descrição", font=('Impact', 20)
        )
        self.entry_manageDESCRIPTION = customtkinter.CTkEntry(
            self.frameLEFT_MANAGE, placeholder_text="Comprar um teclado novo, etc..."
        )

        self.label_manageSEARCH = customtkinter.CTkLabel(
            self.frameLEFT_MANAGE, text="Procurar", font=('Impact', 20)
        )
        self.entry_manageSEARCH = customtkinter.CTkEntry(
            self.frameLEFT_MANAGE, placeholder_text="Titulo da tarefa..."
        )

        self.newTask_btn = customtkinter.CTkButton(
            self.frameLEFT_MANAGE, text="Nova Anotação",
            fg_color=("#111111", "#f0f8ff"), text_color=("#f0f8ff", "#111111"),
            hover_color=self.hover_btn
        )
        self.newTask_btn.configure(command=self.createCRUD)

        self.updateTask_btn = customtkinter.CTkButton(
            self.frameLEFT_MANAGE, text="Atualizar Anotação",
            fg_color=("#111111", "#f0f8ff"), text_color=("#f0f8ff", "#111111"),
            hover_color=self.hover_btn
        )
        self.updateTask_btn.configure(command=self.updateCRUD)

        self.deleteTask_btn = customtkinter.CTkButton(
            self.frameLEFT_MANAGE, text="Apagar Anotação",
            fg_color=("#111111", "#f0f8ff"), text_color=("#f0f8ff", "#111111"),
            hover_color=self.hover_btn
        )
        self.deleteTask_btn.configure(command=self.deleteCRUD)

        # LISTA [CRUD]
        c = 0
        colunas = ['ID', 'TÍTULO', 'STATUS','DESCRIÇÃO']
        listWidth = [10, 50, 50, 200]
        self.listTreeView = ttk.Treeview(
            self.frameLEFT_MANAGE, columns=colunas, show='headings', selectmode="extended"
        )
        self.scrollY = ttk.Scrollbar(
            self.frameLEFT_MANAGE, orient='vertical'
        )
        self.scrollY['command'] = self.listTreeView.yview
        self.listTreeView.configure(yscrollcommand=self.scrollY)

        for col in colunas:
            self.listTreeView.heading(c, text=col)
            self.listTreeView.column(c, width=listWidth[c], anchor='center')
            c+=1

        
        self.label_db.place(relx=0.01, rely=0.001)
        self.status_db.place(relx=0.15, rely=0.001)

        self.label_manageTITLE.place(relx=0.03, rely=0.05)
        self.entry_manageTITLE.place(relx=0.03, rely=0.10, relwidth=0.55)

        self.label_manageDESCRIPTION.place(relx=0.03, rely=0.20)
        self.entry_manageDESCRIPTION.place(relx=0.03, rely=0.25, relwidth=0.55)

        self.label_manageSEARCH.place(relx=0.03, rely=0.35)
        self.entry_manageSEARCH.place(relx=0.03, rely=0.40, relwidth=0.95)

        self.newTask_btn.place(relx=0.6, rely=0.05, relwidth=0.35)
        self.updateTask_btn.place(relx=0.6, rely=0.15, relwidth=0.35)
        self.deleteTask_btn.place(relx=0.6, rely=0.25, relwidth=0.35)

        self.listTreeView.place(relx=0.03, rely=0.46, relwidth=0.9, relheight=0.52)
        self.scrollY.place(relx=0.93, rely=0.46, relheight=0.52)

        self.createDB_USER()