# Control 4

### Forma 1
**1) Cree dinámicamente usando type la clase Rectángulo con los atributos ladoA y ladoB con valor 1 por defecto**

###### Basado en el material de [**Metaclases**](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/04_METACLASES/MetaClases.html)

```python
Rectangulo = type("Rectangulo",(), {"ladoA":1,"ladoB":1})
```

**2) Escriba lo que se imprime en consola con el siguiente programa**

```python
def mi_dec(f):
    def interno(*args, **kwargs):
        print("Los argumentos son: {0} {1}\n".format(*args,**kwargs))
        return f(*args,**kwargs)
    return interno

@mi_dec
def f_1(x, y=1):
    return (x + 1) ** y

def f_2(x, y):
    return x * y

print(f_1(1,2))
print(f_2(2,2))
```

###### Basado en el material de [**Metaclases**](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/04_METACLASES/MetaClases.html)

```python
Los argumentos son: 1 2

4
4
```

### Forma 2
**1) Cree dinámicamente usando type la clase Punto con los atributos x e y con valor 0 por defecto**

###### Basado en el material de [**Metaclases**](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/04_METACLASES/MetaClases.html)

```python
Punto = type("Punto",(), {"x":0,"y":0})
```

**2) Escriba lo que se imprime en consola con el siguiente programa**

```python
def mi_dec(f):
    def interno(*args, **kwargs):
        print("Los argumentos son: {0} {1}\n".format(*args,**kwargs))
        return f(*args,**kwargs)
    return interno

def f_1(y, x=1):
    return x - y

@mi_dec
def f_2(x, y):
    return (x + 1) * y

print(f_1(6,7))
print(f_2(2,2))
```

###### Basado en el material de [**Metaclases**](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/04_METACLASES/MetaClases.html)

```python
1
Los argumentos son: 2 2

6
```

### Forma 3
**1) Cree dinámicamente usando type la clase Control con los atributos nombre y nota con valores "" y 1 por defecto**

###### Basado en el material de [**Metaclases**](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/04_METACLASES/MetaClases.html)

```python
Control = type("Control",(), {"nombre":"","nota":1})
```

**2) Escriba lo que se imprime en consola con el siguiente programa**

```python
def mi_dec(f):
    def interno(*args, **kwargs):
        print("Los argumentos son: {0} {1}\n".format(*args,**kwargs))
        return f(*args,**kwargs)
    return interno

def f_1(y, x=1):
    return x - y

@mi_dec
def f_2(x, y):
    return (x + 1) * y

print(f_1(6,7))
print(f_2(2,2))
```

###### Basado en el material de [**Metaclases**](https://github.com/IIC2233-2015-2/syllabus/blob/master/Material%20de%20clases/04_METACLASES/MetaClases.html)

```python
1
Los argumentos son: 2 2

6
```