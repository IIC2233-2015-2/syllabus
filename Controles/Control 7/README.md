# Control 7

### Pregunta 1
**Explique mediante qué mecanismo una GUI conoce las acciones del usuario**

El mecanismo utilizado se basa en el manejo de eventos. El usuario realiza una acción activando uno de los elementos de la GUI, esto se comunica en el programa como un evento que activa la realización de una acción en este.

### Pregunta 2
**Explique en palabras cómo se genera una señal personalizada**

*1.* Crear la nueva señal como una instancia del objeto `QtCore.pyqtSignal()`, ya sea en la creación de la GUI como variable: `self.señal = QtCore.pyqtSignal()`, o dentro de algún objeto que contenga todas las señales personalizadas (aparece en la materia)

*2.* Conectar mediante el método `connect()` la señal creada con el slot que se ejecutará cuando la señal sea activada: `self.señal.connect(<alguna funcion>)`

*3.* Utilizar el método `emit()` de la señal (propio de la clase `pyqtSignal()`) para activar la señal cuando se requiera: `self.señal.emit()`

### Pregunta 3
**¿Bajo qué modelo un objeto QPushButton interactúa con el resto de los elementos cuando es presionado**

En PyQt4 la interacción entre los distintos widgets ocurre mediante un modelo o mecanismo de control eventos señal y puerto (signal y slot). Cuando un evento ocurre, el objeto que es activado genera una señal. Un puerto o slot es una función que es llamada por alguna de las señales. 

En el caso del `QPushButton`, después de que es presionado se genera el evento `clicked` que enviará la señal a la función definida como slot. Mediante el metodo `connect()` se establece la comunicación entre la señal y el slot.
