#!/usr/local/bin python3
# -*- encoding: utf-8 -*-
from PyQt4 import QtCore, QtGui, uic
import random as rnd
import os
import time
from collections import deque

grilla_simulacion_ui = uic.loadUiType(
    os.path.join(os.path.dirname(__file__), "grilla_simulacion.ui")
)


class GrillaSimulacion(*grilla_simulacion_ui):

    def __init__(self, app, rows=20, cols=20):
        super().__init__()

        self.rows = rows
        self.cols = cols

        dim = 800 // max(rows, cols)

        self.width = cols * dim
        self.height = rows * dim

        self.size = QtCore.QSize(dim, dim)
        self.img_size = QtCore.QSize(dim // 1.2, dim // 1.2)
        self.setupUi(self)
        self._setup_labels()
        self.app = app

        self.__act_queue = deque()
        self.__curr_act = list()
        self._create_thread()

        self.simulationGrid.setSpacing(0)

        dims = (10, 10, self.width - 20, self.height - 20)

        self.gridLayoutWidget.setGeometry(*dims)
        self.setGeometry(50, 50, self.width, self.height)

    @property
    def tiempo_intervalo(self):
        return self.thread.interval

    @tiempo_intervalo.setter
    def tiempo_intervalo(self, value):
        self.thread.interval = value

    def _create_thread(self):
        self.thread = Worker(self.__act_queue, 0)
        self.connect(self.thread, QtCore.SIGNAL("do"), self.__do)
        self.thread.start()

    def _setup_labels(self):
        for x in range(1, self.rows + 1):
            for y in range(1, self.cols + 1):
                label = QtGui.QLabel()
                label.setAlignment(QtCore.Qt.AlignCenter)
                self.simulationGrid.addWidget(label, x, y)

    def agregar_ambulancia(self, x, y, theta=0, reflection=False):
        self._agregar_imagen("Ambulance-64.png", x, y, theta, reflection)

    def agregar_enfermo(self, x, y):
        self._agregar_imagen("Being Sick-64.png", x, y)

    def agregar_auto(self, x, y, theta=0, reflection=False):
        nuevo_auto = rnd.choice([
            self.agregar_convertible,
            self.agregar_pickup,
            self.agregar_sedan
        ])
        nuevo_auto(x, y, theta, reflection)

    def agregar_convertible(self, x, y, theta=0, reflection=False):
        self._agregar_imagen("Convertible-64.png", x, y, theta, reflection)

    def agregar_pickup(self, x, y, theta=0, reflection=False):
        self._agregar_imagen("Pickup-64.png", x, y, theta, reflection)

    def agregar_sedan(self, x, y, theta=0, reflection=False):
        self._agregar_imagen("Sedan-64.png", x, y, theta, reflection)

    def agregar_cuartel_bomberos(self, x, y):
        self._agregar_imagen("Fire Station-64.png", x, y)

    def agregar_carro_bomba(self, x, y, theta=0, reflection=False):
        self._agregar_imagen("Fire Truck-64.png", x, y, theta, reflection)

    def agregar_incendio(self, x, y):
        self._agregar_imagen("Fires-64.png", x, y)

    def agregar_casa(self, x, y):
        self._agregar_imagen("Home-64.png", x, y)

    def agregar_hospital(self, x, y):
        self._agregar_imagen("Hospital 3-64.png", x, y)

    def agregar_robo(self, x, y):
        self._agregar_imagen("Pickpocket-64.png", x, y)

    def agregar_comisaria(self, x, y):
        self._agregar_imagen("Police Station Filled-64.png", x, y)

    def agregar_patrulla(self, x, y, theta=0, reflection=False):
        self._agregar_imagen("Police-64.png", x, y, theta, reflection)

    def agregar_taxi(self, x, y, theta=0, reflection=False):
        self._agregar_imagen("Taxi-64.png", x, y, theta, reflection)

    def agregar_calle(self, x, y):
        if x > self.rows or y > self.cols:
            print("[ERROR] Coordenadas ({}, {})"
                  " fuera de las dimensiones de la grilla!".format(x, y))
            return
        self.__curr_act.append(("street", x, y))

    def _agregar_calle(self, x, y):
        label = self.simulationGrid.itemAtPosition(x, y).widget()
        label.setStyleSheet("background-color: #666666;")

    def __agregar_imagen(self, filename, x, y, theta=0, reflection=False):
        path = os.path.join(os.path.dirname(__file__), "assets", filename)
        pixmap = QtGui.QPixmap(path)
        label = self.simulationGrid.itemAtPosition(x, y).widget()
        pixmap = pixmap.scaled(self.img_size, QtCore.Qt.KeepAspectRatio)

        if theta != 0:
            pixmap = pixmap.transformed(QtGui.QTransform().rotate(theta))

        if reflection:
            pixmap = pixmap.transformed(QtGui.QTransform().scale(-1, 1))

        label.setPixmap(pixmap)

    def _agregar_imagen(self, filename, x, y, *args):
        if x > self.rows or y > self.cols:
            print("[ERROR] Coordenadas ({}, {})"
                  " fuera de las dimensiones de la grilla!".format(x, y))
            return
        self.__curr_act.append(("add", filename, x, y) + args)

    def quitar_imagen(self, x, y, *args):
        if x > self.rows or y > self.cols:
            print("[ERROR] Coordenadas ({}, {})"
                  " fuera de las dimensiones de la grilla!".format(x, y))
            return
        self.__curr_act.append(("remove", x, y) + args)

    def __quitar_imagen(self, x, y):
        label = self.simulationGrid.itemAtPosition(x, y).widget()
        label.clear()

    def actualizar(self):
        if len(self.__curr_act) == 0:
            print("[NOTIFICACION] Se busca actualizar sin "
                  "haber realizado cambios!")
        else:
            self.__act_queue.append(self.__curr_act)
            self.__curr_act = list()

    def __do(self, insts):
        for inst, *args in insts:
            if inst == "add":
                self.__agregar_imagen(*args)
            elif inst == "remove":
                self.__quitar_imagen(*args)
            else:
                self._agregar_calle(*args)

        self.app.processEvents()


class Worker(QtCore.QThread):

    def __init__(self, queue, interval):
        super().__init__()
        self.queue = queue
        self.interval = interval

    def __del__(self):
        self.exiting = True
        self.wait()

    def run(self):
        while True:
            if len(self.queue) > 0:
                to_do = self.queue.popleft()
                self.emit(QtCore.SIGNAL("do"), to_do)
                time.sleep(self.interval)
            else:
                time.sleep(0.01)
