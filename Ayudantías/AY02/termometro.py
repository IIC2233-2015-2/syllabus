# coding=utf-8


class Termometro:
    def __init__(self, temperatura_abs):
        self.kelvin = temperatura_abs

    @property
    def celsius(self):
        return self.kelvin - 273

    @celsius.setter
    def celsius(self, value):
        self.kelvin = value + 273

    @property
    def fahrenheit(self):
        return (self.celsius * 1.8) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        # Reutilizamos el setter que declaramos :)
        self.celsius = (value - 32) / 1.8


if __name__ == '__main__':
    temp = Termometro(temperatura_abs=293)
    print(temp.celsius)
    print(temp.kelvin)
    print(temp.fahrenheit)

    temp.celsius = 31
    print(temp.celsius)
    print(temp.kelvin)
    print(temp.fahrenheit)
