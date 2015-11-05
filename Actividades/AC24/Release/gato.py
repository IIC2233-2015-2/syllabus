import sys


class Gato:
    def __init__(self):
        self.estado = [[" ", " ", " "] for j in range(3)]
        self.turno = "X"
        self.turnos = {"X": "O", "O": "X"}

    def editar_posicion(self, posicion):
        if self.estado[int(posicion[0])][int(posicion[1])] == " ":
            self.estado[int(posicion[0])][int(posicion[1])] = self.turno
            self.turno = self.turnos[self.turno]

    def revisar_ganador(self):
        # revisa fila
        for fila in self.estado:
            ultimo_elemento = fila[0]
            contador = 0
            for elemento in fila:
                if ultimo_elemento == elemento and ultimo_elemento != " ":
                    contador += 1
            if contador == 3:
                print("El jugador {0} ha ganado".format(ultimo_elemento))
                sys.exit()
        # revisar columna
        for i in range(len(self.estado[0])):
            ultimo_elemento = self.estado[0][i]
            contador = 0
            for j in range(len(self.estado)):
                if self.estado[j][i] == ultimo_elemento and ultimo_elemento != " ":
                    contador += 1
            if contador == 3:
                print("El jugador {0} ha ganado".format(ultimo_elemento))
                sys.exit()
        # revisar diagonales
        ultimo_arriba = self.estado[0][0]
        ultimo_abajo = self.estado[2][0]
        contador_arriba = 0
        contador_abajo = 0
        for i in range(len(self.estado)):
            if self.estado[i][i] == ultimo_arriba and ultimo_arriba != " ":
                contador_arriba += 1
            if self.estado[2 - i][i] == ultimo_abajo and ultimo_abajo != " ":
                contador_abajo += 1
        if contador_arriba == 3:
            print("El jugador {0} ha ganado".format(ultimo_arriba))
            sys.exit()
        elif contador_abajo == 3:
            print("El jugador {0} ha ganado".format(ultimo_abajo))
            sys.exit()

    def __repr__(self):
        lista = []
        for fila in self.estado:
            for valor in fila:
                lista.append(valor)
        tupla = tuple(lista)
        return """
            {0} | {1} | {2}
            -- --- --
            {3} | {4} | {5}
            -- --- --
            {6} | {7} | {8}
            """.format(*tupla)
