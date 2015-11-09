# Ayudantía 10

import socket

socketTCP = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

user = input('Cliente (c) o Servidor (s):\t')

if user == 's':
    socketTCP.bind(('127.0.0.1', 3490))
    socketTCP.listen(1)
    cliente, add = socketTCP.accept()
    print(add)
    mensajeEnBytes = cliente.recv(1024)
    print(mensajeEnBytes.decode('ascii'))
    cliente.send(b'hola soy tu servidor')

elif user == 'c':
    socketTCP.connect(('127.0.0.1', 3490))
    socketTCP.send(b'hola hay alguien ahi')
    mensajeEnBytes = socketTCP.recv(1024)
    print(mensajeEnBytes.decode('ascii'))

socketTCP.close()