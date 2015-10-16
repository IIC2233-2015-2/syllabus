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
    def __init__(self, app):
        super().__init__()
        self.setupUi(self)

        self.app = app
        self.tiempo_intervalo = 0

    def agregar_ambulancia(self, x, y, theta, reflection):
        self.agregar_imagen("Ambulance-64.png", x, y, theta, reflection)

    def agregar_enfermo(self, x, y):
        self.agregar_imagen("Being Sick-64.png", x, y)

    def agregar_auto(self, x, y, theta, reflection):
        filename = rnd.choice([
            "Convertible-64.png",
            "Pickup-64.png",
            "Sedan-64.png"
        ])
        self.agregar_imagen(filename, x, y, theta, reflection)

    def agregar_cuartel_bomberos(self, x, y):
        self.agregar_imagen("Fire Station-64.png", x, y)

    def agregar_carro_bomba(self, x, y, theta, reflection):
        self.agregar_imagen("Fire Truck-64.png", x, y)

    def agregar_incendio(self, x, y):
        self.agregar_imagen("Fires-64.png", x, y)

    def agregar_casa(self, x, y):
        self.agregar_imagen("Home-64.png", x, y)

    def agregar_hospital(self, x, y):
        self.agregar_imagen("Hospital 3-64.png", x, y)

    def agregar_robo(self, x, y):
        self.agregar_imagen("Pickpocket-64.png", x, y)

    def agregar_comisaria(self, x, y):
        self.agregar_imagen("Police Station Filled-64.png", x, y)

    def agregar_patrulla(self, x, y, theta, reflection):
        self.agregar_imagen("Police-64.png", x, y)

    def agregar_taxi(self, x, y, theta, reflection):
        self.agregar_imagen("Taxi-64.png", x, y, theta, reflection)

    def agregar_calle(self, x, y):
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

    def quitar_imagen(self, x, y):
        pixmap = QtGui.QPixmap()
        label = self.simulationGrid.itemAtPosition(y, x).widget()

        time.sleep(self.tiempo_intervalo)
        label.setPixmap(pixmap)
        self.app.processEvents()
