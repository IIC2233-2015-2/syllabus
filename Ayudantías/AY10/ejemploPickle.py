import pickle
from datetime import datetime


class Vehiculo:

    def __init__(self, patente, marca, capacidad, ruedas):
        self.patente = patente
        self.marca = marca
        self.capacidad = capacidad
        self.ruedas = ruedas

    def __getstate__(self):
        aGuardar = self.__dict__.copy()
        hoy = datetime.now()
        aGuardar.update(
            {'fechaAlmacenamiento': (hoy.day, hoy.month, hoy.year)})
        return aGuardar

    def __setstate__(self, nuevo):
        hoy = datetime.now()
        print('\nHora de Deserialización')
        print(str(hoy.hour) + ':' + str(hoy.minute))
        print(hoy.day, hoy.month, hoy.year, '\n', sep='-')
        self.__dict__ = nuevo


v = Vehiculo('BB-NN-47', 'FasterFaster', 5, 3)
# print(id(v))
# print(v.__dict__)

# k = pickle.dumps(v)
# print(k)
# print(id(pickle.loads(k)))

# with open('autito.VEHICULO', 'wb') as archivo:
#     pickle.dump(v, archivo)

# with open('autito.VEHICULO', 'rb') as archivo:
#     vClon = pickle.load(archivo)

# print(vClon.__dict__)
