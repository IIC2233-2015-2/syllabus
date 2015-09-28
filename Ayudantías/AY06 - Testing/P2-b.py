from collections import defaultdict
import pytest


__author__ = 'patricio_lopez'


class Dispositivo:

    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


class Router:

    def __init__(self, max_conexiones):
        self.max_conexiones = max_conexiones

        generador = self.__available_ips()

        def nueva_conexion():
            return next(generador)

        self.connections = defaultdict(nueva_conexion)

    def send_data(self, device, data):
        """
        Manda data identificado como el dispositivo.
        Si la data es invalida, no la envia.
        """
        device_ip = self.connections[device]
        return self.__send_data_to_internet(device_ip, data)

    def __send_data_to_internet(self, ip, data):
        if data:
            output = "{}: {}".format(ip, data)
            print(output)
            return output

    def __available_ips(self):
        while len(self.connections) < self.max_conexiones:
            yield(self.random_ip())

    @staticmethod
    def random_ip():
        from random import randint
        return ".".join([str(randint(0, 255)) for x in range(0, 4)])


class TestRouter:
    MAX_CONECTIONS = 5

    def pytest_funcarg__cellphone(request):
        class Celular(Dispositivo):
            pass

        return Celular(nombre="iWindroid Phone")

    def pytest_funcarg__notebook(request):
        class Notebook(Dispositivo):
            pass

        return Notebook(nombre="PC")

    def pytest_funcarg__device_generator(request):
        def dispositivos_generator():
            id = 0
            for _ in range(30):
                yield(Dispositivo("PC {}".format(id)))
                id += 1
        return dispositivos_generator

    def setup_method(self, method):
        self.router = Router(TestRouter.MAX_CONECTIONS)

    def test_connect_device(self, cellphone):
        assert self.router.send_data(cellphone, "Data")

    def test_max_connections(self, device_generator):
        for i, device in enumerate(device_generator()):
            if i <= TestRouter.MAX_CONECTIONS:
                assert self.router.send_data(device, "Data")
            else:
                assert not self.router.send_data(device, "Data")

    def test_repeated_ip(self, monkeypatch, cellphone, notebook):
        # Con 'monkeypath' podemos reemplazar una funcion de una clase
        # Docs: https://pytest.org/latest/monkeypatch.html

        def static_ip():
            """
            Funcion que siempre genera la misma IP
            """
            return "255.255.255.255"

        # Reemplazamos la funcion que crea IPs random
        monkeypatch.setattr(self.router, 'random_ip', static_ip)

        self.router.send_data(cellphone, "Mi IP es valida")
        with pytest.raises(Exception):
            # Esperamos que cuando se repita la IP se genere alguna excepcion.
            self.router.send_data(notebook, "Mi IP esta duplicada D:!")

    def test_invalid_device(self):
        with pytest.raises(Exception):
            assert not self.router.send_data(None, "Data")

        with pytest.raises(Exception):
            self.router.send_data("", "Data")

    def test_invalid_data(self, cellphone):
        assert not self.router.send_data(cellphone, None)
        assert not self.router.send_data(cellphone, "")
