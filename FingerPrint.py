from pyfingerprint.pyfingerprint import PyFingerprint

def search():
    ## Converts ImageBuffer to characteristics and stores it in charbuffer 1
    f.convertImage(0x01)

    # procura por CharBuffer no banco de impressoes
    result = f.searchTemplate()

    positionNumber = result[0]
    accuracyScore = result[1]

    if ( positionNumber == -1 ):
        print('No match found!')
    else:
        print('Found template at position #' + str(positionNumber))

    print('The accuracy score is: ' + str(accuracyScore))

def iniciarConexao(port = '/dev/ttyAMA0', baudRate = 57600, address = 0xFFFFFFFF, password = 0x00000000):
    # Tries to initialize the sensor
    try:
        f = PyFingerprint(port, baudRate, address, password)
        if ( f.verifyPassword() == False ):
            raise ValueError('A senha do leitor biométrico informada está errada!')
        return f
    except Exception as e:
        print('Leitor biométrico não pôde ser inicializado!')
        print('Erro: ' + str(e))
        return None

def criarDigital():
    f = iniciarConexao()
    try:
        print('Informa tua digital:')
        while ( f.readImage() == False ): pass

        # joga o ImageBuffer para o CharBuffer1
        f.convertImage(0x01)

        #verifica se ja existe essa impressao digital
        result = f.searchTemplate()
        if ( result[0] >= 0 ):
            print('Digital já existe na posição #' + str(positionNumber))
            return

        print('Ok, informa tua digital novamente')

        ## Wait that finger is read again
        while ( f.readImage() == False ):
            pass

        ## Converts read image to characteristics and stores it in charbuffer 2
        f.convertImage(0x02)

        ## Compares the charbuffers
        if ( f.compareCharacteristics() == 0 ):
            raise Exception('Fingers do not match')

        ## Creates a template
        f.createTemplate()

        ## Saves template at new position number
        positionNumber = f.storeTemplate()
        print('Finger enrolled successfully!')
        print('New template position #' + str(positionNumber))

    except Exception as e:
        print('Operation failed!')
        print('Exception message: ' + str(e))
        exit(1)
