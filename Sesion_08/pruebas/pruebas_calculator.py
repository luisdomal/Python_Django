"""Ejemplo de pruebas"""

import unittest

from calculator import Calculator


class CalculatorTestCase(unittest.TestCase):
    """Test a calculator"""

    def setUp(self):
        """Tareas de inicialización, se ejecuta una vez antes de cada prueba"""
        print("SET UP")
        self.calculator = Calculator()

    def test_suma(self):
        print("SUMA")
        result = self.calculator.sumar(1, 2)
        self.assertEqual(result, 3)

    def test_resta(self):
        print("RESTA")
        result = self.calculator.restar(6, 2)
        self.assertEqual(result, 4)

    def test_multiplicar(self):
        print("MULTIPLICACIÓN")
        result = self.calculator.multiplicar(6, 2)
        self.assertEqual(result, 12)

    def tearDown(self):
        print("TEAR DOWN")
        """Tareas de limpieza, se ejecuta una vez después de cada prueba"""

    @classmethod
    def setUpClass(cls):
        """Inicialización de clase, se ejecuta una vez antes de TODAS las pruebas"""
        print("SET UP CLASS")
        pass

    @classmethod
    def tearDownClass(cls):
        """Limpieza, se ejecuta al finalizar TODAS las pruebas"""
        print("TEAR DOWN CLASS")
        pass


if __name__ == '__main__':
    unittest.main()
