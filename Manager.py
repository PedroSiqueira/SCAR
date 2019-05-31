import getpass
import FingerPrint as fp
from Dao import Dao

def menu():
    print("###################")
    print("Escolha uma opção")
    print("###################")
    print("1) Listar usuários")
    print("2) Editar usuário")
    print("3) Criar usuário")
    print("4) Apagar usuário")
    print("5) Listar usuário")
    print("0) Sair do programa")

dao = Dao("scar.db")

while(True):
    menu()
    opcao = int(input())
    if(opcao==1):
        print(dao.readUsers())
    elif(opcao==2):
        usuario_id = input("Digita o id do usuário que queres editar")
        usuario_nome = input("Digita o novo nome do usuário (deixa em branco para não alterar):")
        usuario_senha = getpass.getpass("Digita a nova senha do usuário (deixa em branco para não alterar): ")
        usuario = dao.readUser(usuario_id)
        if(input("Digita 's' se quiseres alterar a digital").lower=='s'):
            usuario_digital = fp.alterarDigital(usuario.impressao_digital) # a impressao_digital pode ser None. a funcao alterarDigital devolve o indice onde a digital foi salva
        else: usuario_digital = usuario.impressao_digital
        dao.updateUser(usuario_id,usuario_nome,usuario_senha, usuario_digital)
    elif(opcao==3):
        usuario_id = input("Digita o id do novo usuário:")
        usuario_nome = input("Digita o nome do novo usuário:")
        usuario_senha = getpass.getpass("Digita a senha do novo usuário: ")
        usuario_digital = fp.criarDigital()
        dao.createUser(usuario_nome,usuario_id,usuario_senha,usuario_digital)
    elif(opcao==4):
        usuario_id = input("Digita o id do usuário que queres apagar")
        usuario = dao.readUser(usuario_id)
        fp.apagarDigital(usuario.impressao_digital)
        dao.deleteUser(usuario_id)
    elif(opcao==5):
        usuario_id = input("Digita o id do usuário que queres ver")
        print(dao.readUser(usuario_id))
    elif(opcao==0):
        print("encerrando o programa...")
        break
    else:
        print("Opção não reconhecida...")
