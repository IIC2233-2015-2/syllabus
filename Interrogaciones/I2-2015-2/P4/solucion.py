import json


class Parser:

    @staticmethod
    def parsear(input_file, output_file):
        """Puntaje:
            (3 pts) Apertura del archivo:
                    (2 pts) solo por abrirlo
                    (1 pts) ir leyendolo por linea en vez de usar json.load
                        Se desconto explicitamente por esto porque
                        si se carga con load, se tendra un diccionario
                        que NO TIENE ORDEN.
                        Por lo tanto, no se podria escribir el output
                        respetando el orden del input

            (2 pts) Control de flujo:
                        Programa con estructura:
                            - Leer archivo de input
                            - Parsear archivo
                            - Si el parseo es correcto, escribir archivo de output
                            - Si no, imprimir error

            (5 pts) Lectura del archivo:
                        Determinar EN FORMA GENERAL, cuales son los labels
                        que van y como van.

            (5 pts) Escritura de output:
                        Escribir correctamente el output, con tags (<>, </>)
                        y tabs que correspondan al nivel de profundidad

            (1 pt ) EXTRA: conseguir nombres de archivos con lineEdit.text()
        """

        with open(input_file, "r") as file:
            try:
                content = (c for c in file.readlines())
            except Exception as err:
                print("Hubo un error! {}".format(err))
                return

        parsed = ""

        # profundidad de "tabs"
        depth = 0

        assert next(content) == "{\n"

        # Primera parte: conseguir atributos de "catalog"
        name = next(content).strip().split(": ")[0][1:-1]
        parsed += "<{} ".format(name)

        while True:
            line = next(content)
            keyval, empty = line.strip().split(",")
            key, value = keyval.split(": ")
            parsed += "{}=\"{}\"".format(key[1:-1], value)
            if empty is "":
                parsed += ", "
            elif "{" in empty:
                parsed += ">\n"
                break
        # Hasta aqui, lleva:
        # "<catalog field="256", id="434">\n"

        # Segunda parte: escribir el resto
        while True:
            line = next(content)
            print(line)
            if line[-2] is not ",":
                break

            keyval, empty = line.strip().split(",")
            key, value = keyval.split(": ")

            if empty is "":
                parsed += "\t<{0}>{1}</{0}>\n".format(key[1:-1], value)

            else:
                break

        # Hasta aqui, lleva:
        # <catalog field="256", id="434">
        #   <filename>"00000401.dat"</filename>
        #   <band>"k"</band>

        # Tercera parte: parsear diccionario y listas
        # Dado que muchos alumnos hicieron funciones recursivas
        # importando json, para esta parte de la solucion
        # mostrare como se aplicaria esta idea.
        # Problemas:
        # - Salida no respeta el orden en que esta la entrada
        # - Todos los diccionarios estaran en varias lineas
        # - Por ejemplo, se mostraria:
        #       <mjd>
        #           0.0000
        #       </mjd>
        #       <m>
        #           14.152
        #       </m>
        #       <e>
        #           0.033
        #       </e>
        # No obstante lo anterior, NO se desconto puntaje
        # (salvo 1 punto por usar json.load)
        # Si se implementa la funcion recursivamente
        # considerando profundidad de tabs, y correria bien.
        import json


        newtag = line.strip().split(':')[0]

        parsed += '\t<{}>\n'.format(newtag[1:-1])

        while True:
            measure = next(content).strip()
            if ']' in measure:
                break
            if measure[-1] == ',':
                dic = json.loads(measure[0:-1])
            else:
                dic = json.loads(measure)


            parsed += '\t\t<_{}>\n\t\t\t'.format(newtag[1:-1])
            for key, value in dic.items():
                parsed += '<{0}>{1}</{0}> '.format(key, value)
            parsed += '\n\t\t</_{}>\n'.format(newtag[1:-1])


        parsed += '\t</{}>\n'.format(newtag[1:-1])


        # Finalmente, cerrar el catalog
        parsed += "</{}>".format(name)

        print(parsed)

        if Parser.verificar_parseo(parsed):
            with open(output_file, "w") as file:
                file.write(parsed)

        else:
            print("Hubo un error! Verificacion de parseo incorrecta.")

    @staticmethod
    def _parse(elemento, tabs=0):
        pass

    @staticmethod
    def verificar_parseo(parsed):
        """La funcion verificar_parseo revisa que:
            - Cada vez que se abra un tag (<), este se cierre sin que se haya abierto otro tag.
            - Solo se cierren tags (>) que han sido abiertos
            - Si se "abre una key" (por ejemplo, <m>), esta se cierre despues (</m>)
        Puntaje:
            (3 pts) Verifica correctamente la apertura y cierre de tags (<>)
            (2 pts) Verifica que si se abre una key, esta se cierre.
        NOTA:
            Si el alumno interpreto de forma distinta el enunciado,
            y disenio un test para probar a una funcion verificar_parseo existente,
            se asignaron como maximo 3 de 5 puntos.
        """

        import collections

        # este diccionario guarda en key,
        # una palabra que fue abierta, como
        # "measure" o "mjd".
        # Se suma 1 al value cuando se abrio la palabra (<mjd>)
        # y se resta 1 cuando se cierra (</mjd>)
        d = collections.defaultdict(lambda: 0)

        text = ""               # guarda el texto a abrir o cerrar
        getting_text = False    # True si se esta ABRIENDO algo entre tags <mj...
        closing_text = False    # True si se esta CERRANDO algo entre tags </mj...
        in_string = False       # True si se esta en un string: <m>"stri...
        counter = 0             # suma 1 si hay '<', resta si hay '>'

        for c in parsed:
            if c is "\"":
                in_string = not in_string

            # esto es para evitar que se consideren
            # los "<" y ">" que esten en un string,
            # por ejemplo, si en una parte dijera:
            # <mjd>"este>es<un>string"</mjd>
            # NO SE DESCONTO PUNTAJE por no incluir esto
            elif not in_string:
                if c is "<":
                    counter += 1
                    if counter > 1:
                        print("Se abrio un tag cuando otro antes no se habia cerrado:\n"
                              "\tPor ejemplo, se encontro una parte con:\n"
                              "\t\t<mea<")
                        return False
                    # entra en modo conseguir texto
                    getting_text = True

                elif getting_text:
                    if c is "/":
                        if text:
                            # No se desconto puntaje
                            # por no incluir este caso
                            print("Hay algo extranio:\n"
                                  "\tPor ejemplo, se encontro una parte con:\n"
                                  "\t\t<mea/")
                            return False
                        # modo cerrar una key
                        closing_text = True
                        getting_text = False
                    elif c is " ":
                        # esto evita que se agregue
                        # catalog field="256", id="434"
                        # como key al diccionario
                        # y permite que solo se considere "catalog"
                        getting_text = False
                    elif c != ">":
                        if c is "\n":
                            return False
                        text += c

                elif closing_text and c != ">":
                    if c is "\n":
                        return False
                    text += c

                if c is ">":
                    counter -= 1
                    if counter < 0:
                        print("Se cerro un tag que no se habia abierto.\n"
                              "\tPor ejemplo, se encontro una parte con:\n"
                              "\t\t<measure> algo>")
                        return False

                    if closing_text:
                        d[text] -= 1
                        if d[text] < 0:
                            return False
                        closing_text = False

                    else:
                        d[text] += 1
                        getting_text = False

                    text = ""

        # Revisa que toda key se abrio
        # la misma cantidad de veces que fue cerrada
        for value in d.values():
            if value is not 0:
                print(dict(d))
                return False

        # si pasa todas las pruebas,
        return True


if __name__ == "__main__":
    Parser.parsear("input.txt", "output.txt")
