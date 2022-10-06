import sqlite3 as lite

# ----------------------------------------
# TABELA
con = lite.connect('database/database.bd')

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE lista_telefonica(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, ddd TEXT, telefone TEXT)")