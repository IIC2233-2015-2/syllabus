import threading


class Worker(threading.Thread):
    instances = list()
    mean_data = dict()

    def __init__(self, star_name, function_name):
        super().__init__()
        self.star_name = star_name
        self.function = Worker.functions(function_name)
        self.command = "{} {}".format(function_name, star_name)
        print("Creando Worker para: {}".format(self.command))
        self.setDaemon(True)  # para que mueran cuando acabe el programa ppal
        Worker.instances.append(self)

    @staticmethod
    def functions(func_name):
        def mean(star_name):
            with open("{}.txt".format(star_name), 'r') as file:
                lines = file.readlines()
                ans = sum(map(lambda l: float(l), lines)) / len(lines)
                Worker.mean_data[star_name] = ans
                return ans

        def var(star_name):
            prom = Worker.mean_data[star_name]
            with open("{}.txt".format(star_name), 'r') as file:
                lines = file.readlines()
                n = len(lines)
                suma = sum(map(lambda l: (float(l) - prom) ** 2, lines))
                return suma / (n - 1)

        return locals()[func_name]

    def run(self):
        output = self.function(self.star_name)
        print("Soy el {} y termine mi trabajo!\n"
              "\tEl resultado de {} es {}\n"
              "Ingrese siguiente comando: ".format(
            self.getName(), self.command, output
        ))


if __name__ == "__main__":
    command = input("Ingrese siguiente comando:\n")

    while command != "exit":
        try:
            function, starname = command.split(" ")

            executed = False
            for w in Worker.instances:
                if w.command == command and w.isAlive():
                    print("[DENIED] Ya hay un worker ejecutando el comando")
                    executed = True
                    break

            if not executed:
                if function == "var" and starname not in Worker.mean_data:
                    print("[DENIED] No se puede calcular varianza "
                          "sin haber calculado el promedio antes!")

                elif starname in ["AlphaCentauri", "Arcturus",
                                  "Canopus", "Sirius", "Vega"]:
                    Worker(starname, function).start()

                else:
                    print("[DENIED] Comando invalido\n\t"
                          "El nombre de la estrella no es correcto")

        except (ValueError, KeyError) as err:
            print("[DENIED] {}\n\tComando invalido".format(type(err).__name__))

        command = input("Ingrese siguiente comando:\n")

    print("Comandos ingresados por el usuario:")
    for w in Worker.instances:
        string = "NO alcanzo a terminar: " if w.isAlive() \
            else "Alcanzo a terminar: "
        print(string + w.command)
