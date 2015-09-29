#No editar este programa
from os import listdir

class Corrector:
    def __init__(self, nombre):
        self.nombre = nombre
        with open("Trabajos/" + self.nombre, "r") as archivo:
            lineas = archivo.readlines() 
            self.contenido = list(map(lambda o : o.strip(), lineas))

    def revisar_nombre(self):
        '''Retorna True su el formato del nombre
        del trabajo está bien, y retorna False si no'''
        partes = self.nombre.split(".")
        if not self.revisar_formato(partes[1]):
            return False
        rut = partes[0].split("_")[0]
        if not rut[:-2].isdigit():
            return False
        if not self.revisar_verificador(rut):
            return False
        return self.revisar_orden(partes[0])
        
    def revisar_formato(self, formato):
        #Revisa que el formato sea txt
        if "txt" in formato:
            return True
        return False

    def revisar_verificador(self, rut):
        #Revisa el codigo verificador del rut
        verificador = rut[-1]
        codigo = rut[:-2]
        lista = [int(i) for i in codigo]
        inv = lista[::-1]
        factores = []
        c = 2
        for i in inv:
            factores.append(c)
            c += 1
            if c > 7:
                c = 2
        valor = sum(map(lambda a, b : a * b, inv, factores))
        resto = valor % 11
        num = 11 - resto
        if num == 10:
            num = "k"
        elif num == 11:
            num = "0"
        else:
            num = str(num)
        if num != verificador:
            return False
        return True

    def revisar_orden(self, texto):
        #Revisa el formato rut_nombre_apellido
        p = texto.split("_")
        if len(p) != 3:
            return False
        with open("Lista.txt","r") as l:
            i = l.readlines()
            nombres = list(map(lambda o : o.strip().lower(), i))
        if "{} {}".format(p[1].lower(),p[2].lower()) in nombres:
            return True
        return False

    def get_palabras(self):
        #Cuenta las palabras del trabajo
        return sum(map(lambda l : l.count(" "), self.contenido))

    def get_descuento(self):
        #Calcula el descuento final del trabajo por incumplimiento de reglas
        d = 0
        if not self.revisar_nombre():
            d = 0.5
        if self.palabras < 500:
            d = 1
        return d

    def descontar(self):
        #Descuenta a la nota del trabajo el descuento calculado
        with open("Trabajos/" + self.nombre, "r") as archivo:
            lineas = archivo.readlines()
            nota = float(lineas[0].strip()) - self.descuento
            lineas[0] = "{}\n".format(nota)
        with open("Trabajos/" + self.nombre, "w") as archivo:
            for i in lineas:
                archivo.write(i)

    descuento = property(get_descuento)
    palabras = property(get_palabras)

if __name__ == "__main__":
    #listdir lista los nombres de los archivos en la carpeta dada
    for n in listdir("Trabajos"):
        t = Corrector(n)
        t.descontar()

