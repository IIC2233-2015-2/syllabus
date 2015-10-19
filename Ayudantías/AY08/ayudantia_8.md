# Ayudantía 8: PyQt4

### PyQt-khé?
El framework PyQt será el módulo en el que nos centraremos en este curso para desarrollar las interfaces gráficas de **todas las tareas que siguen** :smiling_imp:

Aprendamos a temerle:

¿Alguno se ha atrevido a hacer `help(QtGui)`? ¡Usted no lo intente! Mejor probemos con:
```python
>>> len(dir(QtGui))
372
```

Así es: 372 elementos definidos en el módulo. Varios son clases que heredan de `QtGui.QWidget`. Hoy las conoceremos (bueno... algunas).

### ¿372? ¿Cómo esperan que los dominemos todos?
**¡No lo esperamos!** Ninguno de nosotros pretende que sean unos maestros en PyQt. Solo se espera que sepan buscar por las clases que necesitan en google :stuck_out_tongue_winking_eye:

Como ayuda,  revisaremos algunos widgets/eventos/problemas/magia negra que fueron de importancia para sus ayudantes el semestre pasado.

#### Widgets básicos
* QWidget: ventana básica. Los demás heredan de esta clase.
* QPushButton: botón. Puede vincularse a un método cuando se presione, con `btn.clicked.connect(metodo)`.
* QLabel: etiqueta que sirve para desplegar información, como texto o imágenes. Para mostrar un string, basta con `setText('mensaje')`. 
* QLineEdit: sirve para ingresar texto, el cual se recibe con el método `text()`.
* QTextEdit: similar al anterior, pero permite mostrar el texto ingresado en más de una línea.
* QRadioButton: botones de selección (solo uno de ellos puede estar presionado a la vez). Puedes revisar si uno está chequeado con el método `isChecked()`.
* QVBoxLayout: para organizar verticalmente un conjunto de widgets.
* QHBoxLayout: para organizar horizontalmente un conjunto de widgets.
* QGridLayout: se comporta como una layout tanto vertical como horizontal. ¿Adivinen de qué clase es la `simulationGrid` en la GUI de su tarea 4?

#### Pixmaps
¿Cómo agregar imágenes a una label? Una forma de hacerlo es definiendo un "mapa de bits" como sigue:
```python
pixmap = QtGui.QPixmap(path)    # path para acceder a una imagen
# Se puede modificar el tamaño, o rotar. Por ejemplo:
pixmap.scaledToHeight(150)
# Ahora se agrega a la label
label.setPixmap(pixmap)
```

Además, los pixmaps sirven para definir otros objetos gráficos, de la clase `QGraphicsPixmapItem`. Estos se pueden agregar a una `QGraphicsScene`, la cual tiene métodos útiles para trabajo con varias imágenes, como `clear`. Luego, estas se agregan a una ventana clase `QtGui.QGraphicsView`, como sigue:
```python
ventana = QtGui.QGraphicsView()
scene = QtGui.QGraphicsScene(ventana)
ventana.setScene(scene)

item = QtGui.QGraphicsPixmapItem(pixmap)
scene.addItem(item)
item.translate(30, 60)  # cambiarlo de posicion
```

#### Colores y dibujos
Para dar un color específico a un texto, se puede crear una paleta, luego setearle un color a esta paleta y finalmente, modificar una label (u otro objeto). Ejemplo:
```python
paleta = QtGui.QPalette()
# color es un numero entero, que representa un color
# el modulo QtCore guarda una gran cantidad de  variables enteras
# para representar teclas, colores, etc. Por ejemplo:
color = QtCore.Qt.red   # color = 7
paleta.setColor(QtGui.QPalette.Foregrount, color)
label.setPalette(paleta)
```
Si desean dibujar triángulos/flechas/rectángulos/lo-que-sea, investiguen sobre la clase `QtGui.QPainter`, y  `QPaintEvent`.

#### Ventanas útiles
¡No reinventen la rueda! Si bien ustedes podrían definir sus propias clases heredando de `QWidget`, en muchos casos otra persona ya lo hizo por nosotros.
```python
# Muestra una ventana PopUp con el mensaje:
# ventana es el "parent" de la popup
QtGui.QMessageBox.information(
    ventana, 
    "Titulo", 
    "Mensaje"
)

# Pregunta al usuario
ans = QtGui.QMessageBox.question(
    ventana, 
    "Titulo", 
    "Pregunta", 
    QtGui.QMessageBox.Yes | QtGui.QMessageBox.No
)
if ans == QtGui.QMessageBox.Yes:
    print("El usuario dijo que si!")
    
# Ventana PopUp que pide un texto
texto, ok = QtGui.QInputDialog.getText(
    ventana, 
    "Titulo", 
    "Ingresa tu texto:"
)
if ok:
    print(texto)
else:
    print("La ventana fue cerrada sin ingresar texto")
    
# que creen que hace esto?
path = QtGui.QFileDialog.getOpenFileName(ventana)
```

#### Eventos
Las widgets de PyQt4 cuentan con algunos métodos especiales que se ejecutan cuando ocurre algún evento. Estos reciben como argumento un evento que tiene empaquetada la información de qué ocurrió. Por ejemplo, 
```python
class Ventana(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)  # para poder seguir el mouse
        
    def keyPressEvent(self, QKeyEvent):
        # se ejecuta cuando una tecla es presionada
        if QKeyEvent.key() == QtCore.Qt.Key_Return:
            print("Presionarion ENTER!")
            
    def mousePressEvent(self, QMouseEvent):
        # se ejecuta cuando se presiona el mouse
        if QMouseEvent.buttons() == QtCore.Qt.LeftButton:
            print("Hizo click derecho!")
            
    def mouseMoveEvent(self, QMouseEvent):
        # se ejecuta cuando se mueve el mouse
        boton = QMouseEvent.buttons()
        # coordenada x actual del mouse
        x = QMouseEvent.x()
        # IMPORTANTE:
        #   x se mide con respecto a la
        #   esquina superior izquierda
        #   DEL WIDGET en que se implemento el metodo
        #   (este puede ser un boton, por ejemplo)
        
    def closeEvent(self, QCloseEvent):
        ans = QtGui.QMessageBox.question(
            self, 
            "Titulo", 
            "Salir?", 
            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No
        )
        if ans == QtGui.QMessageBox.Yes:
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
```

#### Threading, problemas con el main thread y PROPERTIES

Si utilizan threads que modifican gráficamente una ventana, se pueden encontrar con errores feos (ni siquiera en la sintaxis de python) como:
```
QObject::startTimer: timers cannot be started from another thread
```

PyQt4 tienes sus propios threads (`QtCore.QThread`), pero aunque lo intenten con estos, seguramente tampoco funcionará. Esto ocurre porque, para poder detectar eventos como los que se describieron antes, la propia ventana tiene threads corriendo que le avisan cuando un evento es gatillado. Para evitar conflictos al cambiar las widgets de una ventana, existe un main thread que es el encargado de actualizar la interfaz, y se lanzan estos errores cuando la interfaz se está intentando modificar desde un thread distinto.

Esto se puede solucionar definiendo **signals** que le avisen al main thread que ocurrió algo, para que este haga las modificaciones correspondientes. ¡Igual que con los métodos de arriba!

Por ejemplo, escribamos una clase que cuyas instancias le avisen a la ventana que debe cambiar una imagen de lugar cuando se modifique determinado atributo posición (**¿ven por qué eran útiles las properties?**).


#### Ejercicio propuesto

Escriba una clase `BotonMovil` que herede de `QPushButton` y tenga texto inicial "renombrame", cuyas instancias se puedan mover al mantener click izquierdo sobre ellos. Además, cuando se hace click derecho, se debe abrir una ventana que pida un texto al usuario, y cambiar el nombre del botón.

