#!/usr/local/bin python3
# -*- encoding: utf-8 -*-
from PyQt4 import QtGui
from gui.gui import GrillaSimulacion


def main():
    app = QtGui.QApplication([])
    grilla_simulacion = GrillaSimulacion()
    grilla_simulacion.agregar_ambulancia(1, 1, 0, True)
    grilla_simulacion.agregar_auto(2, 2, 90, False)
    grilla_simulacion.agregar_casa(3, 3)
    grilla_simulacion.agregar_cuartel_bomberos(4, 4)
    grilla_simulacion.agregar_carro_bomba(5, 5, 180, True)
    grilla_simulacion.agregar_comisaria(6, 6)
    grilla_simulacion.agregar_enfermo(20, 5)
    grilla_simulacion.agregar_hospital(8, 8)
    grilla_simulacion.agregar_incendio(9, 9)
    grilla_simulacion.agregar_patrulla(10, 10, 0, False)
    grilla_simulacion.agregar_robo(11, 11)
    grilla_simulacion.agregar_taxi(12, 13, 0, True)
    grilla_simulacion.quitar_imagen(3, 3)

    for i in range(1, 21):
        grilla_simulacion.agregar_calle(i, 13)
        grilla_simulacion.agregar_calle(13, i)

    grilla_simulacion.show()
    app.exec_()

if __name__ == '__main__':
    main()
