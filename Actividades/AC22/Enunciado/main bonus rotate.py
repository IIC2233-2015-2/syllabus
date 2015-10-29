# -*- coding: utf8 -*-
from zlib import compress, decompress, crc32


class InstaPUC:

    @staticmethod
    def getData(filename):
        signature = None
        ihdr = {}
        idat = bytearray()
        iend = None
        ########################################
        #                                      #
        # Completar método.                    #
        # Extraer la metadata de la imagen PNG.#
        #                                      #
        ########################################
        return signature, ihdr, decompress(idat), iend

    @staticmethod
    def bytes2matrix(ihdr, idat):
        matriz = []
        ########################################
        #                                      #
        # Completar método.                    #
        # Transformar arreglo de bytes a una   #
        # matriz de pixeles.                   #
        #                                      #
        ########################################
        return matriz

    @staticmethod
    def matrix2string(matriz):
    	"""
    	Este método transforma la matriz en un string de bytes.
    	"""
        out = b''
        for i in range(len(matriz)):
            out += (0).to_bytes(1, byteorder='big')
            for j in range(1, len(matriz[i])):
                for k in matriz[i][j]:
                    out += k.to_bytes(1, byteorder='big')
        return out

    @staticmethod
    def rotate(ihdr, matriz):
        salida = []
        ########################################
        #                                      #
        # Completar método.                    #
        # Girar la matriz de pixeles y         #
        # modificar la metadata.               #
        # OJO: No es transponer.               #
        #                                      #
        ########################################
        return ihdr, salida

    @staticmethod
    def grey(ihdr, matriz):
        salida = []
        ########################################
        #                                      #
        # Completar método.                    #
        # Cambiar cada pixel por el promedio   #
        # de las 3 componentes y modificar la  #
        # metadata.                            #
        #                                      #
        ########################################
        return ihdr, salida

    @staticmethod
    def writeImage(outFile, signature, ihdr, idat, iend):
        idat = compress(idat, 9)
        ########################################
        #                                      #
        # Completar método.                    #
        # Escribe un nuevo archivo PNG con la  #
        # información entregada.               #
        # TIP: No es necesario hacer varios    #
        # chunks de IDAT.                      #
        #                                      #
        ########################################
        print("Tu imagen ha sido transformada exitosamente!")


if __name__ == '__main__':

    imagefile = ''  # Mushroom.png o MickeyMouse.png

    firma, ihdr, data, end = InstaPUC.getData(imagefile)

    matriz = InstaPUC.bytes2matrix(ihdr, data)

    ihdr_gris, matriz_gris = InstaPUC.grey(ihdr, matriz)

    idat_gris = InstaPUC.matrix2string(matriz_gris)

    InstaPUC.writeImage(
        'image.png',
        firma,
        ihdr_gris,
        idat_gris,
        end)

"""
    # Descomentar si se realiza el bonus

    ihdr_gris_rotado, matriz_gris_rotada = InstaPUC.rotate(
        ihdr_gris, matriz_gris)

    idat_gris_rotado = InstaPUC.matrix2string(matriz_gris_rotada)

    InstaPUC.writeImage(
        'image.png',
        firma,
        ihdr_gris_rotado,
        idat_gris_rotado,
        end)
"""
