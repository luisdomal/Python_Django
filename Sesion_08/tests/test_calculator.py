"""Ejemplo de pruebas"""

import unittest
from unittest import result

class CalculatorTestCase(unittest.TestCase):
    """Test a calculator"""
    def test_suma(self):
        result = 1 + 2
        self.assertEqual(result, 3)


if __name__ == '__main___':
    unittest.main()