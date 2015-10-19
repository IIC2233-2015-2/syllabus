# GUI 2.0

----
## Qué cambios tiene?

En esta nueva GUI se realizan varios cambios internos que debiesen facilitar su uso. Además se le modifica un único comportamiento para que su simulación pueda correr más fluida. Esto implica que todos los métodos ya existentes se mantienen iguales a la versión anterior y se le agrega un único método nuevo.

Se normalizó para que todos los métodos que reciban coordenadas tomen los atributos `(x,y)` en ese orden, donde **x** representa la fila e **y** la columna.

La interfaz ahora notifica algunos errores mediante la impresión de mensajes por consola y maneja bastantes excepciones. Si usted intenta agregar un objeto en una posición que no existe, se imprimirá el error, se ignorará ese comando y la interfaz seguirá funcionando normalmente.

---
## Uso
Para utilizar esta gui, simplemente descargue el archivo `gui.py` y cámbielo por el antiguo archivo que se encuentra dentro de la carpeta `gui` en su repo de la tarea 4.

---
## Método nuevo

La clase `GrillaSimulacion`ahora posee el nuevo método

```python
GrillaSimulacion.actualizar() 
```
Este actúa en conjunto con el atributo `tiempo_intervalo` para ir actualizando la interfaz en intervalos más amigables para aquel que esté observando.

A diferencia de la interfaz antigua, este método permite hacer **todos** los cambios acumulados hasta el momento en conjunto, pero siempre manteniendo `tiempo_intervalo` segundos entre cada conjunto de actualizaciones

### Ejemplo

Agregamos una calle y dos casas a la interfaz

```python
grilla = GrillaSimulacion(app, 30, 30)
grilla.agregar_calle(2, 2)
grilla.agregar_casa(4, 4)
grilla.agregar_casa(5, 10)
```

En este instante, la interfaz aún se mostrará en blanco. Para que se vea lo que ha cambiado, basta llamar el método `actualizar`

```python
grilla.actualizar()
```

Ahora todos los cambios se debiesen ver reflejados.

---
## Utilidad

Veamos cómo el método `actualizar` puede ser de gran utilidad para su simulación. Observe el siguiente código:

```python
grilla.tiempo_intervalo = 0.5
for x in range(1, 31):
    for y in range(1, 31):
        grilla.agregar_casa(x, y)
        grilla.actualizar()
```

Esto debiese ir agregando casas llenando por fila de izquierda a derecha y luego hacia abajo. Cada casa se agrega cada 0.5 segundos.

Ahora, tome el siguiente código

```python
grilla.tiempo_intervalo = 0.5
for x in range(1, 31):
    for y in range(1, 31):
        grilla.agregar_casa(x, y)
    grilla.actualizar()
```

Nótese que el método `actualizar` se llama ahora dentro del primer for. Esto quiere decir que se llama una única vez por fila. Esto se traduce a que en la interfaz se llenarán las filas con casas desde arriba hacia abajo. Cada ** *FILA* ** se imprimirá cada 0.5 segundos, y toda la fila se llenará de casas en el mismo instante.

Por último, si al mismo código le agrega un nuevo comando al final:

```python
grilla.tiempo_intervalo = 0.5
for x in range(1, 31):
    for y in range(1, 31):
        grilla.agregar_casa(x, y)
    grilla.actualizar()
print("Terminamos!")
```
El comando `print("Terminamos!")` se ejecutará *sin* atraso alguno. Es decir, se observará en consola `Terminamos!` incluso antes de que comiencen a mostrarse las casas en la interfaz.


Esto debiese permitirle separar por completo el flujo de la simulación al del uso de la interfaz gráfica y a su vez darle mayor libertar para elegir qué cosas desea ir actualizando en la interfaz.
