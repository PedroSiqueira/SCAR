"""
este programa lê do stdin as fingerprint characteristics e procura quais delas correpondem ao fingerprint lido pelo sensor fingerprint
"""

from pyfingerprint.pyfingerprint import PyFingerprint
from sys import stdin

## Tries to initialize the sensor
try:
    f = PyFingerprint('/dev/ttyAMA0', 115200, 0xFFFFFFFF, 0x00000000)
    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')
except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)


try:
    print('Provide your fingerprint...')
    while(not f.readImage()): pass
    f.convertImage(1) # carrega no charbuffer1 o template lido
    print("loading fingerprint characteristics...")
    for line in stdin: # para cada linha da entrada padrao (termina a leitura no EOF)
        f.uploadCharacteristics(2,eval(line))
        print('The matching score between the two templates is', f.compareCharacteristics())


except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))
    exit(1)
