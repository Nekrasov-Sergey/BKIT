from gen_random import gen_random


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
            if self.app == True and type(x) != int:  # если это буквенные символы
                x = x.lower()  # делает все элементы нижнего регистра
            if x not in self.word:
                self.word.add(x)  # добавляет элемент если его ещё не было
                return x


if __name__ == "__main__":
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    data2 = gen_random(10, 1, 3)
    data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    data4 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']

    print('1 case')
    print(list(Unique(data1)))
    print('2 case')
    print(list(Unique(data2)))
    print('3 case')
    print(list(Unique(data3, ignore_case=False)))  # игнорируем регистр
    print('4 case')
    print(list(Unique(data4, ignore_case=True)))  # не игнорируем регистр
