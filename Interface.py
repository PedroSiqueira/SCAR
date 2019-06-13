import RPi.GPIO as GPIO
import time

class Interface:
    def __del__(self):
        GPIO.cleanup()

    def __init__(self, gpiomode = GPIO.BOARD, ledVerde = 11, ledVermelho = 13, fechadura = 12):

        self.ledVerde = ledVerde
        self.ledVermelho = ledVermelho
        self.fechadura = fechadura

        GPIO.setmode(gpiomode)
        GPIO.setup(self.ledVerde, GPIO.OUT)
        GPIO.setup(self.ledVermelho, GPIO.OUT)
        GPIO.setup(self.fechadura, GPIO.OUT)

        GPIO.output(self.ledVerde, GPIO.HIGH)
        GPIO.output(self.ledVermelho, GPIO.LOW)
        GPIO.output(self.fechadura, GPIO.LOW)

    def acessoAutorizado(self, status = 0):
        if(status == 0): # autorizado com sucesso por impressao digital
            GPIO.output(self.fechadura, GPIO.HIGH)
            GPIO.output(self.ledVerde, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(self.fechadura, GPIO.LOW)
            GPIO.output(self.ledVerde, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(self.ledVerde, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(self.ledVerde, GPIO.HIGH)
        elif(status == 1): # autorizado com sucesso por senha
            GPIO.output(self.fechadura, GPIO.HIGH)
            GPIO.output(self.ledVerde, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(self.fechadura, GPIO.LOW)
            GPIO.output(self.ledVerde, GPIO.HIGH)
            time.sleep(1)
        elif(status == 2): # autorizado, mas nao foi possivel salvar horario no banco
            GPIO.output(self.fechadura, GPIO.HIGH)
            GPIO.output(self.ledVermelho, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(self.fechadura, GPIO.LOW)
            GPIO.output(self.ledVermelho, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(self.ledVermelho, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(self.ledVermelho, GPIO.LOW)
        else: # autorizado, mas com alguma ressalva nao catalogada
            GPIO.output(self.fechadura, GPIO.HIGH)
            GPIO.output(self.ledVermelho, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(self.fechadura, GPIO.LOW)
            time.sleep(1)
            GPIO.output(self.ledVermelho, GPIO.LOW)

    def acessoDesautorizado(self, status = 0):
        if(status == 0): # nao encontrou a impressao digital
            GPIO.output(self.ledVerde, GPIO.LOW)
            GPIO.output(self.ledVermelho, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(self.ledVermelho, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(self.ledVermelho, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(self.ledVerde, GPIO.HIGH)
            GPIO.output(self.ledVermelho, GPIO.LOW)
        elif(status == 1): # nao encontrou a senha
            GPIO.output(self.ledVerde, GPIO.LOW)
            GPIO.output(self.ledVermelho, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(self.ledVermelho, GPIO.LOW)
            time.sleep(1)
        else: # outro erro nao catalogado
            GPIO.output(self.ledVerde, GPIO.LOW)
            GPIO.output(self.ledVermelho, GPIO.HIGH)
            time.sleep(1.5)
            GPIO.output(self.ledVerde, GPIO.HIGH)
            GPIO.output(self.ledVermelho, GPIO.LOW)

    def erro(self, e):
        GPIO.output(self.ledVerde, GPIO.LOW)
        GPIO.output(self.ledVermelho, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(self.ledVerde, GPIO.HIGH)
        GPIO.output(self.ledVermelho, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(self.ledVerde, GPIO.LOW)
        GPIO.output(self.ledVermelho, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(self.ledVerde, GPIO.HIGH)
        GPIO.output(self.ledVermelho, GPIO.LOW)
