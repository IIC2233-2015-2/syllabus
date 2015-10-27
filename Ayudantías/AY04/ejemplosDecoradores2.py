__author__ = 'Ivania Donoso'


def saludar_con_emocion(emocion, intensidad):
    def agregar_amor(f):
        print("Agregamos Amor")

        def nuevo_saludo(*args):
            print("Voy a saludar con amor")
            f(*args)
            print("{0} {1}".format(emocion, intensidad))
            print("")
        return nuevo_saludo
    print("Se ha construído el decorador")
    return agregar_amor


@saludar_con_emocion("Te quiero", "mucho")
def saludar(objeto, sujeto):
    print('Hola {0}, soy {1} tu nuevo perro'.format(sujeto, objeto))

print("Después de agregar amor al saludo")

print("Vamos a llamar a P-chan para que salude")

saludar('P-chan', 'Ivania')
print("Despúes de que saluda a Ivania")
saludar('P-chan', 'Pato')
print("Después de que saluda a Pato")
