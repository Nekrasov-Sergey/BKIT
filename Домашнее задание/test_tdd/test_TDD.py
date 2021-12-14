import unittest  # автоматизация тестов
import sys, os  # предоставляет системе особые параметры и функции

from app.handlers.ticket import *

sys.path.append(os.getcwd())  # добавить путь поиска модулей


class TestBot(unittest.TestCase):
    def test_ticket(self):
        self.assertEqual(ticket_check("Сочи"), 0)
        self.assertEqual(ticket_check("Липецк"), 1)

    def test_day(self):
        self.assertEqual(day_check("7"), 0)
        self.assertEqual(day_check("4"), 1)

    def test_trip(self):
        self.assertEqual(trip_check("поезд"), 0)
        self.assertEqual(trip_check("пешком"), 1)
