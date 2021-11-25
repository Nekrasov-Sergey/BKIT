from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):

    @property  # property позволяет превратить метод класса в атрибут класса

    @abstractmethod  # Абстрактным называется объявленный, но не реализованный метод
    def product(self) -> None:
        pass

    @abstractmethod  # Абстрактным называется объявленный, но не реализованный метод
    def milk(self) -> None:  # молоко
        pass

    @abstractmethod
    def gum(self) -> None:  # жвачка
        pass

    @abstractmethod
    def washing_powder(self) -> None:  # стиральный порошок
        pass


class Shop_Builder(Builder):

    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
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


class Shop():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"В магазине продаются: {', '.join(self.parts)}", end="")


class Director:

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
    director = Director()
    builder = Shop_Builder()
    director.builder = builder

    print("Магнит: ")
    director.Magnit()
    builder.product.list_parts()

    print("\n\nМагнит косметик: ")
    director.Magnit_Cosmetic()
    builder.product.list_parts()
