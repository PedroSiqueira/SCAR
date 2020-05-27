import RPi.GPIO as GPIO
from Dao import Dao
from Keypad import Keypad
from Interface import Interface
from pyfingerprint.pyfingerprint import PyFingerprint

"""
este é o programa que gerencia o controle e acesso de usuários
"""
if __name__ == '__main__':
    dao = Dao("scar.db")
    interface = Interface()
    keypad = Keypad(ROWS=[16,18,22,24],COLS=[26,32,36])
    keys = ""

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
    while(True):
        try:
            button=keypad.getKey() # le do teclado matricial
            if(button is not None):
                interface.blinkOnce()
                if(button == '*'): # se for '*', limpa o buffer de entrada
                    keys = ""
                elif(button == '#'): # se for '#', procura pela senha
                    if keys=="7643": # codigo para encerrar o programa
                        break
                    elif dao.allowAccessByPassword(keys):
                        print("Authorized access by password")
                        interface.acessoAutorizado(1)
                    else:
                        print("Unauthorized access by password")
                        interface.acessoDesautorizado(1)
                    keys = ""
                else: # se for um numero
                    keys += button

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
            interface.erro()

    GPIO.cleanup()
    print("program quitted")
