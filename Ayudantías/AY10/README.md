# Ayudantía 10: Serialización y Networking

## ¿Serializar? ¿Para qué?

- La serialización nos permite hacer perdurar en el tiempo un objeto a través de su codificación en bytes (almacenamiento) o cuando tenemos conexiones y deseamos enviar datos (transferencia de datos). Es importante mencionar que este objeto que está guardado en un archivo es solo un CLON del original.

- Hacer esto es mucho más fácil que escribir todos sus atributos en un archivo de texto.


### Pickle

- Esta librería posee un potente algoritmo para la serialización y  des-seralización de objetos en Python.

```python
import pickle


class Vehiculo:
	
	def __init__(self, patente, marca, capacidad, ruedas):
		self.patente = patente
		self.marca = marca
		self.capacidad = capacidad
		self.ruedas = ruedas

v = Vehiculo('BB-NN-47', 'FasterFaster', 5, 3)
print(id(v))
k = pickle.dumps(v)

print(id(pickle.loads(k)))

# Resultado
## >> 140638974860200
## >> 140639002089680

```

- Tambien podemos guardar la serialización dentro de un archivo.

```python

with open('autito.VEHICULO', 'wb') as archivo:
    pickle.dump(v, archivo)

with open('autito.VEHICULO', 'rb') as archivo:
    vClon = pickle.load(archivo)

print(vClon.__dict__)

```


### JSON

- Este módulo hace una serialización "leible" para seres humanos.

```python
import json


class Vehiculo:

    def __init__(self, patente, marca, capacidad, ruedas):
        self.patente = patente
        self.marca = marca
        self.capacidad = capacidad
        self.ruedas = ruedas

    @classmethod
    def by_json(cls, atributos):
        return cls(**atributos)


v = Vehiculo('BB-NN-47', 'FasterFaster', 5, 3)
print(v.__dict__)

vSerializado = json.dumps(v.__dict__)

vDeserializado = json.loads(vSerializado)

vClon = Vehiculo.by_json(vDeserializado)

print(vClon)

print(vClon.__dict__)


```

## Networking

En el desarrollo de sofwares es cada vez más necesaria la comunicación entre programas o entre computadores. Para estos fines utilizamos la **Internet**, pero para poder usar este medio es necesario entender 3 conceptos:

- Dirección IP
- Puertos
- Protocolos

### Dirección IP

- Es una etiqueta para identificar a un dispositivo dentro de una red. 
- Esta dirección es dinámica, pero se puede hacer fija pagando.
- Existe una IP local, que nos identifica dentro de una red.
- Otra IP pública, que identifica nuestro equipo en internet (No la conocemos directamente)

Ver [link](http://cual-es-mi-ip-publica.com/)

### Puertos

- Son los puntos de comunicación dentro de una IP.
- Si conocemos una IP y nos queremos comunicar con ella debemos saber a qué puerto hablarle.
- Un problema común es intentar utilizar un puerto que ya está siendo utilizado. Para esto solo hay que cambiar el puerto.

### Protocolos

Definen cómo debe realizarse el intercambio de datos entre dos puntos de la red. 

Se tienen:
- UDP: Este protocolo no está orientado a la conexión. Uno de los extremos envía información sin confirmar el recibo de estos.
- TCP: Este a diferencia de UDP, verifica la llegada de los datos. En caso de algún error se solicitan nuevamente los datos.

## ¿Cómo se utiliza todo esto en Python?

**SOCKETS**: Dirección IP + Puerto

A través de los sockets se envían bytes. Esto significa que podemos enviar objetos serializados, ya sea `json` o `pickle`.

### Métodos

```python
import socket

socketTCP = socket.socket(socket.AF_INET,
						  socket.SOCK_STREAM)

socketUDP = socket.socket(socket.AF_INET,
						  socket.SOCK_DGRAM)

# métodos cliente
socketCliente.connect(address)

# métodos servidor
socketServidor.bind(address)
socketServidor.listen(backlog)
socketServidor.accept()

# métodos generales

socketCualquiera.send(bytes)
socketCualquiera.recv(1024)
socketCualquiera.sendto(bytes, address)
socketCualquiera.close()
socketCualquiera.gethostname()
```



