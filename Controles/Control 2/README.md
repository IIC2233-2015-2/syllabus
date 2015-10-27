# Control 2

### Forma 1
**Los árboles son una estructura de datos jerárquica. ¿Qué se entiende por un vértice y un camino?**

###### Basado en el material de [**Árboles**](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/02_EDD/06-arboles.html)

Un *vértice* corresponde a la conexión entre un par de nodos (u, v) que tienen una relación directa. 
La secuencia ordenada de nodos consecutivos unidos por un vértice a lo largo de árbol T forman un *camino*.

### Forma 2
**Explique brevemente qué función cumplen los Defaultdicts. Escriba un ejemplo.**

###### Basado en el material de [**Diccionarios**](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/02_EDD/04-dictionaries.html)

Los "defaultdicts" son diccionarios que nos permiten asignar un valor por defecto para los casos cuando se accesa el diccionario usando una "key" que no existe.

```python
dicc = defaultdict(lambda: "vacio")
```

### Forma 3
**Sea una pila _L_, explique la diferencia entre hacer _L.pop()_ y _L[-1]_**

###### Basado en el material de [**Pilas (Stacks)**](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/02_EDD/02-pilas.html)

`L.pop()`: retorna y remueve el último elemento agregado a la pila.

`L[-1]`: retorna el último valor agregado a la pila sin extraerlo.
