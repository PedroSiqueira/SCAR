import getpass
import FingerPrint
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

# Tries to initialize the sensor
try:
    f = PyFingerprint('/dev/ttyAMA0', 57600, 0xFFFFFFFF, 0x00000000)
    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')
except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)

dao = Dao("scar.db")

while(True):
    menu()
    opcao = int(input())
    if(opcao==1):
        print(dao.readUsers())
    elif(opcao==2):
        usuario_id = input("Digita o id do usuário que queres editar")
        dao.updateUser(usuario_id)
    elif(opcao==3):
        usuario_id = input("Digita o id do novo usuário:")
        usuario_nome = input("Digita o nome do novo usuário:")
        usuario_senha = getpass.getpass("Digita a senha do novo usuário: ")
        usuario_digital = lerDigital()
        dao.createUsers(usuario_nome,usuario_id,usuario_senha,usuario_digital)
    elif(opcao==4):
        usuario_id = input("Digita o id do usuário que queres apagar")
        usuario = dao.readUser(usuario_id)
        apagarDigital(usuario.impressao_digital)
        dao.deleteUser(usuario_id)
    elif(opcao==5):
        usuario_id = input("Digita o id do usuário que queres ver")
        print(dao.readUser(usuario_id))
    elif(opcao==0):
        print("encerrando o programa...")
        break
    else:
        print("Opção não reconhecida...")
