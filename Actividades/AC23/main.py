#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os


class Persona:
    pass


def existe_persona(_id):
    pass


def get_persona(_id):
    pass


def write_persona(persona):
    pass


def crear_persona(_id, nombre_completo):
    pass


def agregar_amigo(id_1, id_2):
    pass


def set_persona_favorita(_id, id_favorito):
    pass


def get_persona_mas_favorita():
    pass

# ----------------------------------------------------- #
# Codigo para probar su tarea - No necesitan entenderlo #


def print_data(persona):
    if persona is None:
        print("[AVISO]: get_persona no está implementado")
        return

    for key, val in persona.__dict__.items():
        print("{} : {}".format(key, val))
    print("-" * 80)


# Metodo que sirve para crear el directorio db si no existia #

def make_dir():
    if not os.path.exists("./db"):
        os.makedirs("./db")


if __name__ == '__main__':
    make_dir()
    crear_persona("jecastro1", "Jaime Castro")
    crear_persona("bcsaldias", "Belen Saldias")
    crear_persona("kpb", "Karim Pichara")
    set_persona_favorita("jecastro1", "bcsaldias")
    set_persona_favorita("bcsaldias", "kpb")
    set_persona_favorita("kpb", "kpb")
    agregar_amigo("kpb", "jecastro1")
    agregar_amigo("kpb", "bcsaldias")
    agregar_amigo("jecastro1", "bcsaldias")

    jecastro1 = get_persona("jecastro1")
    bcsaldias = get_persona("bcsaldias")
    kpb = get_persona("kpb")

    print_data(jecastro1)
    print_data(bcsaldias)
    print_data(kpb)

    print(get_persona_mas_favorita())
