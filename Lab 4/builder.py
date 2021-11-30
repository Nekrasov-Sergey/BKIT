from __future__ import annotations  # для аннотаций ->
from abc import ABC, abstractmethod  # для использования абстракции
from typing import Any  # Средство проверки статического типа


# для значения типа Any и присвоить его любой переменной


# Строитель — это порождающий паттерн проектирования, который позволяет создавать сложные объекты пошагово.
# Строитель даёт возможность использовать один и тот же код строительства для получения разных представлений объектов.
class Builder(ABC):

    @property  # property позволяет превратить метод класса в атрибут класса

    @abstractmethod  # Абстрактным называется объявленный, но не реализованный метод
    def product(self) -> None:  # проверка типов аргументов и возвращаемое значение функции
        pass

    @abstractmethod  # Абстрактным называется объявленный, но не реализованный метод
    def milk(self) -> None:  # молоко
        pass

    @abstractmethod  # Абстрактным называется объявленный, но не реализованный метод
    def gum(self) -> None:  # жвачка
        pass

    @abstractmethod  # Абстрактным называется объявленный, но не реализованный метод
    def washing_powder(self) -> None:  # стиральный порошок
        pass


class Shop_Builder(Builder):  # мой класс - строитель магазина

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:  # функция сброса
        self._product = Shop()

    @property  # property позволяет превратить метод класса в атрибут класса
    def product(self) -> Shop:
        product = self._product
        self.reset()
        return product

    def milk(self) -> None:
        self._product.add("молоко")

    def gum(self) -> None:
        self._product.add("жвачка")

    def washing_powder(self) -> None:
        self._product.add("стиральный порошок")


class Shop:

    def __init__(self) -> None:
        self.parts = []  # parts - части

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"В магазине продаются: {', '.join(self.parts)}", end="")


class Director:  # Директор отвечает только за выполнение шагов построения в определённой последовательности

    def __init__(self) -> None:
        self._builder = None

    @property  # property позволяет превратить метод класса в атрибут класса
    def builder(self) -> Builder:
        return self._builder

    @builder.setter  # применяется сеттер к методу builder, то есть делаем метод доступным для записи
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def Magnit(self) -> None:
        self.builder.milk()
        self.builder.gum()

    def Magnit_Cosmetic(self) -> None:
        self.builder.gum()
        self.builder.washing_powder()


if __name__ == "__main__":
    director = Director()  # наследование класса
    builder = Shop_Builder()
    director.builder = builder

    print("Магнит: ")
    director.Magnit()
    builder.product.list_parts()

    print('\n')

    print("Магнит косметик: ")
    director.Magnit_Cosmetic()
    builder.product.list_parts()
