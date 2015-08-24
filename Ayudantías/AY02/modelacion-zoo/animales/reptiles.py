from . import animal


class Reptil(animal.Animal):
    pass


class Serpiente(Reptil):

    @property
    def sonido(self):
        return 'ssssss'


class Python(Serpiente):
    pass
