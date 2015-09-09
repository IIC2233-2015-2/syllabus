__author__ = 'mabucchi'


def tipar(*tipos):
    # Esta función generará un decorador que forzará que los argumentos de la función decorada
    # sean idénticos a <tipos>.

    def decorator(func):
        # Se define el decorador para la función

        def inner(*args):
            # Se define la función decorada. Esta deberá analizar los tipos de los argumentos
            # recibidos.

            # Para esto usamos programación funcional para transformar <args> a una tupla
            # con los tipos de los argumentos.
            # ej: (2, 2, 'hola') -> (int, int, str)
            _types = tuple(map(type, args))

            # Si estos tipos llegasen a ser distintos a los entregados inicialmente, entonces no
            # se está cumpliendo con el tipificado forzado. En este caso
            # imprimimos el error.
            if _types != tipos:
                print(
                    'Error en los tipos! se esperaba {} pero se recibió {}'.format(tipos, _types))

            # En caso contrario, se tiene que <_types> es idéntico a <tipos>, por lo tanto estamos en
            # libertad de ejecutar la función original con los argumentos
            # entregados
            else:
                return func(*args)

        # retornamos la función decorada
        return inner

    # retornamos el decorador generado para <tipos>
    return decorator


class Overload:

    '''Esta clase decoradora permite la sobredefinición de métodos. Para esto, guardará
    todas las sobrecargas junto con los tipos de argumentos que le corresponden en un
    diccionario dentro de esta clase.


    ej:

    @Overload                               Guarda una versión del método <method>
    def method(self):                       asociada a 0 argumentos
        pass

    @method.overload(int, str)              Guarda una versión del método <method>
    def method(self, a, b):                 asociada a 2 argumentos de tipo
        pass                                (<int>, <str>)

    '''

    def __init__(self, func):
        # Creamos el diccionario donde se guardarán las funciones.
        # Guardamos inicialmente la función que está asociada a 0 argumentos,
        # es por esto que se guarda con la llave de una tupla vacía

        self._funcs = {tuple(): func}

    def overload(self, *tipos):

        # Este método deberá generar un decorador que agregue la función
        # decorada al dicionario <_funcs> definido en el __init__ en
        # la llave correspondiente a <tipos>

        def func_adder(func):
            # Este decorador, al recibir una función la guardará en el diccionario
            # con la llave <tipos>.

            # Un ejemplo siguiendo el caso planteado anteriormente:
            #
            #
            #
            # @method.overload(int, str)            Esto causará que el método <method> se
            # def method(self, a, b):               guarde en <self._funcs> con la llave (int, str)
            #     pass
            #                                       self._funcs[(int, str)] = method
            #
            #

            self._funcs[tipos] = func

            # Finalmente, al igual que con los otros decoradores, debemos retornar
            # la función decorada. Sin embargo, a diferencia de los decoradores que
            # habían visto previamente, la función decorada es la instancia de la clase
            # <Overload>, pues las funciones se están guardando allí. Por esto es que
            # retornamos <self>.

            return self

        # Retornamos el decorador generado.
        return func_adder

    def __call__(self, *args):

        # Este método se llamará cuando alguien intenta ejecutar el método decorado.
        # Es por esto que, al recibir los argumentos, debemos buscar en el diccionario
        # la función que esté asociada a los tipos de <args> y ejectuar solo
        # esa.

        # EJ:
        # si alguien llegase a llamar method(2, 'hola') se debería buscar en <self._funcs>
        # la función asociada a los tipos (int, str), es decir
        # <self._funcs[(int, str)]>

        # IMPORTANTE: recordar que en el caso anterior, los argumentos recibidos no serían
        # (2, 'hola'), pues recuerden que los métodos reciben como primer argumento la referencia
        # a la instancia de la clase, es decir <args> sería (obj_self, 2, 'hola').
        #
        # No confundan este <obj_self> con el <self> que viene en el método call. Este
        # último está asociado a la clase <Overload> mientras que el que viene en <args>
        # está asociado a la clase del método decorado.

        # Debido a esto último, mediante programación funcional se obtienen los tipos de los
        # argumentos SIN considerar el self, es decir <args[1:]>

        # ej args = (self, 2, 'hola') -> tipos = (int, str)
        tipos = tuple(map(type, args[1:]))

        # Por último, se revisa si los tipos existen como llave en <self._funcs>. De ser así se
        # ejecuta la función asociada. En caso contrario se imprime un mensaje
        # de error

        if tipos in self._funcs:
            return self._funcs[tipos](*args)
        print('No hay un overload con esos tipos!')

    def __get__(self, obj, cls):
        def caller(*args, **kwargs):
            return self(obj, *args, **kwargs)
        return caller
