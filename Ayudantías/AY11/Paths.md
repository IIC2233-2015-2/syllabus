# Moviéndose a través de directorios

Primero que todo, ¿por qué necesitamos movernos a través de directorios?¿Por qué aprender esto? Bueno, **un sistema organiza archivos y los guarda** en algún lugar de su memoria, pero nosotros vemos algo que parece una url:

```
$ Users/Me/Files/virus.exe
```

> El símbolo `$` se utiliza comunmente para hacer referencia a los comandos en consola, así como `>>` se usa para hacer referencia a los comandos en Python

La explicación es que la mayoria de los sistemas que hoy usamos siguen una **organización jerárquica o de árbol**. En esta organización de arbol el primer nodo es la raiz o *root* y bajo este nodo encontramos archivos y directorios (carpetas), donde cada directorio a su vez contiene archivos y subdirectorios y así sucesivamente...

## ¿Y qué es un path?

Un *path* es una ruta o camino que **especifica una única ubicación de un archivo o directorio en un sistema**. Como la mayoría de los sistemas que hoy usamos siguen la misma estructura de árbol, el moverse a través de paths no es "una cosa de Python", sino algo que **deben saber**. 

Existen dos tipos de *paths*:

* **Absolutos (*full path*):** Apunta a la dirección "completa" en un sistema, por lo tanto el *path* **debe iniciar con el directorio raiz**. 

* **Relativos (*relative path*):** Sigue la ruta a partir del directorio actual. Por ejemplo, el nombre de un archivo puede considerarse una ruta relativa.

> **Importante:** El detalle de cada comando/caracter puede variar entre distintos sistemas y lenguajes. Estas diferencias son pequeñas, por lo que si aprenden una vez se manejarán en todo sistema. 

Algunas representaciones de paths que utilizan los principales sistemas operativos y/o consolas:

| Caracter | Detalle |
| ----- | ----- | 
| `\` | Lleva al *root* |
| `.` | Directorio actual |
| `..` | Directorio padre 

> Los sistemas basados en Unix/Linux usan `/` (*slash*) en vez de `\` (*backslash*). Python usa `\` como "escapador de caracteres" (Recuerda: `\n`)

## ¿Cómo uso esto?

Los caracteres que vimos antes son "acumulables", podemos combinarlos y movernos a través de nuestras carpetas y archivos como queramos. Veamos algunos ejemplos con la siguiente organización:

```
Root:
|
│   system.exe  
│
├───Images
|   ├───Vacaciones
|   |	| playa.jpg
│   │   fondo_de_pantalla.jpg
|   |   ...
|
├───Videos
|   | video1.mp4
|   | ...
|
├───Music
|   | happy_birthday.mp3
|   | ...
```

Veamos algunos paths:

* `$ Root:\Images`
Lleva a la carpeta Images. Este **es un full path porque incluye al directorio raiz!**

* `$ Root:\Images\Vacaciones\playa.jpg`
Esta es la ruta compelta al archivo playa.jpg

* Si estamos en la carpeta Videos... ¿cómo llegamos a la carpeta Music? `$ ..\Music`. **Con `..` "subimos" de directorio**.

* ¿Es el siguiente un path válido? `$ /../..` (Estamos "subiendo" cuando ya estamos en root). La respuesta es **sí**, y nos deja en root.

Entonces, partiendo desde Music, ¿donde nos deja la siguiente ruta?
```
$ .././../../.././Videos/./.././Music/../../Images/.
```


# ¿Y cómo se hace en Python?

En python muchas veces podemos requerir movernos entre carpetas. Por ejemplo, teniendo la siguiente organización:

```
Tarea 6: 
|
|	42.txt
|	main.py
│
├───Modulos
|   | modulo.py
├───css
|   | style.css
|	| bootstrap.css
├───js
|	| script.js
├───static
|   ├───html
|	|	| index.html
|	|	| contact.html
```

¿Cómo puedo decirle a Python que abra el archivo? Fácil, moviendo el archivo a la carpeta del main \**duh*\*... **¡NO!** Si sabemos que el archivo `42.txt`siempre se va a encontrar en esa ubicación **relativa** a nuestro `modulo.py`, es mejor que lo abramos de la siguiente forma:

```python
with open("..\\42.txt", "r") as f:
    la_respuesta_a_la_vida_el_universo_y_todo_lo_demás = f.read()
```

En Python, para movernos sobre carpetas y archivos en nuestro equipo lo mejor es usarlos módulos `os` y `os.path`. Con este módulo podremos manejar fácilmente los nombres de archivos y carpetas. Veamos algunas funciones importantes y un par de ejemplos aplicados sobre el diagrama de arriba:

```python
>> import os

# Una forma segura de manejar los nombres de archivos y carpetas 
# principalmente por "/" y "\" es usar:
>> os.path.join("Tarea 6/Modulos", "modulo.py")
'Tarea 6/Modulos\\modulo.py'

# Una forma segura para separar estos nombres es
>> (filepath, filename) = os.path.split('Tarea 6/Modulos\\modulo.py'
)
>> filename
'modulo.py'
>> filepath
'Tarea 6/Modulos'

>> (shortname, extension) = os.path.splitext(filename)
>> shortname
'modulo'
>> extension
'.py'
# La idea de usar esto es para que los programas que hagan sean cross-platform
#(multiplataforma), ya que, como dijimos, incluso un slash puede arruinar un path 


# ¿Como listar los contenidos de un directorio?
>> os.listdir("Tarea 6")
['42.txt', 'main.py', 'Modulos', 'css', 'js', 'static']

# Ahora que tengo muchos nombres, ¿como se si es un archivo o una carpeta?
>> for f in os.listdir("Tarea 6"):
	    if os.path.isdir(os.path.join("Tarea 6", f)):
	   		print("{0} es un directorio".format(f))
	   	elif os.path.isfile(os.path.join("Tarea 6", f)):
	   	    print("{0} es un archivo".format(f))

# ¿Existirá el archivo "secretos_del_universo.zip" en este path?
>> os.path.exists("/secretos_del_universo.zip")
False

# ¿Donde estoy?
>> os.curdir # Relative path
'.'
>> os.path.realpath(".") # Full path 
'root:/Tarea 6'

# ¿Moverse a una carpeta?
>> os.chdir("css")
```

##### Un ejercicio propuesto para que practiquen: 

Creen su propio explorador de carpetas en consola, que separe archivos de carpetas y que permita moverse ingresando paths :grin:. Algo así estaría bien:

```
$ python paths_propuesto.py

Actual:
Tarea 6

Carpetas:
| Modulos
| css
| js
| static

Archivos:
| 42.txt
| main.py

¿Donde te quieres mover?: 
./../Tarea 6/static

==========

Actual:
static

Carpetas:
| html

¿Donde te quieres mover?: 

```
