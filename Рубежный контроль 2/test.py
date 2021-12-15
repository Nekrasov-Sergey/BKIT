import unittest  # автоматизация тестов
import sys, os  # предоставляет системе особые параметры и функции

from main import *

sys.path.append(os.getcwd())  # добавить путь поиска модулей


class Test(unittest.TestCase):
    def test1(self):
        one_to_many = [(o.name, o.cost, c.name)
                       for c in comps
                       for o in oses
                       if c.id == o.comp_id]
        self.assertEqual(test1(one_to_many), [('Abuntu', 'Msi'), ('Adora', 'Asus')])

    def test2(self):
        one_to_many = [(o.name, o.cost, c.name)
                       for c in comps
                       for o in oses
                       if c.id == o.comp_id]
        self.assertEqual(test2(one_to_many), [('Msi', 1480), ('Asus', 2900), ('Apple', 5450)])

    def test3(self):
        many_to_many_temp = [(c.name, oc.os_id, oc.comp_id)
                             for c in comps
                             for oc in oses_comps
                             if c.id == oc.comp_id]
        many_to_many = [(o.name, o.cost, c_name)
                        for c_name, oc_id, c_id in many_to_many_temp
                        for o in oses
                        if o.id == oc_id]
        self.assertEqual(test3(many_to_many),
                         [('Abuntu', 'Msi'), ('Abuntu', 'Lenovo'), ('Adora', 'Acer'), ('Adora', 'Asus'),
                          ('ChromeOS', 'Msi'), ('ChromeOS', 'Lenovo'), ('MacOS', 'Acer'), ('MacOS', 'Apple'),
                          ('Windows', 'Msi'), ('Windows', 'Asus')])
