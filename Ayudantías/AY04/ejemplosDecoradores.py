__author__ = 'Ivania Donoso'

# Las funciones son objetos, se pueden pasar como parámetros y recibir
# como resultados


# def foobar(funcion_original):
# print("estoy creando una función")
#
#     def nueva_function():
#         print("Soy la nueva función que no puede sumar")
#
#     print(funcion_original(1, 2))
#
#     return nueva_function
#
#
# def sumar(a, b):
#     return a + b
#
# funcion = foobar(sumar)
# funcion()
# print(sumar(1, 4))


def verbose(funcion_original):
    def new_function(*args, **kwargs):
        print("Entrando ", funcion_original.__name__)
        funcion_original(*args, **kwargs)
        print("Saliendo  ", funcion_original.__name__)

    return new_function


def widget_func():
    print("Soy el widget")

talkative_widget_func = verbose(widget_func)
talkative_widget_func()

# También los podemos guardar con el mismo nombre que la función original
# widget_func = verbose(widget_func)
# widget_func()

# Podemos usar "sugar syntax"
# @verbose
