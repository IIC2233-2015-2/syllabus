# -*- encoding: utf8 -*-
import threading
from time import sleep


NOMBRES = ['Juanito', 'Pedrito', 'Karlita', 'Martincito']

lock = threading.Lock()


def crescendo(lista):
    nombre = threading.currentThread().name
    while len(lista) < 10:
        for indice in range(len(lista)):
            # with lock: # Para arreglar la coordinación descomente.
                print(nombre, '->', lista[indice])
        lista += [len(lista)]
        sleep(0.1)


misThreads = []
for n in range(len(NOMBRES)):
    misThreads.append(threading.Thread(
        target=crescendo,
        name=NOMBRES[n],
        kwargs={'lista': []}))
    misThreads[-1].daemon = True
    misThreads[-1].start()
sleep(2)
