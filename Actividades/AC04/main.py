# coding=utf-8


# Completen los métodos
# Les estamos dando un empujoncito con la lectura del input
# Al usar la clausula: "with open('sonda.txt', 'r') as f", el archivo se cierra automáticamente al salir de la función.


def sonda():
    with open('sonda.txt', 'r') as f:
        for line in f:
            pass


def traidores():
    with open('bufalos.txt', 'r') as f:
        for line in f:
            pass

    with open('rivales.txt', 'r') as f:
        for line in f:
            pass


def pizzas():
    with open('pizza.txt', 'r') as f:
        for line in f.read().splitlines():
            pass


if __name__ == '__main__':
    exit_loop = False

    functions = {"1": sonda, "2": traidores, "3": pizzas}

    while not exit_loop:
        print(""" Elegir problema:
            1. Sonda
            2. Traidores
            3. Pizzas
            Cualquier otra cosa para salir
            Respuesta: """)

        user_entry = input()

        if user_entry in functions:
            functions[user_entry]()
        else:
            exit_loop = True
