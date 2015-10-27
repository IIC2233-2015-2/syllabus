# -*- encoding: utf8 -*-
import threading
from time import sleep

aLock = threading.Lock()
bLock = threading.Lock()


class Geometrica(threading.Thread):

    def __init__(self, sumando):
        super().__init__()
        self.daemon = True
        self.sumando = sumando
        self.actual = 0
        self.suma = 0

    def sumar(self):
        "Muestra la suma geométrica actual"
        self.suma += self.sumando**self.actual
        print(self.__class__.__name__.upper(),
              '[{}] ='.format(self.actual), self.suma)
        self.actual += 1

    def run(self):
        while True:
            with aLock:
                print('GEOMÉTRICA:  Ingresó al primer lock (a)')
                with bLock:  # Comente esta línea para solucionar el problema
                    print('GEOMÉTRICA:  Ingresó al segundo lock (b)')
                    sleep(0.2)
                    self.sumar()
                print('GEOMÉTRICA:  Salió del segundo lock (b)')
            print('GEOMÉTRICA:  Salió del primer lock (a)\n')


class Aritmetica(threading.Thread):

    def __init__(self, factor):
        super().__init__()
        self.daemon = True
        self.factor = factor
        self.actual = 0
        self.suma = 0

    def sumar(self):
        "Muestra suma aritmética"
        self.suma += self.factor
        print(self.__class__.__name__.upper(),
              '[{}] ='.format(self.actual), self.suma)
        self.actual += 1

    def run(self):
        while True:
            with bLock:
                print('ARITMÉTICA:  Ingresó al primer lock (b)')
                with aLock:  # Comente esta línea para solucionar el problema
                    print('ARITMÉTICA:  Ingresó al segundo lock (a)')
                    sleep(0.2)
                    self.sumar()
                print('ARITMÉTICA:  Salió del segundo lock (a)')
            print('ARITMÉTICA:  Salió del primer lock (b)\n')


S = Geometrica(0.5)
A = Aritmetica(3)

S.start()
A.start()

sleep(10)
