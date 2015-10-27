from . import animal


class Mamifero(animal.Animal):
    pass


class Leon(Mamifero):

    @property
    def sonido(self):
        return 'raaarww!'


class Jirafa(Mamifero):

    @property
    def sonido(self):
        return ''  # :(
