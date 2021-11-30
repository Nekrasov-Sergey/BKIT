import unittest  # автоматизация тестов
import sys, os  # предоставляет системе особые параметры и функции

from builder import *  # импортировать всё из builder

sys.path.append(os.getcwd())  # добавить путь поиска модулей


class Shop_Test_Builder(unittest.TestCase):
    builder = Shop_Builder()

    def test_magnit_builder(self):
        self.assertEqual(Director.Magnit(self), None)

    def test_magnit_cosmetic_builder(self):
        self.assertEqual(Director.Magnit_Cosmetic(self), None)
