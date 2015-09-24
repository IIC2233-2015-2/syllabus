#!/usr/bin/env python3
# coding=utf-8

from animales.reptiles import Serpiente  # Formar correcta de importar.
from animales.mamiferos import *         # Formar no recomendada.
from zoologico import Zoologico


if __name__ == '__main__':
    zoo = Zoologico('Mi zoologico')
    # Agreguemos una instancia de Serpiente
    zoo.agregar_animal(Serpiente(nombre='S1', fecha_nacimiento='12/12/2014'))

    # Agreguemos una instancia de Leon, que la importamos de 'mamiferos'
    # El problema de usar '*' es que pierdes control de lo que importas.
    zoo.agregar_animal(Leon(nombre='S1', fecha_nacimiento='12/12/2014'))

    zoo.escuchar()
    zoo.contratar_guardias(4)
    for p in zoo.personal:
        print(p.nombre)
