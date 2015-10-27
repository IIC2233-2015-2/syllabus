# coding=utf-8

import personal as p


class Zoologico:

    def __init__(self, nombre, personal=None):
        self.nombre = nombre
        self.animales = []
        self.personal = personal if personal else []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def escuchar(self):
        for animal in self.animales:
            print('Animal #{}: {}'.format(animal.id, animal.sonido))

    def contratar_guardias(self, cantidad):
        for i in range(cantidad):
            # Accedemos a la clase Guardia a través del módulo 'personal'
            # que le pusimos el alias 'p'
            self.personal.append(p.Guardia(
                nombre='G' + str(i),
                equipamento=['Equipamento']
            ))
