import getpass
import FingerPrint as fp
from Dao import Dao
import os

def menu():
    print("###################")
    print("Escolha uma opção")
    print("###################")
    print("1) Listar usuários")
    print("2) Listar usuário")
    print("3) Editar usuário")
    print("4) Criar usuário")
    print("5) Apagar usuário")
    print("6) Pesquisar senha")
    print("0) Sair do programa")

dao = Dao("scar.db")

while(True):
    menu()
    opcao = input()
    if(opcao=='1'):
        os.system('clear') # limpa a tela (funciona apenas no linux)
        for user in dao.readUsers():
            print(user)
    elif(opcao=='2'):
        usuario_id = input("Informa o id do usuário que queres ver: ")
        print(dao.readUser(usuario_id))
    elif(opcao=='3'):
        usuario_id = input("Informa o id do usuário que queres editar: ")

        usuario = dao.readUser(usuario_id)
        if(usuario is None):
            print("Este usuário não foi encontrado")
            continue

        usuario_novo_id = input("Informa o novo id do usuário (deixa em branco para não alterar): ")
        usuario_nome = input("Informa o novo nome do usuário (deixa em branco para não alterar): ")
        usuario_senha = getpass.getpass("Informa a nova senha do usuário (deixa em branco para não alterar): ")
        if(input("Digita 's' se quiseres alterar a digital: ").lower()=='s'):
            usuario_digital = fp.salvarDigital(usuario[3])
        else: usuario_digital = usuario[3]
        dao.updateUser(usuario_id, usuario_novo_id, usuario_nome,usuario_senha, usuario_digital)
        print("Usuário",usuario_id, "alterado com sucesso!")
    elif(opcao=='4'):
        usuario_id = input("Informa o id do novo usuário: ")
        usuario_nome = input("Informa o nome do novo usuário: ")
        usuario_senha = getpass.getpass("Informa a senha do novo usuário: ")
        usuario_digital = fp.salvarDigital()
        dao.createUser(usuario_nome, usuario_id, usuario_senha, usuario_digital)
        print("Usuário",usuario_id, "salvo com sucesso!")
    elif(opcao=='5'):
        usuario_id = input("Informa o id do usuário que queres apagar: ")
        usuario = dao.readUser(usuario_id)
        if(usuario is None): print("Este usuário não foi encontrado")
        elif fp.apagarDigital(usuario[3]):
            dao.deleteUser(usuario_id)
            print("Usuário",usuario_id, "apagado com sucesso!")
        else:
            print("Não foi possível apagar usuário", usuario_id)
    elif(opcao=='6'):
        usuario_senha = getpass.getpass("Informa a senha queres pesquisar: ")
        if(dao.allowAccessByPassword(usuario_senha, True)):
            print("essa senha existe")
        else: print("essa senha NÃO existe")
    elif(opcao=='0'):
        print("encerrando o programa...")
        break
    else:
        print("Opção não reconhecida...")
