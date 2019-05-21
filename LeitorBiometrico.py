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
    i = int(input('Please enter the template position you want to compare: '))
    f.loadTemplate(i,2) # carrega no charbuffer2 o template i
    print('Now, provide your fingerprint...')
    while(not f.readImage()): pass
    f.convertImage(1) # carrega no charbuffer1 o template lido
    print('The matching score between the two templates is', f.compareCharacteristics())

except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))
    exit(1)
