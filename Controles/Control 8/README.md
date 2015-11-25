# Control 8

###### Basado en el material de [Serialización](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/11-IO_SERIALIZACION/10-I_O.html)

### Forma 1
**De un ejemplo útil de personalizar la serialización en un clase de Python.**

Una aplicación práctica de los métodos \_\_getstate\_\_ y \_\_setstate\_\_, es cuando necesitamos serializar un objeto que contiene un atributo que perderá sentido en la serialización. Por ejemplo, si un objeto contiene una conexión a una base de datos, al serializar el objeto, naturalmente la conexión en el objeto serializado se perderá, de hecho pickle genera un error cuando tratamos de serializar este tipo de objetos. Una solución es usar los métodos \_\_getstate\_\_ y \_\_setstate\_\_. Primero, usamos \_\_getstate\_\_ para eliminar la conexión a la base de datos del objeto que se va a serializar (borramos la conexión de la copia del diccionario), y cuando deserializamos el objeto de vuelta, lo volvemos a conectar manualmente a la base de datos dentro del método \_\_setstate\_\_.


### Forma 2
**Explique para qué sirve implemetar el método \_\_getstate\_\_ en una clase cualquiera de Python.**

Cuando pickle trata de serializar un objeto, lo que trata de hacer es es guardar el atributo \_\_dict\_\_ del objeto. Lo interesante es que antes de chequear el atributo \_\_dict\_\_, pickle revisa si es que existe un método llamado \_\_getstate\_\_, si existe, serializará lo que retorna el método \_\_getstate\_\_ en vez del diccionario (\_\_dict\_\_) del objeto.


### Forma 3
**Explique para qué sirve implemetar el método \_\_setstate\_\_ en una clase cualquiera de Python.**

El método \_\_setstate\_\_, se ejecutará cada vez que llamamos a load o loads, para setear el estado actual del objeto recién deserializado. El método \_\_setstate\_\_ recibe como argumento el estado del objeto que fue serializado (el retornado por \_\_getstate\_\_) y debe setear el estado en el cual queremos que el objeto deserializado quede, seteando self.\_\_dict\_\_.