import json
import time
from contextlib import contextmanager
import random


class Unique(object):
    def __init__(self, items, **kwargs):  # kwargs для переменной длины аргументов
        self.data = iter(items)  # метод iter() используется для получения итератора
        self.word = set()  # создание пустого множества
        if kwargs:  # пока есть элементы
            self.app = kwargs['ignore_case']
        else:  # если элементы закончатся
            self.app = False

    def __iter__(self):  # обязательно надо вернуть объект итератора
        return self

    def __next__(self):  # вернуть следующий элемент в последовательности
        while True:
            x = next(self.data)  # перебираются элементы
            if self.app == True:
                x['job-name'] = x['job-name'].lower()  # делаем нижний регистр
            if x['job-name'] not in self.word:
                self.word.add(x['job-name'])  # добавляет элемент если его ещё не было
                return x['job-name']


def print_result(function):  # реализация декоратора print_result
    def decorated(*a):  # *a так как неизвестно количество аргументов
        print(function.__name__)  # печатаем имя функции
        if type(function(*a)) == list:  # если список
            for x in function(*a):
                print(x)
            return (function(*a))
        elif type(function(*a)) == dict:  # если словарь
            for x in function(*a):
                print(x + function(*a)[x])
        else:
            print(function(*a))

    return decorated


@contextmanager
def cm_timer_2():  # реализация с использованием библиотеки contextlib
    startTime = time.time()
    yield
    print("time: {}".format(time.time() - startTime))


# Сделаем другие необходимые импорты

path = r'C:\Users\79508\Downloads\data_light.json'

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path, encoding="utf-8") as f:
    data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    return list(Unique(arg, ignore_case=True))


@print_result
def f2(arg):
    return list(filter(lambda x: x.startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    a = (', зарплата ' + str(random.randint(100000, 200000)) + ' рублей' for x in arg)
    return dict(zip(arg, a))


if __name__ == '__main__':
    with cm_timer_2():
        f4(f3(f2(f1(data))))
