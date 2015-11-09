import socket
import threading
import sys

__author__ = 'Vicente' # Modificado por Ivania :)


class Cliente:

    def __init__(self, usuario):
        self.usuario = usuario
        self.host = '127.0.0.1'
        self.port = 3490
        self.s_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # Un cliente se puede conectar solo a un servidor.
            self.s_cliente.connect((self.host, self.port)) # El cliente revisa que el servidor esté disponible
            # Una vez que se establece la conexión, se pueden recibir mensajes
            recibidor = threading.Thread(target=self.recibir_mensajes, args=())
            recibidor.daemon = True
            recibidor.start()
        except socket.error:
            print("No fue posible realizar la conexión")
            sys.exit()

    def recibir_mensajes(self):
        while True:
            data = self.s_cliente.recv(1024)
            print(data.decode('utf-8'))

    def enviar(self, mensaje):
        msj_final = self.usuario + ": " + mensaje
        self.s_cliente.send(msj_final.encode('utf-8'))


class Servidor:

    def __init__(self, usuario):
        self.usuario = usuario
        self.host = '127.0.0.1'
        self.port = 3490
        self.s_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Debemos hacer el setup para poder escuchar a los clientes que se quieran conectar
        self.s_servidor.bind((self.host, self.port))
        # En este caso solo queremos escuchar un cliente
        self.s_servidor.listen(1)
        self.cliente = None
        self.aceptar()

    def recibir_mensajes(self):
        while True:
            data = self.cliente.recv(1024)
            mensaje = data.decode('utf-8')
            print(mensaje)

    def aceptar(self):
        cliente_nuevo, address = self.s_servidor.accept()
        self.cliente = cliente_nuevo
        thread_cliente = threading.Thread(target=self.recibir_mensajes, args=())
        thread_cliente.daemon = True
        thread_cliente.start()

    def enviar(self, mensaje):
        msj_final = self.usuario + ": " + mensaje
        self.cliente.send(msj_final.encode('utf-8'))


if __name__ == "__main__":

    pick = input("Ingrese S si quiere ser servidor o C si desea ser cliente: ")
    if pick == "S":
        nombre = input("Ingrese el nombre del usuario: ")
        server = Servidor(nombre)
        while True:
            texto = input()
            server.enviar(texto)

    elif pick == "C":
        nombre = input("Ingrese el nombre del usuario: ")
        client = Cliente(nombre)
        while True:
            texto = input()
            client.enviar(texto)