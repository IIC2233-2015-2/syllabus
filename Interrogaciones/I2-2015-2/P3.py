import socket
from datetime import datetime
from threading import Thread

__author__ = 'figarrido'


class Cliente:

    def __init__(self, nombre):
        self.nombre = nombre
        self.socket = socket.socket(socket.AF_INET,
                                    socket.SOCK_STREAM)
        try:
            self.socket.connect(('127.0.0.1', 3490))
            conexion = self.socket.recv(1024)
            if conexion.decode('ascii') == ':conectar:':
                t = Thread(target=self.escuchar)
                self.conectado = True
                t.daemon = True
                t.start()
            elif conexion.decode('ascii') == ':desconectar:':
                self.conectado = False
                self.socket.close()
                print('El servidor está saturado')
        except:
            print('Ocurrió un error')

    def escuchar(self):
        while True:
            mensaje = self.socket.recv(1024)
            if mensaje == b'':
                self.socket.close()
                self.conectado = False
                print('[EL SERVIDOR SE HA DESCONECTADO]')
                break
            print(mensaje.decode('utf-8'))

    def enviar(self, mensaje):
        mensaje = self.nombre + '|' + mensaje
        self.socket.send(mensaje.encode('utf-8'))


class Servidor:

    def __init__(self, N):
        self.socket = socket.socket(socket.AF_INET,
                                    socket.SOCK_STREAM)
        self.socket.bind(('127.0.0.1', 3490))
        self.socket.listen(5)

        self.maxConexiones = N
        self.conectados = []
        self.conectado = True

        print("Para cerrar la conexión, use el comando `quit`")

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
                self.conectados.append(cliente)
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
            try:
                mensaje = cliente.recv(1024)
                self.enviar(
                    cliente, mensaje.decode('utf-8'), datetime.now().time())
            except:
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


user = input('Servidor (s) o Cliente (c): ')

if user == 's':
    s = Servidor(3)
    while s.conectado:
        msg = input()
        if msg == 'quit':
            s.desconectar()
elif user == 'c':
    nombre = input('Nombre de usuario:  ')
    c = Cliente(nombre)
    while c.conectado:
        msg = input()
        c.enviar(msg)
