__author__ = 'cppie_000'

from PyQt4 import QtGui, uic

formulario = uic.loadUiType("qt-designer-mainwindow.ui")
print(formulario[0], formulario[1])

class MainWindow(formulario[0], formulario[1]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton1.clicked.connect(self.dividir)
        #self.btn_new.clicked.connect(self.btn_newGame_clicked)

    def dividir(self):
        self.label_3.setText('= ' + str(float(self.lineEdit1.text()) / float(self.lineEdit2.text())))

if __name__ == '__main__':
    app = QtGui.QApplication([])
    form = MainWindow()
    form.show()
    app.exec_()