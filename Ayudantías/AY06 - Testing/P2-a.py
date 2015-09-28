__author__ = 'patricio_lopez'


def random_ip():
        from random import randint as i
        return ".".join([str(i(0, 255)) for x in " "*4])


def test_random_ip():
    ip = random_ip()
    ip_parts = ip.split('.')
    assert len(ip_parts) == 4

    for numero in ip_parts:
        assert 0 <= int(numero) <= 255


"""
Ahora con unittest
"""
import unittest


class RandomIpTester(unittest.TestCase):
    def test_random_ip(self):
        ip = random_ip()
        ip_parts = ip.split(".")
        self.assertEqual(len(ip_parts), 4)

        for numero in ip_parts:
            self.assertTrue(numero.isdecimal())
            self.assertTrue(0 <= int(numero) <= 255)


suite = unittest.TestLoader().loadTestsFromTestCase(RandomIpTester)
unittest.TextTestRunner().run(suite)
