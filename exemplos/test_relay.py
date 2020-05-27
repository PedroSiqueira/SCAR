import RPi.GPIO as GPIO

def desligar():
    GPIO.output(ledAzul, GPIO.LOW)
    GPIO.output(ledVerde, GPIO.LOW)

ledVerde = 35
ledAzul = 37
fechadura = 31

GPIO.setmode(GPIO.BOARD)

GPIO.setup(ledVerde, GPIO.OUT)
GPIO.setup(ledAzul, GPIO.OUT)
GPIO.setup(fechadura, GPIO.OUT)

while(True):
    r = input("S or N? (anything else to exit)")
    desligar()
    if(r.lower()=="s"):
        GPIO.output(ledAzul, GPIO.HIGH)
        GPIO.output(fechadura, GPIO.HIGH)
    elif(r.lower()=="n"):
        GPIO.output(ledVerde, GPIO.HIGH)
        GPIO.output(fechadura, GPIO.LOW)
    else:
        break;

desligar()
GPIO.output(fechadura, GPIO.HIGH)
GPIO.cleanup()
