import sqlite3
import bcrypt
import datetime

class Dao:
    def __init__(self, db_name):
        self.db_name = db_name

    def allowAccessByFingerPrint(self, index):
        with sqlite3.connect(self.db_name) as con:
            # verifica se existe um usuario com tal impressao digital
            usuario = con.cursor().execute('SELECT id FROM usuario WHERE impressao_digital = ?', (index,)).fetchone()
            # se existir, autoriza o acesso e salva o horario
            if(usuario):
                con.cursor().execute("INSERT INTO horario (horario_entrada, usuario_id) VALUES (?,?)",(datetime.datetime.now(),usuario[0]))
                return True
            else: return False

    def allowAccessByPassword(self, password):
        with sqlite3.connect(self.db_name) as con:
            # como o banco nao salva a senha, mas o salted hash  dela, eh necessario buscar todos os salted hash do banco, e comparar cada um com a senha providenciada
            usuarios = con.cursor().execute('SELECT id,senha FROM usuario').fetchall()
            i=0
            for i,u in usuarios:
                # se password confere com a senha em u, encerra a busca antes do final
                if bcrypt.checkpw(password.encode('utf8'), u[1]):
                    break
            # se encerrou a busca antes do final, autoriza acesso e salva o horario
            if(i<len(usuarios)):
                con.cursor().execute("INSERT INTO horario (horario_entrada, usuario_id) VALUES (?,?)",(datetime.datetime.now(),usuarios[i][0]))
                return True
            else: return False

    def createUser(self, nome, id, senha, impressao_digital = None):
        senha = bcrypt.hashpw(senha.encode('utf8'), bcrypt.gensalt())
        with sqlite3.connect(self.db_name) as con:
            con.cursor().execute("""
                INSERT INTO usuario
                (nome, id, senha, impressao_digital)
                VALUES (?,?,?,?)""",
                (nome, id, senha, impressao_digital)
            )
            con.commit()
            print("Dados inseridos com sucesso.")

    def deleteUser(self, id):
        with sqlite3.connect(self.db_name) as con:
            con.cursor().execute("DELETE FROM usuario WHERE id = ?",(id,))
            con.commit()

    def readUser(self, id):
        with sqlite3.connect(self.db_name) as con:
            return con.cursor().execute("SELECT * FROM usuario WHERE id = ?", (id,)).fetchone()

    def readUsers(self):
        with sqlite3.connect(self.db_name) as con:
            return con.cursor().execute("SELECT * FROM usuario").fetchall()

    def updateUser(self, id, novo_id, nome, senha, impressao_digital=-1):
        with sqlite3.connect(self.db_name) as con:
            con.cursor().execute("UPDATE usuario SET impressao_digital = ? WHERE id = ? LIMIT 1", (impressao_digital, id))
            if(nome):
                con.cursor().execute("UPDATE usuario SET nome = ? WHERE id = ? LIMIT 1", (nome, id))
            if(senha):
                senha = bcrypt.hashpw(senha.encode('utf8'), bcrypt.gensalt())
                con.cursor().execute("UPDATE usuario SET senha = ? WHERE id = ? LIMIT 1", (senha, id))
            if(novo_id):
                con.cursor().execute("UPDATE usuario SET id = ? WHERE id = ? LIMIT 1", (novo_id, id))
            con.commit()
            print("Dados atualizados com sucesso.")
