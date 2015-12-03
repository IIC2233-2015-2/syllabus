## Pregunta 3

### **(20 pts.)** 
> Se requiere implementar un sistema de chat multiusuario para un grupo de personas en una empresa. Por restricciones en la infraestructura de la red, el servidor solo podrá mantener la comunicación entre un máximo de `N` usuarios. La principal función del servidor es la de recibir las conexiones entrantes y mantener la comunicación entre los clientes conectados. Para ello debe redireccionar los mensajes emitidos por un cliente a todo el resto de los clientes conectados indicando: el cliente que emitió el mensaje, el mensaje emitido y la hora en que se emitió en mensaje. Por ejemplo:
```python
Cliente X dijo: <mensaje>(hora).
```
Asumiendo que ya existe la aplicación cliente, implemente el servidor que sea capaz manejar la comunicación entre los clientes según las especificaciones solicitadas. Además, el servidor debe manejar la situación cuando alguno de los clientes se desconecta o termina su conexión. Haga los supuestos necesarios.

```python
class Servidor:

    def __init__(self, N):
        self.socket = socket.socket(socket.AF_INET,
                                    socket.SOCK_STREAM)
        self.socket.bind(('127.0.0.1', 3490))
        self.socket.listen(5)

        self.maxConexiones = N
        self.conectados = []
        self.conectado = True

        t = Thread(target=self.conectar)
        t.daemon = True
        t.start()

    def conectar(self):
        """
        Espera continuamente que algún cliente se conecte.
        Permite la conexión siempre y cuando la cantidad de clientes
        no supere el máximo asignado, enviando un mensaje al aceptar
        la conexión con la confirmación o rechazo.
        """
        while True:
            cliente, add = self.socket.accept()
            if len(self.conectados) < self.maxConexiones:
                print('[NUEVO CLIENTE]')
                cliente.send(b':conectar:')
                self. conectados.append(cliente)
                t = Thread(target=self.escuchar, args=(cliente,))
                t.daemon = True
                t.start()
            else:
                print('[CLIENTE RECHAZADO]')
                cliente.send(b':desconectar:')
                cliente.close()

    def escuchar(self, cliente):
        """
        Espera a que el cliente le envíe un mensaje para enviarlo
        a los demás clientes del sistema informando quién lo envió
        y la hora a la que fue enviado.
        """
        while True:
            mensaje = cliente.recv(1024)
            if mensaje != b'':
                self.enviar(
                    cliente, mensaje.decode('utf-8'), datetime.now().time())
            else:
                print('[CLIENTE DESCONECTADO]')
                self.conectados.remove(cliente)
                break

    def enviar(self, cliente, mensaje, hora):
        """
        Envía el mensaje a todos los clientes del sistema,
        excepto al que envía el mensaje, y descompone el mensaje, ya
        que en un principio viene el nombre del cliente que envía el
        mensaje.
        """
        usuario = mensaje.split('|')[0]
        mensaje = '|'.join(mensaje.split('|')[1:])
        formato = 'Cliente {user} dijo: {msg} ({time})'.format(
            user=usuario, msg=mensaje, time=hora)
        for conectado in self.conectados:
            if conectado != cliente:
                conectado.send(formato.encode('utf-8'))

    def desconectar(self):
        self.conectado = False
        self.socket.close()
```

En esta solución se asume que:
- El cliente al conectarse, si recibe un mensaje de desconexión se desconecta y se conecta si recibe el mensaje de conexión.
- El cliente envía su nombre de usuario al inicio del mensaje con un separador.


|Requerimietos|Puntajes|
|:--------------|:----------|
|Crear correctamente el socket|5|
|Recibir `N` conexiones|3|
|Recibir mensaje|4|
|Redirigir mensaje a todos los clientes|4|
|Modificar formato de mensaje|4|