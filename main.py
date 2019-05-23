from Keys import Keys
from pynput import keyboard
from pyfingerprint.pyfingerprint import PyFingerprint

keys = Keys()

## Initialize keyboard listener
listener = keyboard.Listener(on_release=keys.on_release, suppress=True)
listener.start()

## Tries to initialize the sensor
try:
    f = PyFingerprint('/dev/ttyAMA0', 57600, 0xFFFFFFFF, 0x00000000)
    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')
except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)

print("fingerprint initialized")
while(True):
    try:
        if(f.readImage()):
                ## Converts ImageBuffer to characteristics and stores it in charbuffer 1
                f.convertImage(0x01)

                ## Searchs template
                # procura por CharBuffer no banco de impressoes
                result = f.searchTemplate()

                positionNumber = result[0]
                accuracyScore = result[1]

                if ( positionNumber == -1 ):
                    print('No match found!')
                    print('The accuracy score is: ' + str(accuracyScore))
                    exit(0)
                else:
                    print('Found template at position #' + str(positionNumber))
                    print('The accuracy score is: ' + str(accuracyScore))
    except Exception as e:
        print(e)
