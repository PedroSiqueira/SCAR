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

def initialize_fingerprint(port = '/dev/ttyAMA0', baudRate = 57600, address = 0xFFFFFFFF, password = 0x00000000):
    # Tries to initialize the sensor
    try:
        f = PyFingerprint(port, baudRate, address, password)
        if ( f.verifyPassword() == False ):
            raise ValueError('The given fingerprint sensor password is wrong!')
        return f
    except Exception as e:
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        return None
