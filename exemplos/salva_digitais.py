"""
este programa lê do stdin as fingerprint characteristics e as salva no sensor fingerprint
"""

from pyfingerprint.pyfingerprint import PyFingerprint
from sys import stdin

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
    print("loading fingerprint characteristics...")
    i=0
    hasTemplate = f.getTemplateIndex(0)
    for line in stdin: # para cada linha da entrada padrao (termina a leitura no EOF)
        while(i < f.getStorageCapacity()): # o indice i vai parar quando encontrar um template vazio
            if(not hasTemplate[i]): break
            i += 1
        if(i>=f.getStorageCapacity()): break
        f.uploadCharacteristics(1,eval(line))
        f.storeTemplate(i)
        print("saved fingerprint at ", i)
        i+=1


except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))
    exit(1)
