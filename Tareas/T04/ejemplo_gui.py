#!/usr/local/bin python3
# -*- encoding: utf-8 -*-
from PyQt4 import QtGui
from gui.gui import GrillaSimulacion
import random as rnd

# EJEMPLO COMENTADO DE INTERFAZ GRÁFICA


def main():
    # Aquí se inicializa el sistema de ventanas de PyQt4. Es importante
    # tener claro que aquí aún NO se muestra la ventana de la simulación.
    app = QtGui.QApplication([])

    # Inicializamos la ventana propiamente tal, aún sin mostrarla. Le pasamos
    # una referencia al objeto instanciado más arriba para poder actualizar
    # la interfaz en cada cambio realizado.
    grilla_simulacion = GrillaSimulacion(app, 30)

    # Mostramos la ventana.
    grilla_simulacion.show()

    # Como la simulación es por eventos discretos (muy rápida), es
    # recomendable esperar algún intervalo de tiempo entre actualizaciones
    # de la interfaz. Es importante detallar en el README.md si se decide

    for i in range(1, 21):
        grilla_simulacion.agregar_calle(i, 13)
        grilla_simulacion.agregar_calle(13, i)

    for x in range(1, 21):
        for y in range(1, 31):
            # Esto es equivalente a llamar a grilla_simulacion.agregar_auto
            nuevo_auto = rnd.choice([
                grilla_simulacion.agregar_convertible,
                grilla_simulacion.agregar_sedan,
                grilla_simulacion.agregar_pickup
            ])
            nuevo_auto(x, y, 0, y % 2 == 0)

    # Además existe el parámetro `tiempo_intervalo` de `GrillaSimulacion` que
    # controla el intervalo de tiempo entre actualizaciones. Por defecto parte
    # con un valor igual a 0, para inicializar la iterfaz rápido, pero luego
    # deben modificarlo para que la simulación muestre los cambios a una
    # velocidad más amigable.
    grilla_simulacion.tiempo_intervalo = 0.5

    for x in range(1, 21):
        for y in range(1, 31):
            grilla_simulacion.quitar_imagen(x, y)

    # Bloqueamos el thread principal para que la ventana permanezca abierta.
    # Cuando se cierra la ventana, el thread principal se libera y se termina
    # la ejecución del programa.
    app.exec_()

if __name__ == '__main__':
    main()
