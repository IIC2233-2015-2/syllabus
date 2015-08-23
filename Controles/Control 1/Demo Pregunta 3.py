# Basado en una respuesta de StackOverflow
# http://stackoverflow.com/a/8959269/3281097


class AlgunaClase:

    def __init__(self):
        self.foo = 'Soy un atributo de la instancia llamado foo'
        self.foo_list = []

    bar = 'Soy un atributo de la clase llamado bar'
    bar_list = []

if __name__ == '__main__':
    # Creamos una instancia de la clase ...
    ac1 = AlgunaClase()
    # ... y le damos un valor a una variable de la instancia
    ac1.foo_list.append('Entrando a foo_list de la instancia ac1')
    print(ac1.foo_list)

    # Creamos otra instancia de la misma clase ...
    ac2 = AlgunaClase()
    # ... y ahora le damos otro valor a una variable de la instancia
    ac2.foo_list.append('Entrando a foo_list de la instancia ac2')
    print(ac2.foo_list)

    # Entramos a la variable de la clase desde las distintas instancia
    ac1.bar_list.append('Entrando bar_list desde ac1')
    ac2.bar_list.append('Entrando bar_list desde ac2')
    print(ac1.bar_list)
    print(ac2.bar_list)

    # ¿Seran iguales las listas?
    print(ac1.bar_list == ac2.bar_list)
    # Vemos que SI son iguales :) ...

    # ... y es mas ...
    print(ac1.bar_list is ac2.bar_list)
    # ... son la misma lista
