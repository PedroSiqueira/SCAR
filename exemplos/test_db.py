import sqlite3
import hashlib
import datetime
import string
import random
import datetime

""" cria 200 usuarios e 10000 horarios para verificar o tamanho do banco de dados"""
def main():
    with sqlite3.connect("scar.db") as con:
        for i in range(200):
            print("creating usuario ",i)
            createUser(con,
                randomString(128),
                randomString(16,string.digits),
                randomString(8,string.digits),
                i
            )
        print("usuarios criados")
        con.commit()

        users = con.cursor().execute("SELECT * FROM usuario").fetchmany(100)

        for i in range(10000):
            print("creating horario ",i)
            createHorario(con,
                datetime.datetime.now(),
                datetime.datetime.now()+datetime.timedelta(days = 10),
                users[random.randint(0,99)][1]
            )
        print("horarios criados")
        con.commit()

def randomString(stringLength,string_type=string.ascii_letters):
    """Generate a random string with the combination of lowercase and uppercase letters """
    letters = string_type
    return ''.join(random.choice(letters) for i in range(stringLength))

def createUser(con, nome, id, senha, impressao_digital = None):
    senha = hashlib.md5(senha.encode('utf8')).hexdigest()
    con.cursor().execute("""
        INSERT INTO usuario
        (nome, id, senha, impressao_digital)
        VALUES (?,?,?,?)""",
        (nome, id, senha, impressao_digital)
    )
    return True

def createHorario(con, horario_entrada,horario_saida,index):
    con.cursor().execute(
        """INSERT INTO horario
        (horario_entrada,horario_saida, usuario_id)
        VALUES (?,?,?)"""
        , (horario_entrada,horario_saida, index)
    )
    #print(horario_entrada,horario_saida,index)
    return True

class Dao:
    """db_nome: caminho do banco de dados a ser aberto"""
    def __init__(self, db_name):
        self.db_name = db_name

    def deleteUser(self, id):
        with sqlite3.connect(self.db_name) as con:
            con.cursor().execute("DELETE FROM usuario WHERE id = ?",(id,))
            con.commit()

    def readUser(self, id):
        with sqlite3.connect(self.db_name) as con:
            return con.cursor().execute("SELECT * FROM usuario WHERE id = ?", (id,)).fetchone()

    def updateUser(self, id, novo_id, nome, senha, impressao_digital=-1):
        with sqlite3.connect(self.db_name) as con:
            con.cursor().execute("UPDATE usuario SET impressao_digital = ? WHERE id = ? LIMIT 1", (impressao_digital, id))
            if(nome):
                con.cursor().execute("UPDATE usuario SET nome = ? WHERE id = ? LIMIT 1", (nome, id))
            if(senha):
                senha = hashlib.md5(senha.encode('utf8')).hexdigest()
                con.cursor().execute("UPDATE usuario SET senha = ? WHERE id = ? LIMIT 1", (senha, id))
            if(novo_id):
                con.cursor().execute("UPDATE usuario SET id = ? WHERE id = ? LIMIT 1", (novo_id, id))
            con.commit()
            return True

if __name__ == "__main__":
    main()
