import sqlite3

conn = sqlite3.connect("scar.db")

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS usuario
(nome TEXT NOT NULL, id INTEGER PRIMARY KEY, senha TEXT NOT NULL UNIQUE, impressao_digital TEXT)""")

cursor.execute("""CREATE TABLE IF NOT EXISTS horario
(horario_entrada TEXT, horario_saida TEXT,  usuario_id INTEGER NOT NULL,
FOREIGN KEY (usuario_id) REFERENCES usuario(id))""")

conn.close()
