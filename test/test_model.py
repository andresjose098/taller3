# tests/test_model.py
import unittest
from model.parqueadero_model import ParqueaderoModel


class TestParqueaderoModel(unittest.TestCase):
    def setUp(self):
        self.model = ParqueaderoModel()
        self.model.inicializar_espacios()

    def test_ocupar_espacio(self):
        resultado = self.model.ocupar_espacio('ABC123')
        self.assertTrue(resultado)

    def test_liberar_espacio(self):
        self.model.ocupar_espacio('ABC123')
        resultado = self.model.liberar_espacio('ABC123')
        self.assertTrue(resultado)


if __name__ == '__main__':
    unittest.main()
