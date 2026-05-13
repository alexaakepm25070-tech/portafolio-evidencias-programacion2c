import unittest
from src.operaciones import suma, resta, multi, divi, expo

class TestOperaciones(unittest.TestCase):

    def test_suma_positivos(self):
        self.assertEqual(suma(2, 3), 5)

    def test_suma_negativos(self):
        self.assertEqual(suma(-2, -3), -5)

    def test_suma_mixta(self):
        self.assertEqual(suma(-2, 3), 1)

    def test_resta_basica(self):
        self.assertEqual(resta(10, 5), 5)

    def test_resta_negativa(self):
        self.assertEqual(resta(10, 30), -20)

    def test_resta_valoresNegativos(self):
        self.assertEqual(resta(-5, -5), 0)

    def test_multi_positivos(self):
        self.assertEqual(multi(2, 3), 6)

    def test_multi_negativos(self):
        self.assertEqual(multi(-2, -3), 6)

    def test_multi_mixta(self):
        self.assertEqual(multi(-2, 3), -6)
 
    def test_divi_basica(self):
        self.assertEqual(divi(10, 2), 5)

    def test_divi_negativa(self):
        self.assertEqual(divi(-10, 2), -5)

    def test_divi_negativos(self):
        self.assertEqual(divi(-10, -2), 5)

    def test_expo_basico(self):
        self.assertEqual(expo(2, 3), 8)

    def test_expo_negativo(self):
        self.assertEqual(expo(-2, 3), -8)

if'_name_ '== '_main_':
    unittest.main()