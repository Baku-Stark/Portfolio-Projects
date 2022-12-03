import sqlite3 as lite

# ===============================================
# CONEXÃO COM SQLITE3
con = lite.connect("data/cadastro.db")

# ===============================================
# CRIAÇÃO DA TABELA
def cadastroCreate():
    try:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS cadastro(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo TEXT,
                nome TEXT,
                telefone TEXT,
                cidade TEXT
            )
            """)
    except Exception as e:
        print(f"\033[1;31m[Falha ao criar a tabela: {e}]\033[m")
    else:
        print("\033[1;36m[Tabela criada com sucesso!]\033[m")