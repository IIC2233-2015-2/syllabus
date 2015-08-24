class Animal:
    id_counter = 0

    def __init__(self, nombre, fecha_nacimiento):
        Animal.id_counter += 1
        self.id = Animal.id_counter
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

    @property
    def sonido(self):
        pass
