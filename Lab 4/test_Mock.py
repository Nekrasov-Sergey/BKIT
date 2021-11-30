import unittest  # автоматизация тестов
import sys, os  # предоставляет системе особые параметры и функции
from unittest.mock import patch, Mock
# Когда функция оформлена через @patch, mock класса, метода или функции,
# переданная в качестве цели для @patch, возвращается и передается в качестве аргумента декорируемой функции.
import builder

sys.path.append(os.getcwd())  # добавить путь поиска модулей
from builder import *


class Shop_Test_Builder(unittest.TestCase):
    @patch.object(builder.Shop_Builder(), 'milk')
    # patch.object принимает объект и имя атрибут, который требуется исправить,
    # а также, при необходимости, значение для исправления.
    def test_milk(self, mock_milk):
        mock_milk.return_value = None
        self.assertEqual(Shop_Builder().milk(), None)
