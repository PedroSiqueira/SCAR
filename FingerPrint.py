from pyfingerprint.pyfingerprint import PyFingerprint
import time

def iniciarConexao(port = '/dev/ttyAMA0', baudRate = 57600, address = 0xFFFFFFFF, password = 0x00000000):
    try:
        f = PyFingerprint(port, baudRate, address, password)
        if ( f.verifyPassword() == False ):
            raise ValueError('A senha do leitor biométrico informada está errada!')
        return f
    except Exception as e:
        print('Leitor biométrico não pôde ser inicializado!')
        raise e

def salvarDigital(index = -1):
    try:
        f = iniciarConexao()
        print('Informa a digital:')
        while ( f.readImage() == False ): pass

        # joga o ImageBuffer para o CharBuffer1
        f.convertImage(0x01)

        #verifica se ja existe essa impressao digital
        result = f.searchTemplate()
        if ( result[0] >= 0 ):
            raise Exception('Digital já existe na posição', result[0])

        print('Ok, informa a digital novamente')
        time.sleep(2)

        while ( f.readImage() == False ): pass

        # joga o ImageBuffer para o CharBuffer2
        f.convertImage(0x02)

        # Compares the charbuffers
        if ( f.compareCharacteristics() == 0 ):
            raise Exception('Digitais não conferem')

        # Coloca em CharBuffer1 e CharBuffer2 suas características combinadas
        f.createTemplate()

        # Salva o CharBuffer na memória
        i = f.storeTemplate(index)
        print('Digital salva na posição', i)
        return i

    except Exception as e:
        print('Erro: ' + str(e))
        if input("Deseja tentar novamente? (s/n) ").lower()=='s':
            return salvarDigital(index)
        else: return -1

def apagarDigital(index):
    if index is None: return True
    try:
        f = iniciarConexao()
        if(f.deleteTemplate(index)):
            return True
    except Exception as e:
        print('Erro: ' + str(e))
