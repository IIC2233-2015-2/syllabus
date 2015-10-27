import threading


class Worker(threading.Thread):
    mean_data = dict()      # para guardar los promedios
    # Sientete libre para usar otras
    # variables estaticas aqui si quieres

    # programa el __init__
    # recuerda imprimir cual es el comando
    # para el cual se creo el worker
    def __init__(self, star_name, function_name):
        super().__init__()
        pass

    @staticmethod
    def functions(func_name):
        """
        Este metodo recibe el nombre de una funcion
        y retorna una funcion que calcula promedio
        o varianza segun el argumento.
        Se necesita haber calculado promedio
        para poder calcular varianza
        """

        def mean(star_name):
            with open("{}.txt".format(star_name), 'r') as file:
                lines = file.readlines()
                ans = sum(map(lambda l: float(l), lines))/len(lines)
                Worker.mean_data[star_name] = ans
                return ans

        def var(star_name):
            prom = Worker.mean_data[star_name]
            with open("{}.txt".format(star_name), 'r') as file:
                lines = file.readlines()
                n = len(lines)
                suma = sum(map(lambda l: (float(l) - prom)**2, lines))
                return suma/(n-1)

        return locals()[func_name]

    # escriba el metodo run
    def run(self):
        pass


if __name__ == "__main__":
    command = input("Ingrese siguiente comando:\n")

    while command != "exit":
        # Complete el main:
        #   - Que no se caiga el programa al ingresar inputs invalidos
        #   - Revisar que no haya un worker ejecutando el comando
        #   - Revisar que solo se puede calcular var estrella
        #           si ya se calculo mean estrella
        #   - Si corresponde: crear worker, echarlo a correr

        command = input("Ingrese siguiente comando:\n")

    # imprimir cuales comandos
    # alcanzaron a terminar, y cuales no
