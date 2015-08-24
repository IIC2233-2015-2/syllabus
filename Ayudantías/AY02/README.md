# Ayudantía 02
## Modularización de código y de cómo me enamoré de los `import`
Es muy mala práctica hacer un programa donde todo el código vaya en un solo y gran archivo `main.py`.

Lo que tenemos que hacer es separar el programa en módulos donde cada uno tenga cierta funcionalidad bien clara y específica.

Supongamos que tenemos que modelar un zoológico. Una buena opción es tener una estructura del proyecto:

```sh
# Todo esto está adjunto a esta ayudantía.

/modelacion-zoo
|-- main.py
|-- zoologico.py
|-- /animales
|   |-- __init__.py
|   |-- animal.py
|   |-- mamiferos.py
|   |-- reptiles.py
|-- personal.py
```

Si estamos en la clase `Zoologico` del archivo `zoologico.py`, nos gustaría poder agregar `Guardias` del archivo `personal.py`.

Para hacer esto, en `zoologico.py` tenemos las siguientes opciones:

```python
# Importa todo el módulo y accedemos
# a sus contenidos a través de 'personal'
import personal
g = personal.Guardia(nombre='G' + str(i), equipamento=['Equipamento'])

# Podemos usar un 'alias'
import personal as p
g = p.Guardia(nombre='G' + str(i), equipamento=['Equipamento'])
```

```python
# Importa un elemento específico.
from personal import Guardia
g = Guardia(nombre='G' + str(i), equipamento=['Equipamento'])

# Podemos encadenarlos, por ejemplo:
from personal import Guardia, Visitante, Veterinario, crear_personal
```

```python
# Importa absolutamente todo y se accede directamente.
# Esta es la opción MENOS RECOMENDADA porque perdemos control
# de lo que importamos y puede generar conflictos.
from personal import *
g = Guardia(nombre='G' + str(i), equipamento=['Equipamento'])
```

Habrás notado que no solo importa clases, sino que también puedes importar **funciones** y **variables**.

## ¿Qué es y qué hace `@property`?
Las properties son descriptores que invocan una función para acceder a un atributo de una clase. ¿Y esto qué significa? Bueno, en Python podemos definir una property así:

```python
property(fget=None, fset=None, fdel=None, doc=None)
# Retorna el atributo de la property
```

Esta sintaxis indica que: cada vez que intentamos obtener el valor de un atributo (get) se llama a la función en `fget`, cuando queremos definir un atributo (set) se llama a la función en `fset` y lo mismo para borrar un atributo (del) con `fdel`. Ahora, una buena forma de hacer visible el comportamiento sobre nuestro atributo es usar el decorador `@property`.

### Veamoslo aplicado en un ejemplo:

```python
class Termometro:
    def __init__(self, kelvin):
        self.kelvin = temperatura_abs
        self.celsius = self.kelvin - 273
        self.fahrenheit = (self.celsius * 1.8) + 32
```

**¿Qué problemas trae este _approach_?**
1. Estamos ocupando memoria de nuestro computador guardando valores redundantes.
2. Si queremos cambiar el valor de una unidad, tenemos que actualizar los otros dos.

Probemos esta otra solución:

```python
class Termometro:
    def __init__(self, temperatura_abs):
        self.kelvin = temperatura_abs

    def celsius(self):
        return self.kelvin - 273

    def fahrenheit(self):
        return (self.celsius() * 1.8) + 32
```

Funciona, pero es un poco inconsistente al usar:

```python
temp = Termometro(temperatura_abs=293)
c = temp.celsius()      # Con () porque es una función
k = temp.kelvin         # Sin paréntesis, es una propiedad
f = temp.fahrenheit()   # Con () porque es una función
```

Además deberíamos declarar los métodos para poder ejecutar `temp.set_celsius(value)` y `temp.set_fahrenheit(value)` mientras que los `kelvin` se harían simplemente como `temp.kelvin = value`.

#### El approach final y correcto usando `@property`:

```python
class Termometro:
    def __init__(self, temperatura_abs):
        self.kelvin = temperatura_abs

    @property
    def celsius(self):
        return self.kelvin - 273

    @property
    def fahrenheit(self):
        return (self.celsius * 1.8) + 32
```

Ahora sí el uso es consistente y funciona bien:

```python
temp = Termometro(temperatura_abs=293)
c = temp.celsius
k = temp.kelvin
f = temp.fahrenheit
```

Ahora si queremos modificar algún valor, usamos el `setter`:

```python
class Termometro:
    # ...
    @celsius.setter
    def celsius(self, value):
        self.kelvin = value + 273
    # ...

# Uso
temp = Termometro(temperatura_abs=293)
temp.celsius = 31
```

¡Adiós datos redundantes! 👋😄

El código completo del `termometro` lo puedes encontrar [aquí](termometro.py).

**¿Qué hace `@property`?**

Le dice a Python que el método que acabamos de definir en nuestra clase (el que decoramos con `@property`) es en verdad un atributo, y que queremos que cuando hagamos una acción sobre este atributo nuestra clase debería hacer otras cosas, segun las funciones definidas bajo los decoradores `@property.setter`, `@property.getter` y `@property.deleter`.

## Ejercicio Estructura de Datos: `StepStack`
**a)** Se necesita programar una clase llamada `Stack` que utilice internamente una lista y que exponga los métodos `push(value)`, `pop()`, `top()` y `__len__`.

```python
class Stack:

    def __init__(self):
        pass

    def push(self, value):
        pass

    def pop(self):
        return None

    def top(self):
        return None

    def __len__(self):
        return 0
```

**b)** Modificar la solución anterior para que en vez de usar listas, use **nodos**. Para esto debe crear la clase `Node`.

**c)** Basándose en lo anterior, programar una clase `FixedStack` que herede de `Stack`, pero que este ponga un límita de capacidad. El valor del límite de debe declarar en el `__init__`.

```python
class FixedStack(Stack):
    pass
```

**d)** Finalmente, programar una clase `StepStack` que herede de `FixedStack` y vaya concatenandose más `StepStack` a medida que se vayan llenando. Estos deben ser accedidos secuencialmente. Es decir:
1. Intentamos agregar un elemento al `StepStack` principal.
2. Si está lleno, revisamos si hay uno después de él y lo intentamos agregar.
3. Si no existe uno después de él, lo creamos y agruegamos el elemento.

Todo esto de manera recursiva. De manera análoga debe funcionar el `pop()` y `top()`

```python
class StepStack(FixedStack):
    pass
```
