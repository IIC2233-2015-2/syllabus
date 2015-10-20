import sys
from PyQt4 import QtGui
from backend import Partida

class Buscaminas(QtGui.QWidget):

    def __init__(self, n, minas):  # con "n" se genera una matriz de nxn
        super(Buscaminas, self).__init__()
        self.n = n
        self.minas = minas
        self.partida = Partida(n, minas)
        ":::COMPLETAR:::"

        self.initUI()

    def initUI(self):
        ":::COMPLETAR:::"

    def buttonClickedLeft(self):
        ":::COMPLETAR:::"

    def apretar_boton(self, posicion):  # Posición como una tupla (x, y)
        "Esta funcion devuelve la cantidad de minas alrededor de un espacio"
        "No tiene ninguna relación con lo que sucederá en la UI"
        boton = self.partida.botones[posicion]
        return self.partida.clickear(boton)

    def notificar(self, mensaje):
        ":::COMPLETAR:::"
        "Debe notificar a traves de un label cuando muera o sobreviva"


if __name__ == '__main__':
        app = QtGui.QApplication(sys.argv)
        ex = Buscaminas(5, 10)
        sys.exit(app.exec_())
