import sqlite3
import hashlib
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


    def allowAccessByPassword(self, password, dontLog = False):
        """
        Se encontrar a senha password no banco de dados, registra no banco o horario da consulta e o id do usuario de senha password e retorna True, senao, retorna False. Se dontLog for True, nao registra o horario de consulta no banco, mesmo se encontrar a senha password.
        """
        with sqlite3.connect(self.db_name) as con:
            password = hashlib.md5(password.encode('utf8')).hexdigest()
            usuario = con.cursor().execute('SELECT id FROM usuario WHERE senha = ?'
                                           , (password,)).fetchone()
            if(usuario):
                if(not dontLog):
                    con.cursor().execute(
                        """INSERT INTO horario (horario_entrada, usuario_id)
                        VALUES (?,?)"""
                        , (datetime.datetime.now(), usuarios[0])
                    )
                return True
            else: return False

    def createUser(self, nome, id, senha, impressao_digital = None):
        senha = hashlib.md5(senha.encode('utf8')).hexdigest()
        with sqlite3.connect(self.db_name) as con:
            con.cursor().execute("""
                INSERT INTO usuario
                (nome, id, senha, impressao_digital)
                VALUES (?,?,?,?)""",
                (nome, id, senha, impressao_digital)
            )
            con.commit()
            return True

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
                senha = hashlib.md5(senha.encode('utf8')).hexdigest()
                con.cursor().execute("UPDATE usuario SET senha = ? WHERE id = ? LIMIT 1", (senha, id))
            if(novo_id):
                con.cursor().execute("UPDATE usuario SET id = ? WHERE id = ? LIMIT 1", (novo_id, id))
            con.commit()
            return True
