from PyQt4 import QtGui
from PyQt4 import QtCore
import time


class MoveMyImageEvent:
    """
    Las instancias de esta clase
    contienen la informacion necesaria
    para que la ventana actualice
    la posicion de la imagen
    """
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y


class Character(QtCore.QThread):
    trigger = QtCore.pyqtSignal(MoveMyImageEvent)
    # pyqtSignal recibe *args que le indican
    # cuales son los tipos de argumentos que seran enviados
    # en este caso, solo se enviara un argumento:
    #   objeto clase MoveMyImageEv
    # TENDRIA MAS SENTIDO QUE ESTE ATRIBUTO NO FUESE ESTATICO?
    #   Intentenlo en casa...
    #   spoiler: PyQt4-KHEEE?
    
    def __init__(self, parent, path, x, y, wait):
        """
        Un Character es un QThread que movera una imagen
        en una ventana. El __init__ recibe los parametros:
            parent: ventana
            x e y: posicion inicial en la ventana
            wait: cuantos segundos esperar
                antes de empezar a mover su imagen
        """
        super().__init__()
        self.image = QtGui.QLabel(parent)
        self.image.setPixmap(QtGui.QPixmap(path))
        self.image.show()
        self.image.setVisible(True)
        self.trigger.connect(parent.actualizarImagen)
        self.__position = (0, 0)
        self.wait = wait
        
        # esta linea se ve inocente
        # pero va a mandar una senhal (evento) a la ventana
        self.position = (x, y)
        
    @property
    def position(self):
        return self.__position
        
    @position.setter
    def position(self, value):
        self.__position = value

        # El trigger emite su senhal a la ventana
        self.trigger.emit(MoveMyImageEvent(
            self.image, self.position[0], self.position[1]
        ))

        # Prueben cambiar las lineas anteriores
        # por lo siguiente (para que el thread mueva
        # directamente la label "self.imagen")
        # self.image.move(self.position[0], self.position[1])
        
    def run(self):
        time.sleep(self.wait)
        for i in range(0, 100, 10):
            for j in range(100):
                time.sleep(0.01)
                self.position = (i, j)


class Ventana(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 100, 400, 500)
        self.setWindowTitle("Ejemplo")

    # La sintaxis es igual que para los 
    # ejemplos en el item anterior
    # esto recibira un objeto clase MoveMyImageEvent
    def actualizarImagen(self, myImageEvent):
        label = myImageEvent.image
        label.move(myImageEvent.x, myImageEvent.y)
        
if __name__ == '__main__':
    app = QtGui.QApplication([])
    ventana = Ventana()
    ventana.show()

    # Creamos 10 threads
    # que iran moviendo las imagenes de pato
    # notar que empezaran en momentos distintos
    # pues wait depende de i
    for i in range(10):
        personaje = Character(
            parent=ventana,
            path="mrpatiwi.png",
            x=0, y=0,
            wait=3*(9-i)
        )
        personaje.start()
    app.exec_()
