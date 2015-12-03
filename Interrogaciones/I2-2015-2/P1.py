import threading
import random
from collections import deque
import time

# Se tienen las funciones fs y fv ya implementadas
# Se asume que se tiene una función, llamémosla "f_semaforos", que dada la lista de tiempos entre dos nodos, retorna
# una lista de los semáforos entre esos mismos dos nodos
# Se asume también una lista con todos los semáforos

def fs(nodo_i, nodo_j):
    pass


def fv(tiempo):
    pass


def f_semaforos(lista_tiempos_medios):
    pass


class Simulacion:
    def __init__(self, matriz, semaforos):
        self.matriz = matriz
        self.autos = []
        self.semaforos = semaforos
        self.tiempo = 0

    def run(self):
        for semaforo
            while self.tiempo <= (24 * 60 ):  # Cantidad de minutos en un día.
                if self.tiempo % 60 == 0:
                    numero_autos = fv(self.tiempo)
                    if numero_autos < len(self.autos):
                        for i in range(len(self.autos) - numero_autos):
                            self.autos.append(Auto(self.tiempo))


                    elif numero_autos > len(self.autos):
                        autos_ida = [auto for auto in self.autos if auto.retorno == False]
                        for i in range(len(autos_ida)):
                            auto_elegido = random.choice(autos_ida)
                            auto_elegido.retorno = True
                            autos_ida.remove(auto_elegido)


class Auto(threading.Thread):
    def __init__(self, tiempo, sim=Simulacion):
        super().__init__()
        self.sim = sim
        while True:
            self.origen = random.randint(0, self.sim.matriz)
            self.destino = random.randint(0, self.sim.matriz)
            try:
                div = 1 / self.sim.matriz[self.inicio][self.destino]
                #Si la matriz devuelve cero es que los nodos no están conectados, y tirará error
                break
            except ZeroDivisionError:
                pass
        self.tiempo = tiempo
        self.retorno = False  # Indica si el auto va de vuelta o no
        self.rojo_verde, self.tiempos_medios = fs(self.origen, self.destino)
        self.semaforos = f_semaforos(self.tiempos_medios)
        self.duracion_viaje = len(self.semaforos)#Cuántos semaforos hay en el camino

    def run(self):
        num_semaforo = 0
        while True:
            if num_semaforo == self.duracion_viaje and self.retorno == False:
                time.sleep(self.tiempos_medios[0])
                print("Viaje terminado. {0}-[1} . Hora llegada: {2}".format(self.origen, self.destino, self.sim.tiempo))
                break
            time.sleep(self.tiempos_medios[num_semaforo])
            self.tiempos_medios.pop(0)
            semaforo_actual=semaforos[0]
            if semaforo_actual.estado == "rojo":
                semaforo_actual.cola.append(self)
                with self.semaforo_actual.lock:
                    pass



#Se asume que los semaforos ya vienen todos creados
class Semaforo(threading.Thread):
    def __init__(self, id):
        super().__init__()
        self.cola = deque()
        self.id = id
        self.lock = threading.Lock()
        self.estado = "verde"
        self.duracion = fs()[0][self]  #Cuánto se demora en cambiar de color

    def run(self):
        time.sleep(self.duracion)
        if self.estado == "verde":
            self.estado = "rojo"
        else:
            self.estado = "verde"


if __name__ == '__main__':
    matriz=[]
    semaforos=[]
    #Se asume que estas dos variables ya vienen implementadas de forma correcta.
    simulacion = Simulacion(matriz, semaforos)
    simulacion.run()






