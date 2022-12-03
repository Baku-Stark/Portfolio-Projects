import sqlite3 as lite

# ===============================================
# CONEXÃO COM SQLITE3 [TABLE cadastro]
con = lite.connect("data/cadastro.db")

# ===============================================
# FUNÇÕES CRUD
# --- CRIAR UM NOVO CADASTRO
def createCRUD(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO cadastro (codigo, nome, telefone, cidade) VALUES (?, ?, ?, ?)"
        cur.execute(query, i)

# --- LER BANCO DE DADOS
def readCRUD():
    with con:
        lista = []

        cur = con.cursor()
        query = "SELECT * FROM cadastro"
        cur.execute(query)
        info = cur.fetchall()

        for i in info:
            lista.append(i)

        return lista

def readCrudCity():
    with con:
        lista_city = []

        cur = con.cursor()
        query = "SELECT cidade FROM cadastro"
        cur.execute(query)
        info = cur.fetchall()

        for i in info:
            lista_city.append(i)
        
        return lista_city

# --- ATUALIZAR CADASTRO
def updateCRUD(i):
    with con:
        cur = con.cursor()
        query = "UPDATE cadastro SET codigo=?, nome=?, telefone=?, cidade=? WHERE id=?"
        cur.execute(query, i)

# --- APAGAR CADASTRO
def deleteCRUD(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM cadastro WHERE id=?"
        cur.execute(query, i)

# --- BUSCAR CADASTRO
def buscarCRUD(i):
    with con:
        lista = []

        cur = con.cursor()
        query = f"""SELECT codigo, nome, telefone, cidade FROM cadastro WHERE nome LIKE "{i}" ORDER BY nome ASC"""
        cur.execute(query)
        info = cur.fetchall()

        for i in info:
            lista.append(i)

        return lista