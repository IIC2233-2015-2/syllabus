# coding=utf-8


class Personal:

    def __init__(self, nombre):
        self.nombre = nombre


class Guardia(Personal):

    def __init__(self, equipamento, **kwargs):
        super().__init__(**kwargs)
        self.equipamento = equipamento
