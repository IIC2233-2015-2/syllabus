# Control 6

### Forma 1
Explique de que forma se puede sincronizar un recurso compartido en la modalidad Productor-Consumidor

###### Basado en el material de [Threading-Sincronizacion](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/08_THREADING/02_Sincronizacion.html)

R1:mediante el uso de locks que aseguren que el acceso al recurso pueda ser solo por un thread a la vez.

R2: Utilizando los métodos acquire() y release() antes y después de utilizar el recurso compartido respectivamente. Con ellos se asegura (bloquea) la ejecución de los demás threads mientras se usa el recurso.

### Forma 2
Explique como se podría implementar una clase cuyas instancias correspondan a listas que controlan el acceso para ser modificadas

###### Basado en el material de [Threading-Sincronizacion](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/08_THREADING/02_Sincronizacion.html)

Creando una clase que hereda de lista y agregando como atributo threading.Lock() en la instancia.Luego, se hace el bloqueo llamando este atributo al agregar o sacar elementos de la lista.

### Forma 3
Explique en qué casos conviene que un lock pertenezca a la clase y en qué casos conviene que pertenezca a la instancia. De un ejemplo de cada situación

###### Basado en el material de [Threading-Sincronizacion](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/08_THREADING/02_Sincronizacion.html) y en una respuesta del profesor Christian Pieringer.

Depende de la modelación y lo que se esté buscando. Si se quiere crear objetos threading-safe a nivel atributos o variables de instancia, como por ejemplo un deque que trabaje con concurrencia, los locks deben estar en la instancia puesto que podríamos querer otras deque threading-safe pero independientes de la anterior.
Cuando el lock pertenece a la clase, el lock es estático y cumple con hacer al objeto threading-safe a nivel datos estáticos. Un ejemplo es el modelo de productor-consumidor para un mismo recurso.

