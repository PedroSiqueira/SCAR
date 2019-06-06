from Dao import Dao
from Keys import Keys
from pynput import keyboard
from pyfingerprint.pyfingerprint import PyFingerprint

dao = Dao("scar.db")
keys = Keys(dao)

## Initialize keyboard listener
listener = keyboard.Listener(on_release=keys.on_release, suppress=True)
listener.start()

# Tries to initialize the sensor
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
            search()
    except Exception as e:
        print(e)
