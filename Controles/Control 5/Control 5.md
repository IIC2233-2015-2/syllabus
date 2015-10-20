# Control 5

### Forma 1
**Explique en qué consisten los métodos ``setUp`` y ``tearDown`` de ``unittest``, ¿Cuál es la principal ventaja de estos métodos?**

###### Basado en el material de [**Testing**](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/07_TESTING/8-Testing.html)

* ``setUp``: método que se ejecuta automáticamente **antes** de cada test, de manera que permite establecer el contexto de las pruebas. 

* ``tearDown``: método que se ejecuta automáticamente **después** de: cada test, lo que permite limpiar los archivos, objetos, etc. generados por la prueba.

La ventaja de ambos métodos recide en que evitan escribir código redundante para cada test, además de ayudar en la independencia de cada test.

-  3 pts por explicar bien ``setUp``
-  3 pts por explicar bien ``tearDown``

### Forma 2
**1) ¿Es posible implementar un test que revise si una función en particular genera una excepción específica?. Justifique su respuesta.**

###### Basado en el material de [**Testing**](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/07_TESTING/8-Testing.html)

Sí, es posible. ``unittest`` permite esto por medio del método ``assertRaises``, y ``pytest`` con el método ``raises``.

Ambos métodos reciben como argumento la excepción que se espera obtener, la función que se desea testear y los parámetro de la función (o bien se puede realizar con la keyword ``with``). En caso de producirse la excepción el test pasa con éxito.

Método ``assertRaises``:
```python
import unittest


class TestearArchivo(unittest.TestCase):

    def test_division_by_zero_a(self):
        self.assertRaises(ZeroDivisionError, lambda x: print(1/x), 0)

    def test_division_by_zero2_b(self):
        with self.assertRaises(ZeroDivisionError):
            print(1/0)
```

Método ``raises``:
```python
import pytest


def test_division_by_zero_a():
    pytest.raises(ZeroDivisionError, print(1/0))


def test_division_by_zero2_b():
    with pytest.raises(ZeroDivisionError):
        print(1/0)
```

-  5 pts por justificar correctamente.
-  1 pt por responder correctamente.


### Forma 3
**¿De qué manera es posible implementar un test unitario para comprobar si un número x existe en una lista de elementos? Escriba un ejemplo.**

###### Basado en el material de [**Testing**](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/07_TESTING/8-Testing.html)

Existen diversas forma de implementarlo. 
En ``unittest``: se debe crear una clase que herede de ``unittest.TestCase``. Se debe crear un método cuyo nombre comience con **test**. Luego se puede utilizar cualquiera de estos dos métodos ``assertIn`` o ``assertTrue`` para comprobar si **x** existe en una lista de elementos:
```python
import unittest


class TestearArchivo(unittest.TestCase):
    def setUp(self):
        lista = [1, 2, 3]
        x = 1

    def test_value_in_list_a(self):
        self.assertIn(x, lista)

    def test_value_in_list_b(self):
        self.assertTrue(x in lista)
```

En ``pytest``: se debe crear una función cuyo nombre comience con **test**. Luego utilizando la keyword ``assert`` y escribiendo la condición que se debe cumplir (``x in lista``) se puede realizar el test:
```python
def test_value_in_list_a():
    lista = [1, 2, 3]
    x = 1
    assert x in list
```

-  4 pts por entregar el ejemplo.
-  2 pts por explicar el procedimiento.

