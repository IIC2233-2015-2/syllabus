
def abstractmethod(funcion):
    funcion.__isabstractmethod__ = True
    return funcion


class abstractproperty(property):
    __isabstractmethod__ = True


class ABCMeta(type):
    def __call__(cls, *args, **kw):
        absmethods = [
            attr for attr in dir(cls)
            if getattr(
                getattr(cls, attr),
                '__isabstractmethod__',
                False
            )
        ]
        
        if not absmethods:
            return super().__call__(*args, **kw)

        else:
            raise TypeError(
                "Can't instantiate abstract class {} "
                "with abstract methods {}".format(
                    cls.__name__,
                    ", ".join(absmethods)
                )
            )


if __name__ == "__main__":
    class A(metaclass=ABCMeta):
        pass
    a = A()  # se instancia sin problemas
    print(a)

    class Figura(metaclass=ABCMeta):
        @abstractmethod
        def trasladar(self):
            pass

        @abstractproperty
        def perimetro(self):
            pass

    # f = Figura()  # tira error
    
    class Cuadrado(Figura):
        pass

    # c = Cuadrado()  # tira error

    class Triangulo(Figura):
        def __init__(self, centro, lado):
            self.lado = lado
            self.centro = centro

        def trasladar(self, nuevo):
            self.centro = nuevo

        @property
        def perimetro(self):
            return 3*self.lado

    t = Triangulo((0, 0), 3)
