import sqlite3
from datetime import datetime


def conectar():
    return sqlite3.connect("financeiro.db", check_same_thread=False)


def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movimentacoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT,
        tipo TEXT,
        categoria TEXT,
        valor REAL,
        descricao TEXT
    )
    """)

    conn.commit()
    conn.close()


# ---------------- ADICIONAR ----------------
def adicionar(tipo, valor, categoria, descricao):
    conn = conectar()
    cursor = conn.cursor()

    data = datetime.now().strftime("%d/%m/%Y")

    # garante que valor sempre será número
    valor = float(valor)

    cursor.execute("""
        INSERT INTO movimentacoes (data, tipo, categoria, valor, descricao)
        VALUES (?, ?, ?, ?, ?)
    """, (data, tipo, categoria, valor, descricao))

    conn.commit()
    conn.close()


# ---------------- LISTAR ----------------
def listar():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM movimentacoes ORDER BY id DESC")
    dados = cursor.fetchall()

    conn.close()
    return dados