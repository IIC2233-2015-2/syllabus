import socket
import threading
import sys


class Cliente:

    def __init__(self, usuario):
        self.usuario = usuario
        self.host = '127.0.0.1'
        self.port = 3491
        self.s_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection = True
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
        while self.connection:
            data = self.s_cliente.recv(1024)
            mensaje = data.decode('utf-8')
            if mensaje.split(': ')[1] == 'quit':
                self.desconectar()
                print('El servidor se ha desconectado')
                print(self.connection)
            print(mensaje)

    def enviar(self, mensaje):
        msj_final = self.usuario + ": " + mensaje
        self.s_cliente.send(msj_final.encode('utf-8'))

    def desconectar(self):
        self.connection = False
        self.s_cliente.close()


class Servidor:

    def __init__(self, usuario, num_clients=1):
        self.usuario = usuario
        self.host = '127.0.0.1'
        self.port = 3491
        self.s_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Debemos hacer el setup para poder escuchar a los clientes que se quieran conectar
        self.s_servidor.bind((self.host, self.port))
        # En este caso solo queremos escuchar un cliente
        self.s_servidor.listen(num_clients)
        self.clientes = []
        self.connection = True

        # No hacemos self.aceptar()

        thread_aceptar = threading.Thread(target=self.aceptar, args=())
        thread_aceptar.daemon = True
        thread_aceptar.start()

    def recibir_mensajes(self, cliente):
        while self.connection:
            data = cliente.recv(1024)
            mensaje = data.decode('utf-8')
            if mensaje.split(': ')[1] == 'quit':
                self.clientes.remove(cliente)
            print(mensaje)

    def aceptar(self):
        while True:
            cliente_nuevo, address = self.s_servidor.accept()
            self.clientes.append(cliente_nuevo)
            thread_mensajes = threading.Thread(target=self.recibir_mensajes, args=(cliente_nuevo,))
            thread_mensajes.daemon = True
            thread_mensajes.start()

    def enviar(self, mensaje):
        c, mensaje = mensaje.split(',')
        msj_final = self.usuario + ": " + mensaje
        self.clientes[int(c)].send(msj_final.encode('utf-8'))

    def desconectar(self):
        for i in range(len(self.clientes)):
            self.enviar(str(i) + ',quit')
        self.connection = False
        self.s_servidor.close()



if __name__ == "__main__":

    pick = input("Ingrese S si quiere ser servidor o C si desea ser cliente: ")
    if pick == "S":
        nombre = input("Ingrese el nombre del usuario: ")
        server = Servidor(nombre, num_clients=2)
        while server.connection:
            texto = input()
            if texto == 'quit':
                server.desconectar()
            else:
                server.enviar(texto)
    else:
        nombre = input("Ingrese el nombre del usuario: ")
        client = Cliente(nombre)
        while client.connection:
            texto = input()
            if texto == 'quit':
                client.enviar('quit')
                client.desconectar()
            else:
                client.enviar(texto)


