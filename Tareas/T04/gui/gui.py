#!/usr/local/bin python3
# -*- encoding: utf-8 -*-
from PyQt4 import QtCore, QtGui, uic
import random as rnd
import os
import time

grilla_simulacion_ui = uic.loadUiType(
    os.path.join(os.path.dirname(__file__), "grilla_simulacion.ui")
)


class GrillaSimulacion(*grilla_simulacion_ui):
    def __init__(self, app, rows=20, cols=20):
        super().__init__()
        self.setupUi(self)
        self.setup_labels(cols, rows)

        self.app = app
        self.tiempo_intervalo = 0

    def setup_labels(self, rows, cols):
        for y in range(1, rows + 1):
            for x in range(1, cols + 1):
                self.simulationGrid.addWidget(QtGui.QLabel(), y, x)

    def agregar_ambulancia(self, y, x, theta, reflection):
        self.agregar_imagen("Ambulance-64.png", x, y, theta, reflection)

    def agregar_enfermo(self, y, x):
        self.agregar_imagen("Being Sick-64.png", x, y)

    def agregar_auto(self, y, x, theta, reflection):
        nuevo_auto = rnd.choice([
            self.agregar_convertible,
            self.agregar_pickup,
            self.agregar_sedan
        ])
        nuevo_auto(x, y, theta, reflection)

    def agregar_convertible(self, y, x, theta, reflection):
        self.agregar_imagen("Convertible-64.png", x, y, theta, reflection)

    def agregar_pickup(self, y, x, theta, reflection):
        self.agregar_imagen("Pickup-64.png", x, y, theta, reflection)

    def agregar_sedan(self, y, x, theta, reflection):
        self.agregar_imagen("Sedan-64.png", x, y, theta, reflection)

    def agregar_cuartel_bomberos(self, y, x):
        self.agregar_imagen("Fire Station-64.png", x, y)

    def agregar_carro_bomba(self, y, x, theta, reflection):
        self.agregar_imagen("Fire Truck-64.png", x, y, theta, reflection)

    def agregar_incendio(self, y, x):
        self.agregar_imagen("Fires-64.png", x, y)

    def agregar_casa(self, y, x):
        self.agregar_imagen("Home-64.png", x, y)

    def agregar_hospital(self, y, x):
        self.agregar_imagen("Hospital 3-64.png", x, y)

    def agregar_robo(self, y, x):
        self.agregar_imagen("Pickpocket-64.png", x, y)

    def agregar_comisaria(self, y, x):
        self.agregar_imagen("Police Station Filled-64.png", x, y)

    def agregar_patrulla(self, y, x, theta, reflection):
        self.agregar_imagen("Police-64.png", x, y, theta, reflection)

    def agregar_taxi(self, y, x, theta, reflection):
        self.agregar_imagen("Taxi-64.png", x, y, theta, reflection)

    def agregar_calle(self, y, x):
        label = self.simulationGrid.itemAtPosition(y, x).widget()
        label.setStyleSheet("background-color: #666666;")

    def agregar_imagen(self, filename, x, y, theta=0, reflection=False):
        path = os.path.join(os.path.dirname(__file__), "assets", filename)
        pixmap = QtGui.QPixmap(path)
        label = self.simulationGrid.itemAtPosition(y, x).widget()
        pixmap = pixmap.scaled(label.size(), QtCore.Qt.KeepAspectRatio)

        if theta != 0:
            pixmap = pixmap.transformed(QtGui.QTransform().rotate(theta))

        if reflection:
            pixmap = pixmap.transformed(QtGui.QTransform().scale(-1, 1))

        time.sleep(self.tiempo_intervalo)
        label.setPixmap(pixmap)
        self.app.processEvents()

    def quitar_imagen(self, y, x):
        pixmap = QtGui.QPixmap()
        label = self.simulationGrid.itemAtPosition(y, x).widget()

        time.sleep(self.tiempo_intervalo)
        label.setPixmap(pixmap)
        self.app.processEvents()
