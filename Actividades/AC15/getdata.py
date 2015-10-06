import random

random.seed(2015)

SLOW_PC = False     # cambiar a True si tarda mas de 3 minutos en ejecutar

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
    # Si AUN tarda mucho
    # reducir el .5 en mult
    mult = .5 if SLOW_PC else 1

    for name, data in stars.items():
        print("Cargando: {}".format(name))

        with open(name+".txt", "w") as file:
            for _ in range(mult * data[-1]):
                file.write("{}\n".format(random.gauss(**data[0])))
