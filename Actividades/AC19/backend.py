from random import randint


class Boton:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.mina = False
        self.clickeado = False

    def __repr__(self):
        return str((self.x, self.y)) + " " + str(self.mina)


class Partida:

    def __init__(self, n, minas):
        self.n = n
        self.total = n * n
        self.minas = minas
        self.botones = {}
        self.posiciones_con_mina = []
        self.crear_espacio()
        self.asignar_minas()

    def crear_espacio(self):
        for y in range(self.n):
            for x in range(self.n):
                boton = Boton(x, y)
                self.botones[(x, y)] = boton

    def poner_mina(self):
        pos = (randint(0, self.n - 1), randint(0, self.n - 1))
        if pos in self.posiciones_con_mina:
            self.poner_mina()
        else:
            self.posiciones_con_mina.append(pos)
            self.botones[(pos[0], pos[1])].mina = True

    def asignar_minas(self):
        for i in range(self.minas):
            self.poner_mina()

    def clickear(self, boton):
        if not boton.clickeado:
            boton.clickeado = True
            if boton.mina:
                return "X"
            else:
                return str(self.comprobar_vecinos(boton))

    def comprobar_vecinos(self, boton):
        vecinos = []
        for i in range(-1, 2):
            for r in range(-1, 2):
                xx = boton.x + i
                yy = boton.y + r
                #  Para verificar que no se busque un boton fuera del mapa:
                dentro_limite = (xx >= 0 and yy >= 0 and
                                 xx <= (self.n - 1) and yy <= (self.n - 1))
                # Para que no agregue el mismo boton como uno de sus vecinos:
                mismo_boton = xx == boton.x and yy == boton.y
                if dentro_limite and not mismo_boton:
                    vecinos.append(self.botones[xx, yy])
        # DEVUELVE EL NUMERO DE MINAS A SU ALREDEDOR:
        return len([v.mina for v in vecinos if v.mina])
