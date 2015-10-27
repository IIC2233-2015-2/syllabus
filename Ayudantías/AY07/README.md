# Ayudantía 7: Threading

En ciencia de la computación un *thread* lo entenderemos como la unidad básica de procesamiento.
Los *threads* nos permiten generar **pseudoparalelismo** en nuestros programas.


### ¿PSEUDOPARALELISMO? :fearful:

Nuestro computador siempre está realizando muchísimas tareas a la vez (o eso al menos creemos), pero lo que está pasando realmente es que cada tarea es un **thread**, y estas tareas se van 'turnando' para ser ejecutados. Esto como imaginarán lo hacen muy rápido, ya que todo este tiempo pensaron que se hacia al mismo tiempo (:smirk:)


### Y... ¿Cómo lo programamos? :sweat:

En la mayoría de los lenguajes de programación, se debe crear una variable del tipo `Thread`, se le asigna una función o método a ejecutar y luego este se inicia. Así el código principal es ejecutado mientras el thread también se ejecuta *pseudoparalelamente*.


### ¿Se nombró el código principal? 

Sí!!! El `main` es un thread, todo el tiempo fue un thread :scream:.


### Y en Python... ¿Cómo se usan?

Python nos provee un módulo para trabajar y crear nuestro propios programas multiprocesos. Este módulo es `threading`, dentro de este encontraremos las herramientas para necesarias para trabajar con `Thread`.

#####Ejemplo 1:

```python

import threading

def sucesor(a):
	while True:
		print(a + 1, 'sucesor de', a)
		a += 1

miPrimerThread = threading.Thread(target=sucesor, args=(1,))
miPrimerThread.daemon = True
miPrimerThread.start()
```

Como se pudo ver la clase `Thread` (sí, es una clase :wink:) recibe como argumentos una función (`target`) y los parámetros de la función (`àrgs` como tupla o `kwargs` como diccionario). También se les puede dar un nombre (`name`) y como vimos en el ejemplo el `Thread` se inicia ejecutando el método `start()`.

### ¿Qué es lo que hace `miPrimerThread.daemon`?

En el ejemplo anterior se esperaría que se ejecutara infinitamente el método, ya que está en un ciclo `while` sin condición de término, esto **NO** sucede porque le dijimos a `miPrimerThread` que terminara cuando lo hiciera el thread principal al poner su atributo `daemon = True`. Si no se especificara, `miPrimerThread` seguiría andando aun cancelando la ejecución del thread principal.


### Multithreading

Como se dijo anteriormente podemos ejecutar *múltiples* procesos en nuestros programas.

Ejemplo 2:

```python
import threading

NOMBRES = ['Juanito', 'Pedrito', 'Karlita', 'Martincito']


def crescendo(lista):
	nombre = threading.currentThread().name
	while len(lista) < 10:
		for indice in range(len(lista)):
			print(nombre, '->', lista[indice])
		lista += [len(lista)]


misThreads = []
for n in range(len(NOMBRES)):
	misThreads.append(threading.Thread(
		target=crescendo,
		name=NOMBRES[n],
		kwargs={'lista': []}))
	misThreads[-1].daemon = True
	misThreads[-1].start()
	
input("Esperando que terminen...")
```

En este ejemplo todo debería funcionar bien, pero al ejecutarlo podemos ver que no es así :astonished:. Aunque esta herramienta acelere procesos y nos permita ejecutar programas simultaneamente y nos traiga muchos beneficios, también trae muchísimos problemas. Los principales problemas son la *coordinación* (que se ejecuten en los momentos adecuados) y las *colisiones* o *concurrencia* (cuando intentan acceder a un recurso en común) entre threads .

Como no somos los primeros en tener estos problemas, otros ya han creado mecanismos para tener un mayor control sobre los threads :smile:.

### Lock

Este es uno de los mecanismos más frecuentes que nos ayudan a solucionar esta clase de problemas.

Ejemplo 2 (mejorado):
```python
import threading
import time


NOMBRES = ['Juanito', 'Pedrito', 'Karlita', 'Martincito']

lock = threading.Lock()


def crescendo(lista):
    nombre = threading.currentThread().name
    while len(lista) < 10:
        for indice in range(len(lista)):
            lock.acquire()
            print(nombre, '->', lista[indice])
            lock.release()
        lista += [len(lista)]
        time.sleep(0.1)


misThreads = []
for n in range(len(NOMBRES)):
    misThreads.append(threading.Thread(
        target=crescendo,
        name=NOMBRES[n],
        kwargs={'lista': []}))
    misThreads[-1].daemon = True
    misThreads[-1].start()
    
input("Esperando que terminen...")
```


Ejemplo 2 (mejorado y con otra sintaxis):
```python
import threading
import time


NOMBRES = ['Juanito', 'Pedrito', 'Karlita', 'Martincito']

lock = threading.Lock()


def crescendo(lista):
    nombre = threading.currentThread().name
    while len(lista) < 10:
        for indice in range(len(lista)):
        	with lock:
            	print(nombre, '->', lista[indice])
        lista += [len(lista)]
        time.sleep(0.1)


misThreads = []
for n in range(len(NOMBRES)):
    misThreads.append(threading.Thread(
        target=crescendo,
        name=NOMBRES[n],
        kwargs={'lista': []}))
    misThreads[-1].daemon = True
    misThreads[-1].start()
    
input("Esperando que terminen...")
```

### Más problemas :disappointed:

Con los locks también debemos tener precaución!! Si no podemos quedar en un **deadlock**, cuando bloqueamos un trozo de código y el programa no puede continuar, porque no se desbloquea lo que bloqueamos.

Ejemplo 3:

```python
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
                print('GEOMÉTRICA:	Ingresó al primer lock (a)')
                with bLock:
                    print('GEOMÉTRICA:	Ingresó al segundo lock (b)')
                    sleep(0.2)
                    self.sumar()
                print('GEOMÉTRICA:	Salió del segundo lock (b)')
            print('GEOMÉTRICA:	Salió del primer lock (a)\n')


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
                print('ARITMÉTICA:	Ingresó al primer lock (b)')
                with aLock:
                    print('ARITMÉTICA:	Ingresó al segundo lock (a)')
                    sleep(0.2)
                    self.sumar()
                print('ARITMÉTICA:	Salió del segundo lock (a)')
            print('ARITMÉTICA:	Salió del primer lock (b)\n')


S = Geometrica(0.5)
A = Aritmetica(3)

S.start()
A.start()

sleep(10)

```

## Ejercicio

Cree una clase `Monitor` que reciba una instancia de la clase `Auto` y la velocidad máxima permitida. El `Monitor` debe estar al tanto de de la velocidad de la clase `Auto`, tendrá que avisar cuando esté llegando al 90% de la velocidad máxima, cuando se exceda le cambie la aceleración (`cambiarAceleracion()`) y si baja a menos del 50% de la velocidad máxima que cambie nuevamente la acelaración.

```python
class Auto:

    def __init__(self, aceleracion):
        self.velocidad = 0
        self.aceleracion = aceleracion
        self.avanzando = True

    def andar(self):
        while self.avanzando:
            self.velocidad += self.aceleracion
            sleep(0.1)

    def cambiarAceleracion(self):
        self.aceleracion *= -1

    def detener(self):
        self.avanzando = False
```
