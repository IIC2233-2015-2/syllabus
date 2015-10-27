# Ayudantía 3: Debuggeo y documentación

## Docstrings - Documentando formalmente nuestro código

Muchas veces usando módulos de Python nos hemos encontrado con funciones o métodos que no sabemos que hacen, ¿y qué hacemos? Quizás reconozcan esto:

```python
help(funcionDesconocida)
```

También quizás reconozcan esto de algun código que hayan escrito alguna vez:

```python
def sentido_de_la_vida_el_universo_y_todo_lo_demas(parametro_desconocido):

	# mucho codigo por aqui
	# mas codigo por aca
	# ...
	# y voilá

	return 42
```

En esta función no es claro qué hace el código, ni de qué tipo debe ser el parámetro que le damos... Si lo piensas, tiene lógica escribir en alguna parte **cómo funciona nuestro código**, **qué necesita una función** o **qué constantes tiene una clase**. 

Pero, si yo quiero que alguien ocupe mi código, ¿cómo puedo hacer que Python entregue esta información?, ¿existe alguna convención como PEP8 para esto? Pues bien, veamos un poco de esto para facilitar la vida de nuestros futuros compañeros programadores :grin:

Cabe mencionar que algunas IDEs, como PyCharm, **analizan estos docstring y te ayudan a programar mostrando autocompletado o te avisan cuando estás usando mal algún método o clase.**

#### PEP287: reStructuredText Docstring Format

Existen muchas formas de poder informar a los usuarios y otros programadores sobre cómo usar nuestro código. Por esta razón es que nace la **PEP287** [*(más sobre PEPs al final)*](#sobre-peps). Simplemente llamemosla **convención reST**.

En Python, existen los *docstrings*, que son descripciones de módulos, clases y funciones. Estas descripciones se escriben como un string especificado en nuestro código que, tal como un comentario, entrega información útil de un segmento de código. 

Bueno, ya que dijimos que no le diríamos "PEP287" cambiemos el título de la sección antes de seguir.

#### reST y algunos ejemplos

Aprender a hacer un buen código es cosa de costumbre, es una **sana costumbre**. Por esto, no hay mejor manera de aprender que con ejemplos y unas pequeñas reglas que veremos aplicadas. Escribamos un archivo `modulo.py` de ejemplo para que veas cómo se escriben los *docstrings*:

```python
"""
Este (doc)string es el encabezado de nuestro archivo, cuando pidamos
información de este módulo, obtendremos este texto. Observa bien
que estamos escribiendo dentro de 3 comillas (") pues asi podemos
escribir multiples lineas.
"""

class MiClase:
    """Aqui pondremos informacion relevante de nuestra clase, asi 
    podremos conocer con exactitud las constantes y métodos
    disponibles cuando usemos MiClase."""

    def algun_metodo(self):
        """Quizas ya sabemos que este metodo existe y debería ser
        listado cuando pidas informacion sobre MiClase, pero no 
        sabemos a la primera de que tipo es el argumento retornado
        por este metodo ni de que tipo son los argumentos que debemos
        darle. Ya veremos eso mas adelante."""
        pass
        

def alguna_funcion():
    """No solamente podemos escribir informacion sobre nuestras clases
    y metodos de clases, sino que tambien de cualquier funcion. Tan
    solo tienes que rellenar tu texto aqui."""
    pass
```

Ahora, ¿cómo podemos acceder a esta documentación? Bueno, una forma es abriendo el archivo y leyendolo (*duh*), pero eso es muy poco práctico :stuck_out_tongue_winking_eye:, hay formas mejores. La mejor forma es usar `help()`. Python puede reconocer los *docstrings* y cuando pides información de un método, una clase o un módulo desde consola obtenemos el *docstring* correspondiente:

```python
>>> import modulo
>>> help(modulo)

# Aqui saldra mucha información, como el nombre del módulo, la 
# descripción, clases y sus metodos, funciones, constantes
# y la ruta al archivo, pero para resumir...

DESCRIPTION
    Este string es el encabezado de nuestro archivo, cuando pidamos
    información de este módulo, obtendremos este texto. Observa bien
    que estamos escribiendo dentro de 3 comillas (") pues asi podemos
    escribir multiples lineas.

# Aqui saldra mas informacion, pero ya entendiste la idea :P

>>> help(modulo.MiClase)
# -> Docstring de la clase

>>> help(modulo.MiClase.algun_metodo)
# -> Docstring del metodo de la clase

>>> help(modulo.alguna_funcion)
# -> Docstring de la funcion 
```

Ya tienes una idea bastante general, pero dijimos que podríamos saber los tipos de argumentos y de lo que obtenemos de las funciones (y métodos)...

### Documentando de mejor forma las funciones

Esto sin duda que es una buena práctica, más aun cuando estamos haciendo códigos muy largos, funciones mágicas y cosas que podrían confundir a quien lo lea a futuro (incluyéndonos), pues puede ser que a otro programador no le interese lo que hace el código, sino que simplemente quiere saber para qué le sirve y usarlo. (*¿Acaso has leido el código de Python? Sabemos como usar las listas, pero pocos se preguntan cómo es el verdadero código detrás*)

Bueno, para esta parte la PEP nombrada antes no especifica mucho, pero a fin de cuentas son convenciones. Veamos una función que suma dos valores y retorna el resultado como string:

```python
def funcion(x, y):
	return str(x + y)
```

Quizás alguien lea el código y no sepa cuáles son los parámetros correctos para darle, ni los tipos de estos parámetros, o qué se obtiene como resultado ni su tipo. Para especificar qué esperamos recibir y qué deberíamos retornar podemos indicarlo vía *docstring*:

```python
def funcion(primerValor, segundoValor):
	"""Suma dos valores y retorna el resultado como string

	:param primerValor: Numero al que le quiero sumar otro.
	:type primerValor: int or float
	:param segundoValor: Numero que le sumare al primero.
	:type segundoValor: int or float
	:returns: Suma de los valores en forma de string.
	:rtype: str
	"""
	return str(primerValor + segundoValor)
```

Otra convención bastante popular últimamente es la [**Guía de Estilo para Python de Google**](https://google-styleguide.googlecode.com/svn/trunk/pyguide.html), que en muchos puntos es compatible con la PEP257 [*(más sobre Guías de Estilo al final)*](#sobre-guias-de-estilo). Esta sugiere:

```python
def funcion(primer_valor, segundo_valor):
	"""Retorna la suma de dos valores como string

	Esta funcion toma dos argumentos y aplica los axiomas
	del algebra para sumar usando dedos (?) y escribir el 
	número de dedos como string. Es decir, hace magia.

	Args:
		primer_valor (int): Descripcion del primer argumento
		segundo_valor (int): Descripcion del segundo argumento

	Returns:
		str: Descripcion de la salida
	"""
	return str(primer_valor + segundo_valor)
```

Una vez más, debemos recordar que son convenciones. Si bien son recomendaciones, a lo largo del curso queremos que se acostumbren a escribir buenos códigos, con buena documentación y que sigan las buenas costumbres, por lo que esperamos que apliquen esta convención para explicar lo que escriban (y de paso facilitarle la vida a sus ayudantes).

______

###### Sobre PEPs:
 Por si te lo preguntas: **PEP** significa **P**ython **E**nhancement **P**roposals, que vendría siendo algo así como Propuestas de mejoras para Python. Existen muchas propuestas y puedes consultarlas en el índice, que corresponde a la [**PEP 0**](https://www.python.org/dev/peps/). Existen Meta-PEPs (PEPs de PEPs o de procesos) como [**PEP8**](https://www.python.org/dev/peps/pep-0008/), PEPs informativas como [**PEP478**](https://www.python.org/dev/peps/pep-0478/) que incluye los cambios que vendrán en Python 3.5, PEPs implementadas como la [**PEP465**](https://www.python.org/dev/peps/pep-0465) que incluirá desde Python 3.5 un nuevo operador ("@") para multiplicación de matrices, y muchos otros tipos. El que busca siempre encuentra :wink:

###### Sobre Guias de Estilo:
 Como seguramente ya supondrás, una **Guía de Estilo** es un **conjunto de reglas o convenciones** para escribir código en algun lenguaje de programación en específico. Una forma de hacerse una idea es viendo los ejemplos de [**Wikipedia**](https://es.wikipedia.org/wiki/Estilo_de_programaci%C3%B3n). Pero ¿para qué me sirve esto?. Estas reglas no son solo para que el código se vea "bien", la idea de fondo es que cualquier otro programador que llegue después a leer tu código entienda de forma clara qué hace tu programa. En **Python** ya conoces **PEP8**, que funciona bastante bien y es de las más utilizadas por los programadores en Python. Pero no es la única guía, ni tampoco el único lenguaje con una. En [**este repo**](https://github.com/SalGnt/cscs), bastante reciente, podrás encontrar una lista de muchas convenciones y Guías de Estilo utilizadas para muchos lenguajes, incluido Python :snake:
