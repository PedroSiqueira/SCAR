import RPi.GPIO as GPIO
import time

class Interface:
    def __init__(self, gpiomode = GPIO.BOARD, ledVerde = 11, ledVermelho = 13, fechadura = 18):
        GPIO.setmode(gpiomode)
        GPIO.setup(ledVerde, GPIO.OUT)
        GPIO.setup(ledVermelho, GPIO.OUT)
        GPIO.setup(fechadura, GPIO.OUT)

        GPIO.output(ledVerde, GPIO.HIGH)
        GPIO.output(ledVermelho, GPIO.LOW)
        GPIO.output(fechadura, GPIO.LOW)

    def acessoAutorizado(status = 0):
        if(status == 0): # autorizado com sucesso por impressao digital
            GPIO.output(fechadura, GPIO.HIGH)
            GPIO.output(ledVerde, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(fechadura, GPIO.LOW)
            GPIO.output(ledVerde, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(ledVerde, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(ledVerde, GPIO.HIGH)
        elif(status == 1): # autorizado com sucesso por senha
            GPIO.output(fechadura, GPIO.HIGH)
            GPIO.output(ledVerde, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(fechadura, GPIO.LOW)
            GPIO.output(ledVerde, GPIO.HIGH)
            time.sleep(1)
        elif(status == 2): # autorizado, mas nao foi possivel salvar horario no banco
            GPIO.output(fechadura, GPIO.HIGH)
            GPIO.output(ledVermelho, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(fechadura, GPIO.LOW)
            GPIO.output(ledVermelho, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(ledVermelho, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(ledVermelho, GPIO.LOW)
        else: # autorizado, mas com alguma ressalva nao catalogada
            GPIO.output(fechadura, GPIO.HIGH)
            GPIO.output(ledVermelho, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(fechadura, GPIO.LOW)
            time.sleep(1)
            GPIO.output(ledVermelho, GPIO.LOW)

    def acessoDesautorizado(status = 0):
        if(status == 0): # nao encontrou a impressao digital
            GPIO.output(ledVerde, GPIO.LOW)
            GPIO.output(ledVermelho, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(ledVermelho, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(ledVermelho, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(ledVerde, GPIO.HIGH)
            GPIO.output(ledVermelho, GPIO.LOW)
        elif(status == 1): # nao encontrou a senha
            GPIO.output(ledVerde, GPIO.LOW)
            GPIO.output(ledVermelho, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(ledVermelho, GPIO.LOW)
            time.sleep(1)
        else: # outro erro nao catalogado
            GPIO.output(ledVerde, GPIO.LOW)
            GPIO.output(ledVermelho, GPIO.HIGH)
            time.sleep(1.5)
            GPIO.output(ledVerde, GPIO.HIGH)
            GPIO.output(ledVermelho, GPIO.LOW)

    def erro(e):
        GPIO.output(ledVerde, GPIO.LOW)
        GPIO.output(ledVermelho, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(ledVerde, GPIO.HIGH)
        GPIO.output(ledVermelho, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(ledVerde, GPIO.LOW)
        GPIO.output(ledVermelho, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(ledVerde, GPIO.HIGH)
        GPIO.output(ledVermelho, GPIO.LOW)
