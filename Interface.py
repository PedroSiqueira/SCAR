import RPi.GPIO as GPIO
import time

"""
esta classe acessa os leds e a trava elétrica
"""
class Interface:
    def __init__(self, boardOrBcm = True, ledVermelho = 33, ledVerde = 35,  ledAzul = 37, fechadura = 31):
        self.ledVermelho = ledVermelho
        self.ledVerde = ledVerde
        self.ledAzul = ledAzul
        self.fechadura = fechadura

        if(boardOrBcm==True):
            GPIO.setmode(GPIO.BOARD)
        else:
            GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.ledVermelho, GPIO.OUT)
        GPIO.setup(self.ledVerde, GPIO.OUT)
        GPIO.setup(self.ledAzul, GPIO.OUT)
        GPIO.setup(self.fechadura, GPIO.OUT)

        GPIO.output(self.ledAzul, GPIO.HIGH)
        GPIO.output(self.ledVermelho, GPIO.LOW)
        GPIO.output(self.ledVerde, GPIO.LOW)
        GPIO.output(self.fechadura, GPIO.HIGH) # o relay eh desligado no sinal HIGH

    def acessoAutorizado(self, status = 0):
        if(status == 0): # autorizado com sucesso por impressao digital
            GPIO.output(self.fechadura, GPIO.LOW)
            GPIO.output(self.ledVerde, GPIO.HIGH)
            GPIO.output(self.ledAzul, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(self.fechadura, GPIO.HIGH)
            GPIO.output(self.ledVerde, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(self.ledVerde, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(self.ledVerde, GPIO.LOW)
            GPIO.output(self.ledAzul, GPIO.HIGH)
        elif(status == 1): # autorizado com sucesso por senha
            GPIO.output(self.fechadura, GPIO.LOW)
            GPIO.output(self.ledVerde, GPIO.HIGH)
            GPIO.output(self.ledAzul, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(self.fechadura, GPIO.HIGH)
            time.sleep(0.5)
            time.sleep(0.5)
            GPIO.output(self.ledVerde, GPIO.LOW)
            GPIO.output(self.ledAzul, GPIO.HIGH)

        elif(status == 2): # autorizado, mas nao foi possivel salvar horario no banco
            GPIO.output(self.fechadura, GPIO.LOW)
            GPIO.output(self.ledVerde, GPIO.HIGH)
            GPIO.output(self.ledAzul, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(self.fechadura, GPIO.HIGH)
            GPIO.output(self.ledVermelho, GPIO.HIGH)
            GPIO.output(self.ledVerde, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(self.ledVerde, GPIO.HIGH)
            GPIO.output(self.ledVermelho, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(self.ledVerde, GPIO.LOW)
            GPIO.output(self.ledAzul, GPIO.HIGH)

        else: # autorizado, mas com alguma ressalva nao catalogada
            GPIO.output(self.fechadura, GPIO.LOW)
            GPIO.output(self.ledVerde, GPIO.HIGH)
            GPIO.output(self.ledAzul, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(self.fechadura, GPIO.HIGH)
            GPIO.output(self.ledVerde, GPIO.LOW)
            GPIO.output(self.ledAzul, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(self.ledVerde, GPIO.HIGH)
            GPIO.output(self.ledAzul, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(self.ledVerde, GPIO.LOW)
            GPIO.output(self.ledAzul, GPIO.HIGH)

    def acessoDesautorizado(self, status = 0):
        if(status == 0): # nao encontrou a impressao digital
            GPIO.output(self.ledVermelho, GPIO.HIGH)
            GPIO.output(self.ledAzul, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(self.ledVermelho, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(self.ledVermelho, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(self.ledVermelho, GPIO.LOW)
            GPIO.output(self.ledAzul, GPIO.HIGH)
        elif(status == 1): # nao encontrou a senha
            GPIO.output(self.ledVermelho, GPIO.HIGH)
            GPIO.output(self.ledAzul, GPIO.LOW)
            time.sleep(0.5)
            time.sleep(0.5)
            time.sleep(0.5)
            GPIO.output(self.ledVermelho, GPIO.LOW)
            GPIO.output(self.ledAzul, GPIO.HIGH)
        else: # outro erro nao catalogado
            GPIO.output(self.ledVermelho, GPIO.HIGH)
            GPIO.output(self.ledAzul, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(self.ledVermelho, GPIO.LOW)
            GPIO.output(self.ledAzul, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(self.ledVermelho, GPIO.HIGH)
            GPIO.output(self.ledAzul, GPIO.LOW)
            time.sleep(0.5)
            GPIO.output(self.ledVermelho, GPIO.LOW)
            GPIO.output(self.ledAzul, GPIO.HIGH)

    def erro(self):
        for i in range(2):
            GPIO.output(self.ledAzul, GPIO.LOW)
            GPIO.output(self.ledVermelho, GPIO.HIGH)
            GPIO.output(self.ledVerde, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(self.ledVermelho, GPIO.LOW)
            GPIO.output(self.ledVerde, GPIO.LOW)
            time.sleep(0.5)
        GPIO.output(self.ledAzul, GPIO.HIGH)

    def blinkOnce(self, ledId=None):
        if(ledId is None): ledId = self.ledAzul
        if(GPIO.input(ledId)==True):
            on=GPIO.LOW
            off=GPIO.HIGH
        else:
            on=GPIO.HIGH
            off=GPIO.LOW

        GPIO.output(ledId,on)
        time.sleep(0.5)
        GPIO.output(ledId,off)

if __name__== "__main__":
    i = Interface()
    while(True):
        r=input("digite 'a' para autorizado, 'd' para desautorizado, 'b' para piscar ou outra coisa para sair")
        if(r=='a'):
            r=int(input("digite um numero"))
            i.acessoAutorizado(r)
        elif(r=='d'):
            r=int(input("digite um numero"))
            i.acessoDesautorizado(r)
        elif(r=='b'):
            r=input("'r' para vermelho, 'g' para verde ou outro valor para azul")
            if(r=='r'): i.blinkOnce(i.ledVermelho)
            elif(r=='g'): i.blinkOnce(i.ledVerde)
            else: i.blinkOnce(i.ledAzul)
        else:
            i.erro()
            break
    GPIO.cleanup();
