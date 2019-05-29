"""
este programa imprime todas as fingerprint characteristics armazenadas no sensor de fingerprint
"""


from pyfingerprint.pyfingerprint import PyFingerprint

## Tries to initialize the sensor
try:
    f = PyFingerprint('/dev/ttyAMA0', 57600, 0xFFFFFFFF, 0x00000000)
    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')
except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)


try:
    templates = f.getTemplateIndex(0)
    for i in range(0, len(templates)):
        if(templates[i]):
            f.loadTemplate(i)
            print(f.downloadCharacteristics())

except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))
    exit(1)
