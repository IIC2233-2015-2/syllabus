from PyQt4 import QtGui, uic
from calc_financiero import calcular_jub

form = uic.loadUiType("hexa.ui")


class MainWindow(form[0], form[1]):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Completar la creación de la interfaz #

    def calcular(self):
        """ Completar esta función para calcular los cambios de los datos
        en tiempo real según el input del usuario. """
        pass


if __name__ == '__main__':
    app = QtGui.QApplication([])
    form = MainWindow()
    form.show()
    app.exec_()
