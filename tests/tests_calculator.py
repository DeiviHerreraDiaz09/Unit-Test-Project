import unittest
import src.calculator as c


class CalculatorTests(unittest.TestCase):

    def test_suma(self):
        assert c.suma(2, 3) == 5

    def test_resta(self):
        assert c.restar(3, 2) == 1

    def test_multiplicacion(self):
        assert c.multiplicacion(2, 3) == 6

    def test_division(self):
        result = c.dividir(4, 2)
        expected = 2
        assert result == expected
