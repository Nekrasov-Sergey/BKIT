import time
from contextlib import contextmanager


class cm_timer1:  # реализации на основе класса

    def __init__(self):
        self.startTime = time.time()

    def __enter__(self):  # этот метод создает и возвращает объект связи базы данных
        self.startTime = time.time()

    def __exit__(self, type, value, traceback):  # этот метод закрывает файл
        if type is not None:
            print(type, value, traceback)
        else:
            print("time: {}".format(time.time() - self.startTime))


@contextmanager
def cm_timer2():  # реализация с использованием библиотеки contextlib
    startTime = time.time()
    yield
    print("time: {}".format(time.time() - startTime))


if __name__ == '__main__':
    with cm_timer1():  # with вызывает метод __enter__
        time.sleep(5.5)
    with cm_timer2():
        time.sleep(5.5)
