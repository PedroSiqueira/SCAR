import traceback
import RPi.GPIO as GPIO

"""
esta classe conecta ao teclado membrana
"""
class Keypad:
    def __init__(self, gpiomode, ROWS, COLS):
        self.ROWS=ROWS
        self.COLS=COLS
        GPIO.setmode(gpiomode)
        if(len(self.ROWS)!=4):
            raise ValueError('Number of rows not supported')
        if(len(self.COLS)==3):
            self.MATRIX = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
        elif(len(self.COLS)==4):
            self.MATRIX = [[1,2,3,'A'],[4,5,6,'B'],[7,8,9,'C'],['*',0,'#','D']]
        else:
            raise ValueError('Number of columns not supported')

        for j in self.COLS:
            GPIO.setup(j, GPIO.OUT)
            GPIO.output(j, 1)

        for i in self.ROWS:
            GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def getKey(self):
        button = None
        for j in range(len(self.COLS)):
            GPIO.output(self.COLS[j], 0)
            for i in range(len(self.ROWS)):
                if(GPIO.input(self.ROWS[i])==0):
                    button = self.MATRIX[i][j]
                    while(GPIO.input(self.ROWS[i])==0):
                        pass
            GPIO.output(self.COLS[j], 1)
        return button

if __name__ == '__main__':
    try:
        keypad = Keypad(GPIO.BOARD,ROWS=[16,18,22,24],COLS=[26,32,36])
        button=None
        while(button != '*'):
            button=keypad.getKey()
            if(button is not None):
                print("ola", button)
    except: traceback.print_exc()
    GPIO.cleanup()
    print("the end")
