# coding=utf-8

# Ligeramente modificado del enunciado original

import threading
from time import sleep


class Auto:

    def __init__(self, aceleracion, intervalo=0.1):
        self.velocidad = 0
        self.aceleracion = aceleracion
        self.intervalo = intervalo
        self.avanzando = True

    def andar(self):
        while self.avanzando:
            self.velocidad += self.aceleracion
            sleep(0.1)

    def cambiar_aceleracion(self):
        self.aceleracion *= -1

    def detener(self):
        self.velocidad = 0
        self.avanzando = False


class Monitor(threading.Thread):

    def __init__(self, auto, velocidad_maxima, intervalo=0.1):
        super().__init__(target=Monitor.monitorear,
                         args=(self, velocidad_maxima, intervalo))
        self.auto = auto
        self.daemon = True

    def monitorear(self, velocidad_maxima, intervalo):
        run = threading.Thread(target=Auto.andar, args=(self.auto,))
        run.daemon = True
        run.start()

        while self.auto.avanzando:
            print('Vas a {}'.format(self.auto.velocidad))
            sleep(intervalo)

            if self.auto.velocidad > 1.2 * velocidad_maxima:
                print('Demasiado rápido! Cancelando test...')
                self.auto.detener()

            elif self.auto.velocidad > velocidad_maxima:
                print('Te pasaste del límite de velocidad.')
                self.auto.cambiar_aceleracion()

            elif self.auto.velocidad >= 0.9 * velocidad_maxima:
                print('Estás llegando al límite de velocidad')

            elif self.auto.velocidad < 0.5 * velocidad_maxima \
                    and self.auto.aceleracion < 0:
                print('Vas muy lento!')
                self.auto.cambiar_aceleracion()


if __name__ == '__main__':
    # Nuestro auto
    auto = Auto(aceleracion=15, intervalo=0.1)

    # Prueba cambiando el intervalo de control de velocidad del auto
    intervalo = 0.05  # 0.2 | 0.01 | 0.3

    monitor = Monitor(auto, velocidad_maxima=180, intervalo=intervalo)

    monitor.start()
    monitor.join()
