from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview

# ----------------------------------------
# IMPORTAÇÃO DA "view.py"
from view import *

# =============================================
# CORES

# --- DARK MODE
dark_left = "#252525"
dark_bg = "#2F3136"
dark_right = "#252525"
dark_fg = "#f0f8ff"

# --- LIGHT MODE
light_left = "#ADAFB2"
light_bg = "#f0f8ff"
light_right = "#ADAFB2"
light_fg = "#111111"

# =============================================
# APLICAÇÃO
root = Tk()
mode_check = IntVar()

class App(Frame):
    def __init__(self, master):
        super().__init__()
        # =============================================
        # WIDGET
        root.title("Python - Lista Telefônica")
        root.geometry("570x500")
        root.iconbitmap("_img/pc.ico")
        root.resizable(width='false', height='false')

        # =============================================
        # FRAME ESQUERDO
        self.frame_left = Frame(
            root, bg=light_left, width=230, height=500
        )

        self.theme_btn = Checkbutton(
            root, text="Dark Mode", font=('Helvetica 12 bold'),
            bg=light_left, fg=light_fg, variable=mode_check,
            command=self.DarkMode
        )

        self.label_nome = Label(
            root, text="Nome*", font=('Poppins 10 bold'),
            bg=light_right, fg=light_fg)
        self.insert_nome = Entry(root)

        self.label_ddd = Label(
            root, text="DDD*", font=('Poppins 10 bold'),
            bg=light_right, fg=light_fg)
        self.insert_ddd = Entry(root)

        self.label_telefone = Label(
            root, text="Telefone*", font=('Poppins 10 bold'),
            bg=light_right, fg=light_fg)
        self.insert_telefone = Entry(root)

        self.descLabel = Label(
            root, bg=light_left, fg=light_fg,
            font=('Ivy 10 bold'), justify='left'
        )
        self.descLabel['text'] = "Criador do projeto: Baku-Stark\nProjeto: Lista Telefônica(CRUD)\nPython Version: 3.10"

        # =============================================
        # FRAME CENTRO
        self.frame_center = Frame(
            root, bg=light_bg, width=340, height=500
        )

        self.btn_insert = Button(
            root, text="Inserir", font=('Arial 15 bold'),
            fg=light_fg, bg=light_left, relief='raised', overrelief='ridge', command=self.create
        )

        self.btn_update = Button(
            root, text="Atualizar", font=('Arial 15 bold'),
            fg=light_fg, bg=light_left, relief='raised', overrelief='ridge', command=self.updateSys
        )

        self.btn_delete = Button(
            root, text="Deletar", font=('Arial 15 bold'),
            fg=light_fg, bg=light_left, relief='raised', overrelief='ridge', command=self.deleteSys
        )

        # =============================================
        # PAINEL
        self.frame_left.grid(row=0, column=1)
        self.theme_btn.place(x=0, y=10)
        self.label_nome.place(x=20, y=50)
        self.insert_nome.place(x=20, y=70)
        # -----------------
        self.label_ddd.place(x=20, y=100)
        self.insert_ddd.place(x=20, y=120)
        # -----------------
        self.label_telefone.place(x=20, y=150)
        self.insert_telefone.place(x=20, y=170)
        # -----------------
        self.descLabel.place(x=20, y=250)

        self.frame_center.grid(row=0, column=2)
        self.btn_insert.place(x=235, y=250)
        self.btn_update.place(x=350, y=250)
        self.btn_delete.place(x=480, y=250)

        self.show()

    # =============================================
    # FUNÇÕES
    def DarkMode(self):
        check = mode_check.get()

        if check == 1:
            self.theme_btn['bg'] = dark_left
            self.theme_btn['fg'] = dark_fg

            self.frame_left['bg'] = dark_left
            self.label_nome['bg'] = dark_left
            self.label_nome['fg'] = dark_fg
            self.label_ddd['bg'] = dark_left
            self.label_ddd['fg'] = dark_fg
            self.label_telefone['bg'] = dark_left
            self.label_telefone['fg'] = dark_fg
            self.descLabel['bg'] = dark_left
            self.descLabel['fg'] = dark_fg

            self.frame_center['bg'] = dark_bg
            self.btn_insert['bg'] = dark_left
            self.btn_insert['fg'] = dark_fg
            self.btn_update['bg'] = dark_left
            self.btn_update['fg'] = dark_fg
            self.btn_delete['bg'] = dark_left
            self.btn_delete['fg'] = dark_fg

            self.btn_confirmar['bg'] = dark_left
            self.btn_confirmar['fg'] = dark_fg
        
        else:
            self.theme_btn['bg'] = light_left
            self.theme_btn['fg'] = light_fg

            self.frame_left['bg'] = light_left
            self.label_nome['bg'] = light_left
            self.label_nome['fg'] = light_fg
            self.label_ddd['bg'] = light_left
            self.label_ddd['fg'] = light_fg
            self.label_telefone['bg'] = light_left
            self.label_telefone['fg'] = light_fg
            self.descLabel['bg'] = light_left
            self.descLabel['fg'] = light_fg

            self.frame_center['bg'] = light_bg
            self.btn_insert['bg'] = light_left
            self.btn_insert['fg'] = light_fg
            self.btn_update['bg'] = light_left
            self.btn_update['fg'] = light_fg
            self.btn_delete['bg'] = light_left
            self.btn_delete['fg'] = light_fg

            self.btn_confirmar['bg'] = light_left
            self.btn_confirmar['fg'] = light_fg

    # ----- FUNÇÃO [-MOSTRAR-] 
    global list_tel

    def show(self):
        global list_tel
        lista = acess()
        
        tabela_head = ['ID', 'Nome', 'DDD', 'Telefone']
        
        hd = ["nw", "nw", "nw", "nw"]
        h = [30, 100, 40, 170]
        n = 0

        list_tel = Treeview(
            root, selectmode="extended", columns=tabela_head, show="headings"
        )

        list_tel.place(x=230, y=0)

        for col in tabela_head:
            list_tel.heading(col, text=col.title(), anchor=CENTER)
            list_tel.column(col, width=h[n], anchor=hd[n])

            n += 1

        for item in lista:
            list_tel.insert('', 'end', values=item)

        # ----- FUNÇÃO  [-CRIAR-]
    def create(self):
        nome = self.insert_nome.get()
        ddd = self.insert_ddd.get()
        tel = self.insert_telefone.get()

        lista = [nome, ddd, tel]
        
        if len(tel) > 9:
            messagebox.showerror(title="Erro De Registro",
            message="O número de telefone está incorreto!")
        
        elif len(tel) == 8:
            messagebox.showerror(title="Erro De Contagem",
            message="O número de telefone possui 8 digitos. O número 9 foi adicionado no ínicio!")
            newTel = "9" + tel
            print(f'({ddd}){newTel[0:5]}-{newTel[5:]}')

            print('\033[36m(Commit Realizado!)\033[m')
            print('')

            newList = [nome, ddd, newTel]

            insert(newList)
            self.insert_nome.delete(0, 'end')
            self.insert_ddd.delete(0, 'end')
            self.insert_telefone.delete(0, 'end')

            messagebox.showinfo(title="Inserção conluída",
            message="O cadastro foi realizado com sucesso!") 

        elif len(tel) < 8:
            messagebox.showerror(title="Erro De Registro",
            message="O número de telefone possui a contagem de dígitos menor que 8!")
        
        elif nome == "":
            messagebox.showerror(
                title="Erro De Registro(nome)",
                message="O usuário precisa inserir um nome!"
            )

        elif len(ddd) > 3:
            messagebox.showerror(
                title="Erro De Registro(DDD)",
                message="O DDD está incorreto!"
            )
        
        elif ddd == "":
            messagebox.showerror(
                title="Erro De Registro(DDD)",
                message="O usuário precisa inserir o DDD!"
            )

        else:
            print('\033[36m(Commit Realizado!)\033[m')
            print('')

            insert(lista)

            self.insert_nome.delete(0, 'end')
            self.insert_ddd.delete(0, 'end')
            self.insert_telefone.delete(0, 'end')

            messagebox.showinfo(title="Inserção conluída",
            message="O cadastro foi realizado com sucesso!")

        self.show()


    # ----- FUNÇÃO [-ATUALIZAR-]
    def updateSys(self):
        try:
            treevData = list_tel.focus()
            treevDisc = list_tel.item(treevData)
            treevList = treevDisc['values']

            valor_id = treevList[0]

            self.insert_nome.delete(0, 'end')
            self.insert_ddd.delete(0, 'end')
            self.insert_telefone.delete(0, 'end')

            self.insert_nome.insert(0, treevList[1])
            self.insert_ddd.insert(0, treevList[2])
            self.insert_telefone.insert(0, treevList[3])
            
            # ---- REWRITE PROCESS
            def updateCheck():
                nome = self.insert_nome.get()
                ddd = self.insert_ddd.get()
                telefone = self.insert_telefone.get()
                
                listaUp = [nome, ddd, telefone, valor_id]

                if nome == "":
                    messagebox.showerror(
                        title="Erro De Registro(nome)",
                        message="O usuário precisa inserir um nome!")
                
                else:
                    update(listaUp)
                    messagebox.showinfo(
                        title="Atualização - Sucesso",
                        message="A atualização foi realizada com sucesso!")

                    self.insert_nome.delete(0, 'end')
                    self.insert_ddd.delete(0, 'end')
                    self.insert_telefone.delete(0, 'end')
                
                self.show()
            
            self.btn_confirmar = Button(
                root, text="Confirmar",
                font=('Arial 15 bold'), fg=light_fg,
                bg=light_left, relief='raised',
                overrelief='ridge', command=updateCheck)

            self.btn_confirmar.place(x=350, y=350)

        except IndexError:
            messagebox.showerror(title="Erro",
            message="Selecione algum elemento dos dados na lista!")
    
    # ----- FUNÇÃO [-APAGAR-]
    def deleteSys(self):
        try:
            treevData = list_tel.focus()
            treevDisc = list_tel.item(treevData)
            treevList = treevDisc['values']

            valor_id = [treevList[0]]
            
            delete(valor_id)
            messagebox.showinfo(title="Apagar", message="Função delete realizada!")

            self.show()
        
        except IndexError:
            messagebox.showerror(title="Erro",
            message="Selecione algum elemento dos dados na lista!")
# =============================================
# ATIVAÇÃO DO ROOT
if __name__ == '__main__':
    app = App(root)
    app.master.mainloop()