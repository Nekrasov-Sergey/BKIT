import unittest
import sys, os
from builder import *

sys.path.append(os.getcwd())


class Shop_Test_Builder(unittest.TestCase):
    director = Director()
    builder = Shop_Builder()
    director.builder = builder

    def test_magnit_builder(self):
        print("Магнит: ")
        self.director.Magnit()
        self.builder.product.list_parts()

    def test_magnit_cosmetic_builder(self):
        print("\nМагнит косметик: ")
        self.director.Magnit_Cosmetic()
        self.builder.product.list_parts()
