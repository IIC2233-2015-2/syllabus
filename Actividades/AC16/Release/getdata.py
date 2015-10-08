__author__ = 'Ariel Seisdedos'
import random

random.seed(2015)
"""
Si el programa demora mucho en correr,
remover algunas estrellas de este diccionario
o disminuir la cantidad de datos para cada una
(ultimo elemento de la lista stars[s])
"""
stars = {"Sirius": [{"mu": -1.47,
                     "sigma": 0.2},
                    4000000],
         "Canopus": [{"mu": -0.72,
                      "sigma": 0.1},
                     3500000],
         "AlphaCentauri": [{"mu": -0.27,
                            "sigma": 0.15},
                           5000000],
         "Arcturus": [{"mu": -0.04,
                       "sigma": 0.05},
                      2500000],
         "Vega": [{"mu": 0.03,
                   "sigma": 0.8},
                  3000000]}


if __name__ == "__main__":

    for name, data in stars.items():

        with open(name+".txt", "w") as file:
            for _ in range(data[-1]):
                file.write("{}\n".format(random.gauss(**data[0])))
