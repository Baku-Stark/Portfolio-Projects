import sqlite3 as lite

# ----------------------------------------
# ATIVAR LISTA
con = lite.connect('database/database.bd')

# ----------------------------------------
# INSERIR INFORMAÇÕES
def insert(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO lista_telefonica(nome, ddd, telefone) VALUES (?, ?, ?)"
        cur.execute(query, i)

# ----------------------------------------
# ACESSAR INFORMAÇÕES
def acess():
    lista = []

    with con:
        cur = con.cursor()
        query = "SELECT * FROM lista_telefonica"
        cur.execute(query)
        info = cur.fetchall()

        for i in info:
            lista.append(i)
        
    return lista

# ----------------------------------------
# ATUALIZAR INFORMAÇÕES
def update(i):
    with con:
        cur = con.cursor()
        query = "UPDATE lista_telefonica SET nome=?, ddd=?, telefone=? WHERE id=?"
        
        cur.execute(query, i)

# ----------------------------------------
# DELETAR INFORMAÇÕES
def delete(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM lista_telefonica WHERE id=?"
        cur.execute(query, i)