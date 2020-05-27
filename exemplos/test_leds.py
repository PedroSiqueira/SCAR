import RPi.GPIO as GPIO

def desligar():
    GPIO.output(ledAzul, GPIO.LOW)
    GPIO.output(ledVermelho, GPIO.LOW)
    GPIO.output(ledVerde, GPIO.LOW)
    GPIO.output(fechadura, GPIO.LOW)

ledVermelho = 33
ledVerde = 35
ledAzul = 37
fechadura = 31

GPIO.setmode(GPIO.BOARD)

GPIO.setup(ledVermelho, GPIO.OUT)
GPIO.setup(ledVerde, GPIO.OUT)
GPIO.setup(ledAzul, GPIO.OUT)
GPIO.setup(fechadura, GPIO.OUT)

while(True):
    r = input("R, G or B? (anything else to exit)")
    desligar()
    if(r.lower()=="r"):
        GPIO.output(ledVermelho, GPIO.HIGH)
    elif(r.lower()=="g"):
        GPIO.output(ledVerde, GPIO.HIGH)
    elif(r.lower()=="b"):
        GPIO.output(ledAzul, GPIO.HIGH)
    else:
        break;

desligar()
GPIO.cleanup()
