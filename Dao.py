import sqlite3
import bcrypt

class Dao:
    def __init__(self, db_name):
        self.db_name = db_name

    def allowAccessByPassword(self, password):
        with sqlite3.connect(self.db_name) as con:
            # como o banco nao salva a senha, mas o salted hash  dela, eh necessario buscar todos os salted hash do banco, e comparar cada um com a senha providenciada
            senhas = con.cursor().execute('SELECT senha FROM usuario').fetchall()
            liberado = False
            for senha in senhas:
                if bcrypt.checkpw(password.encode('utf8'), senha[0]):
                    liberado = True
                    break
            if(liberado): print("acesso liberado!")
            else: print("acesso bloqueado")

    def createUser(self, nome, id, senha, impressao_digital = None):
        try:
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
        except Exception as e:
            print("Erro", e)
