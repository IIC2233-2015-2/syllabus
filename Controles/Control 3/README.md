# Control 3

### Forma 1

**1) Dada la siguiente función, escriba cómo sería su implementación como una función lambda:**

```python
import numpy as np

def mi_func(a, b):
    return np.sqrt(a**2 + b**2)
```
###### Basado en el material de [**LambdaFunctions**](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/03_FUNCTIONAL/3-Built-ins-Functional.html)

Función lambda:

```python        
mi_func = lambda a,b: np.sqrt(a**2 + b**2)
```

-	Correcta implementación de función lambda 3 puntos
-	Descuento de 0.5 por cada error de sintaxis.

**2) Explique en palabras qué hace la función map.**

###### Basado en el material de [**MAP**](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/03_FUNCTIONAL/3-Built-ins-Functional.html)

La función `map` recibe como parámetros una función y un iterable. Retorna un generador, que resulta de aplicar la función sobre cada elemento del iterable.

-	Nombrar los parámetros que recibe Map, 1 punto.
-	Nombrar lo que retorna Map, 1 punto.
-	Explicar cómo opera Map, 1 punto.

### Forma 2

**Explique en palabras qué hace la siguiente línea de código:**

```python
file_name = "archivo.txt"
f = lambda l : l.rstrip().split()[0]
reduce(str.__add__, map(f, [line for line in open(file_name)]))
```
###### Basado en el material de [**LambdaFunctions/MAP/REDUCE**](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/03_FUNCTIONAL/3-Built-ins-Functional.html)

**Función lambda:** Borrará los espacios del lado derecho del string l, si los tuviera. Luego genera una lista con los substrings de l, ocupando como separador la presencia de un espacio en blanco. Finalmente retornará el primer elemento de la lista, si no hay espacios en blanco, retornará el string completo que compone l.

**Map:** A cada línea del archivo, “archivo.txt”, le aplica la función lambda f y retornará un generador formado por estos strings.

**Reduce:** Aplicará `str.\__add__` a los elementos del generedor creado por `map`. Por lo que concatenará todos los strings que componen el generador en un solo string.

Finalmente se generará un solo string, que está compuesto por el primer string (desde `indice[0]` hasta antes de un espacio en blanco) de cada línea del archivo “archivo.txt”.

-	Correcta explicación función Lambda, 2 puntos.
-	Correcta explicación función Map, 2 puntos.
-	Correcta explicación función Reduce, 2 puntos.



### Forma 3

Explique en palabras qué hace la siguiente línea de código:

```python
file_name = "archivo.txt"
f = lambda l : l.rstrip()[0]
print(reduce(str.__add__, map(f, [line for line in open("logs_out.txt")])))
```
###### Basado en el material de [**LambdaFunctions/MAP/REDUCE**](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/03_FUNCTIONAL/3-Built-ins-Functional.html)

**Función lambda:** Borrará los espacios del lado derecho del string l, si los tuviera. Luego retornará el primer caracter que compone l, es decir `l[0]`.

**Map:** A cada línea del archivo, “logs_out.txt”, le aplica la función lambda f y retornará un generador formado por estos strings.

**Reduce:** Aplicará `str.\__add__` a los elementos del generedor creado por `map`. Por lo que concatenará todos los strings que componen el generador en un solo string y lo imprimirá en consola

Finalmente se obtendrá la impresión de un solo string, que está compuesto por el primer carácter de cada línea del archivo “logs_out.txt”

-	Correcta explicación función Lambda, 2 puntos.
-	Correcta explicación función Map, 2 puntos.
-	Correcta explicación función Reduce, 2 puntos.
-	Descuento de 0.5 por no mencionar la impresión en consola.

