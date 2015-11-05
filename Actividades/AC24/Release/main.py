import socket
import threading
from gato import Gato, sys


class Service:
    def __init__(self):
        pass

    def escuchar(self):
        pass

    def enviar(self, mensaje):
        pass


class Cliente(Service):
    def __init__(self, gato):
        pass


class Servidor(Service):
    def __init__(self, gato):
        pass

    def aceptar(self):
        pass


if __name__ == "__main__":

    pick = input("Ingrese X si quiere ser servidor o O si desea ser cliente: ")
    if pick == "X":
        server = Servidor()
        server.aceptar()
        while True:
            mensaje = input("Jugador {0} debe ingresar la posicion en que desea jugar".format(server.gato.turno))
            server.enviar(mensaje)

    elif pick == "O":
        client = Cliente()
        escuchador = threading.Thread(target=client.escuchar)
        escuchador.daemon = True
        escuchador.start()
        while True:
            mensajes = input("Jugador {0} debe ingresar la posicion en que desea jugar".format(client.gato.turno))
            client.enviar(mensajes)
