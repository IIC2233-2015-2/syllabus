# Ayudantía 5: Más metaclases, clases abstractas

Las clases asbtractas son clases cuyas instancias no tienen mucho sentido a menos que 
correspondan a alguna sub-clase específica. En python, se implementan a través del módulo 
`abc`, desde el cual se puede importar la (meta)clase `ABCMeta` y las funciones `abstractmethod`, 
`abstractproperty`.

Funcionan así: si uno intenta instanciar de parte de una clase que tiene 
definido un `abstractmethod`(o `abstractproperty`) que no ha sido overrideado en una subclase,
se levanta la excepción `TypeError`.

```python
from abc import ABCMeta, abstractmethod, abstractproperty

class A(metaclass=ABCMeta):
	pass

a = A()	# se instancia sin problemas

class Figura(metaclass=ABCMeta):
	@abstractmethod
	def trasladar(self):
		pass

	@abstractproperty
	def perimetro(self):
		pass

# TypeError: Can't instantiate abstract class
# with abstractmethods trasladar, perimetro
f = Figura()

class Cuadrado(Figura):
	pass

# Lanza la misma excepcion que arriba
c = Cuadrado()

class Triangulo(Figura):
	def __init__(self, lado, centro):
		self.lado = lado	# Los suponemos equilateros
		self.centro = centro

	def trasladar(self, nuevo):
		self.centro = nuevo

	@property
	def perimetro(self):
		return 3*self.lado

# Success!
t = Triangulo(4, (0, 0))
```


### Ejercicio
Escriba código que defina a la metaclase `ABCMeta`, y también a `abstractmethod`, `abstractproperty` de modo que 
el programa escrito arriba produzca las mismas excepciones que si se importan desde `abc`.

####Tips
* Para levantar `TypeError` con un mensaje de error específico, puedes usar `raise TypeError(mensaje)`.
* Pueden ser útiles los built-ins `dir`, `getattr`.