from MetaClases import *
from random import *

__author__ = 'bamavrakis'
programadores = ['Belen', 'Patricio', 'Jaime', 'Marco', 'Bastian',
                 'Antonio1', 'Ivania', 'Felipe', 'Matias', 'Carlos',
                 'Ariel', 'Francisco', 'Francisca', 'Iacopo', 'Enrique',
                 'Patricio', 'Vicente', 'Rodolfo', 'Eduardo', 'Diego',
                 'Guillermo', 'Fernando', 'Juan1', 'Juan2', 'Nicolás',
                 'Antonio2']


class Robot(metaclass=MetaRobot):

    def __init__(self, creadores, inicial):
        self.creadores = creadores
        self.actual = inicial

    def Verificar(self):
        if self.actual.hacker:
            return True
        return False


class Puerto():

    def __init__(self, ide, hacker):
        self.hacker = hacker
        self.ide = ide

    """
    El atributo hacker es un número entero que se comporta como bool
    (si, en python bool es subclase de int)
    """

if __name__ == '__main__':
    puertos = {}
    for i in range(10):
        puertos[i] = Puerto(i, randint(0, 1))
    robocop6 = Robot(programadores, puertos[0])
    robocop6.check_creator()
    robocop6.cambiar_nodo(puertos[randint(0, 9)])
    robocop6.cortar_conexion()
