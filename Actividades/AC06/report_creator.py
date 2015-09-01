"""
Generador de datos aleatorios
"""

from random import choice
import itertools


def generate(ammount):
    """
    Genera un archivo con datos aleatorios.
    :param n: Numero de datos aleatorios a generar.
    """

    anos = [2013, 2013, 2013, 2013, 2014]

    meses = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio',
             'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')

    dias = ('lunes', 'martes', 'miercoles',
            'jueves', 'viernes', 'sabado', 'domingo')

    colores = ('amarillo', 'azul', 'naranja', 'rojo', 'verde')

    horas = ['{:02d}-{:02d}'.format(i, i+1) for i in range(24)]

    motivos_alta = (
        'Retiro sin atencion',
        'Alta administrativa',
        'Alta por defuncion',
        'Alta solicitada por el paciente',
        'Alta por transferencia interna - Hospitalizacion',
    )

    with open("Reporte.txt", "w") as file:
        for _ in itertools.repeat(None, ammount):
            file.write("{}\t{}\t{}\t{}\t{}\t{}\n".format(
                choice(anos), choice(meses), choice(dias),
                choice(colores), choice(horas), choice(motivos_alta)
            ))


if __name__ == '__main__':
    generate(10000)
