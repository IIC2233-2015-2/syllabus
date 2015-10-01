class Ramo:

    def __init__(self, sigla, vacantes, creditos):
        self.sigla = sigla
        self.vacantes = int(vacantes)
        self.creditos = int(creditos.replace("\n", ""))


class Base:

    def __init__(self):
        self.db = []
        with open("ramos.txt") as file:
            for x in file.readlines()[1:]:
                self.db.append(
                    Ramo(x.split("\t")[0], x.split("\t")[1], x.split("\t")[2]))

    def inscribir(self, sigla, alumno):
        # primer error no enconcontrar ramo
        objeto_ramo = next(x for x in self.db if x.sigla == sigla)
        if objeto_ramo.vacantes > 0:
            objeto_ramo.vacantes -= 1
            print("SISTEMA: {} tomado con exito, vacantes restantes: {}".format(sigla, objeto_ramo.vacantes
                                                                                ))
            return True

        else:
            print("{}: lo sentimos {} no tiene vacantes disponibles".format(
                alumno.nombre.upper(), sigla))
            print("SISTEMA: ERROR {} sin vacantes =(\n".format(sigla))
            return False

    def botar(self, sigla, alumno):
        objeto_ramo = next(x for x in self.db if x.sigla == sigla)
        objeto_ramo.vacantes += 1
        print("{}: Ha botado con exito el ramo {}".format(
            alumno.nombre, sigla))


class Alumno:

    def __init__(self, base, creditos,  nombre):
        self.maximo_creditos = 50
        self.base = base
        self.creditos_actuales = creditos
        self.ramos = []
        self.nombre = nombre

    def tomar_ramo(self, sigla):
        # error de busqueda
        creditos = next(x for x in self.base.db if x.sigla == sigla).creditos

        if self.creditos_actuales + creditos <= self.maximo_creditos:
            if self.base.inscribir(sigla, self):
                self.creditos_actuales += creditos
                print("{}: has tomado {} con exito, creditos actuales: {}\n".format(
                    self.nombre.upper(), sigla, self.creditos_actuales))
                if self.chequear_repeticion(sigla):
                    self.agregar_ramo(sigla)
                    return True
                else:
                    return False
                # chequear que no haya tomado ese ramo antes
        else:
            print("{}: ERROR creditos actuales: {} no es posible tomar mas ramos\n".format(
                self.nombre.upper(), self.creditos_actuales))
            return False

    def botar_ramo(self, sigla):
        creditos = next(x for x in self.base.db if x.sigla == sigla).creditos
        self.creditos_actuales -= creditos
        if sigla in self.ramos:
            self.ramos.remove(sigla)
            self.base.botar(sigla, self)
            return True
        else:
            print("{}: ERROR, no tienes el ramo {} que estas botando".format(
                self.nombre.upper(), sigla))
            return False

    def agregar_ramo(self, sigla):
        self.ramos.append(sigla)

    def chequear_repeticion(self, sigla):
        return (sigla not in self.ramos)
