#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
All rights reserved.

"""

import tempfile
from pyfingerprint.pyfingerprint import PyFingerprint


## Reads image and download it
##

## Tries to initialize the sensor
try:
    f = PyFingerprint('/dev/ttyAMA0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)

## Gets some sensor information
print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

## Tries to read image and download it
try:
    print('Waiting for finger...')

    ## Wait that finger is read
    while ( not f.readImage() ): pass

    if(input('press 1 to download image or anything else to download string... ')=='1'):
        print('Downloading image (this take a while)...')
        imageDestination =  tempfile.gettempdir() + '/fingerprint.bmp'
        f.downloadImage(imageDestination)
        print('The image was saved to "' + imageDestination + '".')
    else:
        f.convertImage() # joga a impressao do ImageBuffer para o CharBuffer
        print('Finger characteristics:')
        print(f.downloadCharacteristics()) # retorna o que está em CharBuffer

except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))
    exit(1)
