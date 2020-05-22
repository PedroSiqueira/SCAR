from Dao import Dao
from Keys import Keys
from Interface import Interface
from pynput import keyboard
from pyfingerprint.pyfingerprint import PyFingerprint

"""
este é o programa que gerencia o controle e acesso de usuários
"""

dao = Dao("scar.db")
interface = Interface()
keys = Keys(dao, interface)

## Initialize keyboard listener
listener = keyboard.Listener(on_release=keys.on_release, suppress=True)
listener.start()

# Tries to initialize the sensor
try:
    f = PyFingerprint('/dev/ttyAMA0', 57600, 0xFFFFFFFF, 0x00000000)
    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')
        print("fingerprint initialized")
except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)

print("Waiting for fingerprint or password...")
while(not keys.quit):
    try:
        # se ha uma impressao digital no ImageBuffer
        if(f.readImage()):
            # joga o ImageBuffer no CharBuffer1
            f.convertImage(0x01)

            # procura pelo CharBuffer1 na memoria do sensor
            result = f.searchTemplate()
            index = result[0]

            # se encontrou a impressao digital
            if ( index >= 0 ):
                # tenta salvar no banco de dados o horario de acesso
                if(dao.allowAccessByFingerPrint(index)):
                    print("Authorized access on fingerprint", index)
                    interface.acessoAutorizado()
                # nao conseguiu salvar o horario no banco de dados
                else:
                    print("Could not find user in database")
                    interface.acessoAutorizado(2)
            else:
                print("Unauthorized access")
                interface.acessoDesautorizado()

    except Exception as e:
        print(e)
        interface.erro(e)
