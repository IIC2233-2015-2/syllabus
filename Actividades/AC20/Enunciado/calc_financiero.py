__author__ = 'Iacopo'

from collections import namedtuple


def calcular_jub(ingreso, cotiza, edad, edad_j, esp_vida, fondo_elegido):

    """
    Calculo de monto de jubilacion, a partir de parametros.
    Esta funcion retorna un string con el formato: $Limite inferior - $Limite superior

    Keyword arguments:
    ingreso -- ingreso mensual imponible, en pesos.
    cotiza -- porcentaje de cotizacion (ej. poner 10, si es 10%).
    edad -- edad actual de la persona en agnos (la formula asume que la persona comienza a trabajar a esa edad).
    edad_j -- edad de jubilacion.
    esp_vida -- esperanza de vida de la persona.
    fondo_elegido -- Fondo en el cual se ahorrara (Recibe letras mayusculas desde la A hasta la E).

    Nota 1: Este calculo es una simplificacion del modelo real de AFP, no se alegre/entristezca por los
            numeros entregados, es muy probable que no se condigan con la realidad.
    Nota 2: Se omitieron acentos y otras letras, para evitar problemas de codificacion.
    """

    Fondo = namedtuple("Fondo", "rent desv")

    fondos = {"A": Fondo(0.053, 0.19), "B": Fondo(0.0522, 0.15), "C": Fondo(0.051, 0.12),
              "D": Fondo(0.049, 0.03), "E": Fondo(0.05, 0.01)}

    aporte = ingreso*cotiza/100

    m_trab = (edad_j - edad)*12
    m_jub = (esp_vida - edad_j)*12

    fondo_elegido = fondo_elegido.upper()

    def _calc(bound):
        delta = fondos[fondo_elegido].desv if bound == "upp" else -fondos[fondo_elegido].desv
        r_anual = fondos[fondo_elegido].rent*(1+delta)
        r_mensual = (1 + r_anual)**(1/12) - 1

        r_m_dep = r_mensual - (1.0148**(1/12) - 1)
        r_m_ret = r_mensual - (1.0125**(1/12) - 1)

        try:

            monto_jub = ((aporte/r_m_dep)*(1-(1/((1+r_m_dep)**m_trab)))*((1+r_m_dep)**(m_trab+1)))\
                        *(((1+r_m_ret)/r_m_ret)*(1-(1/((1+r_m_ret)**m_jub))))**-1

        except ZeroDivisionError as e:
            return "Error datos"

        except Exception as e:
            return "Error"

        return int(monto_jub)

    return "${} - ${}".format(_calc("low"), _calc("upp"))