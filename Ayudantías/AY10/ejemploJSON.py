import json


class Vehiculo:

    def __init__(self, patente, marca, capacidad, ruedas):
        self.patente = patente
        self.marca = marca
        self.capacidad = capacidad
        self.ruedas = ruedas

    @classmethod
    def by_json(cls, atributos):
        return cls(**atributos)


v = Vehiculo('BB-NN-47', 'FasterFaster', '5', 3)
print(v.__dict__)

vSerializado = json.dumps(v.__dict__)

vDeserializado = json.loads(vSerializado)
# print(type(vDeserializado))
vClon = Vehiculo.by_json(vDeserializado)

print(vClon)

print(vClon.__dict__)
