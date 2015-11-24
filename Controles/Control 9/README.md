# Control 9

### Forma 1
**1)Explique cuáles son las principales diferencias entre un cliente y un servidor desde el punto de vista de codigo en python**

Respuesta: Las principales diferencias entre un cliente y un servidor, son primero que un cliente puede conectarse a mas de
un servidor, pero no puede aceptar conexiones de otros clientes bajo la aquitectura cliente-servidor. Por otro lado
el servidor puede tener conexiones con mas de un cliente, y debe estar siempre atento a potenciales conexiones.
Desde el punto de vista de los métodos, el servidor tiene el método ``listen()`` que no lo tiene el cliente ya que es el
quien puede recibir mas de una conexion. También el servidor tiene el método ``bind()`` que no lo tiene el cliente ya que 
el sistema operativo hace el enlace automáticamente en el método ``connect()``

**2) Describa que función cumple el método `listen()` de un socket.**

Respuesta: el método ``listen()`` le dice al sistema que escuche potenciales conexiones, el parámetro que recibe es la 
cantidad de conexiones permitidas.

###### Basado en el material de [**Networking**](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/12-NETWORKING/12-Networking.html)

- Pregunta 1: 1 punto por cada diferencia entre el cliente y el servidor. 
-  Pregunta 2: 3 pts por correcta explicación del método.

### Forma 2
**1) Usted necesita implementar la transmisión de datos de un sistema de streaming de video, qué tipo de conexión usaría para
este requerimiento**.

Respuesta: se debe utilizar un protocolo de transmisión de datos del tipo ``UDP`` ya que permite el envío de datos sin 
la necesidad de establecer una conexión. Los paquetes de datos enviados a través del protocolo UDP 
contienen un encabezado suficiente para ser identificados y direccionados correctamente a través de la red.

**2) Describa qué función realiza el método `bind()` de un socket y comente porque en el cliente no se usa.**

Respuesta: el metodo ``bind()`` enlaza el socket a un puerto, los parámetros que recibe son el host y el puerto, en el cliente
no es necesario implementarlo en el cliente ya que el sistema operativo lo hace automáticamente a traves del método ``connect()``

###### Basado en el material de [**Networking**](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/12-NETWORKING/12-Networking.html)




-  Pregunta 1: 1,5 pts. por elegir el protocolo correctamente y 1,5 pts. por la justificación de su elección.
-  Pregunta 2: 1,5 pts. por explicar en que consiste el método y 1,5 pts. por explicar porque en el cliente no se usa.


### Forma 3
**1) Usted necesita implementar la conexión para una plataforma de correos electrónicos ¿Qué protocolo de comunicación utilizaría?
Justifique su respuesta.**

Respuesta: Se debe utilizar un protocolo de transmisión de datos ``TCP`` ya que este protocolo asegura que la información llegue 
intacta, es decir garantiza que no haya pérdida de esta. Para este tipo de protocolo se necesita que haya una conexión entre
quien envía y quien recibe la información, de forma que si falla el envío de un paquete, el receptor solicite nuevamente el 
envío de este.

**2) Describa que función cumple el método `accept()` de un socket.**

Respuesta: El método ``accept()`` es el que establece una conexión entre un cliente y un servidor.

###### Basado en el material de [**Networking**](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/12-NETWORKING/12-Networking.html)


-  Pregunta 1: 1,5 pts. por elegir el protocolo correctamente y 1,5 pts. por justificación de su elección.
-  Pregunta 2: 3 pts. por explicar correctamente que función cumple el método ``accept()``

