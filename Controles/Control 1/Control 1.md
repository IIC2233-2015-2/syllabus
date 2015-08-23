# Control 1 

### Pregunta 1
**¿Qué es el overriding de operadores y para qué sirve? Escriba un ejemplo (en código).**

###### Basado en el material de [**Poliformismo**](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/01_OOP/3-Polimorfismo.html)

*Overriding* es la implementación de un método en una subclase, lo que *invalida* la implementación del mismo en la super clase. Por lo tanto, el *overriding de operadores* es la implementación de algún operador (como `__add__`) en una clase de forma que podamos personalizarlo para que funcione como necesitemos.

```python
class Curso():

	def __init__(self, alumnos):
	    self.lista_alumnos = alumnos

    # Sobreescribimos el operador __add__ (+)
    # para que cuando sumemos instancias de la clase Curso ...
    def __add__(self, otro_curso):
        # ... unamos las listas de alumnos ...        
        acumulado = self.lista_alumnos + otro_curso.lista_alumnos
        # ... y retornamos un nuevo objeto (el resultante)
        return Curso(acumulado)
```

 Usandolo en tiempo de ejecución:

```python
>>> IIC2233_2015_1 = Curso(alumnos_2015_1)
>>> IIC2233_2015_2 = Curso(alumnos_2015_2)
>>> IIC2233 = IIC2233_2015_1 + IIC2233_2015_2
>>> len(IIC2233.lista_alumnos) 
# len(IIC2233_2015_2) + len(IIC2233_2015_1)
```

### Pregunta 2
**Explique cómo la sentencia `super()` permite evitar el problema del diamante.**

###### Basado en el material de [**Herencia y Multiherencia**](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/01_OOP/2-Herencia-Multiherencia.html)

Para que cada clase se preocupe de llamar el método de la clase que la *precede* en el orden del esquema de multiherencia, debemos decirle este orden a Python. Pero, ¿cómo lo hacemos? A través de la sentencia `super()`. Esta sentencia permite evitar el problema del diamante **diciendole a Python desde donde hereda** la sub-clase (la que *invoca* `super()`), lo que permitirá que Python se encargue de que la llamada corresponda a la clase que respeta el orden en la multiherencia.

### Pregunta 3
**¿Cuál es la diferencia entre una variable que pertenece a la clase y una que pertenece a la instancia? Explique cómo se define la variable en cada uno de los casos.**

En el caso de las **variables de clase** estas corresponden a las definidas dentro del bloque de clase (`class ...`), y son comunes a todas las instancias. Mientras que las **variables de una instancia** se definen en tiempo de ejecución, cuando usamos `__init__` por ejemplo y cuyo valor solo pertenece a la instancia.

```python
class AlgunaClase:

    def __init__(self):
        self.foo = 'Soy un atributo de la instancia llamado foo'
        self.foo_list = []

    bar = 'Soy un atributo de la clase llamado bar'
    bar_list = []
```

Profundizando un poco en esto, la variable que pertenece a la clase es una propiedad (atributo/función) de la clase que es independiente de la instancia con la que se intente acceder a ella, un atributo o función independiente de la instancia. Independiente de la instancia quiere decir que no necesariamente se necesita una para conocer el valor o ejecutar la función, y que es como una variable global pero que pertenece a una clase.

```python
class A:

	variable_independiente = 90

	def __init__(self):
		pass

	

# Podemos acceder a esta variable desde la clase...
print(A.variable_independiente)
>> 90

# ... desde instancias...
objeto1 = A()
print(objeto1 .variable_independiente)
>> 90

# ... y si modificamos el valor en la clase,
# se modifica en la instancia
A.variable_independiente = 3
print(objeto1.variable_independiente)
>> 3
```

Si se le cambia el valor para una instancia en particular, entonces solo se cambia para esa:
```python
objeto1 = A()
objeto2 = A()
objeto2.variable_independiente = 3

# El valor en la clase permanece intacto...
print(A.variable_independiente)
>> 90

# ... al igual que el de las instancias ...
print(objeto1 .variable_independiente)
>> 90

# ... excepto la instancia a la que le dijimos que cambiara el valor
print(objeto2 .variable_independiente)
>> 3
```
