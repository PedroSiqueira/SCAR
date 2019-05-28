from pyfingerprint.pyfingerprint import PyFingerprint

class FingerPrint: pass

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
