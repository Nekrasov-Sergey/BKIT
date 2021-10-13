def field(items, *args):
    assert len(args) > 0  # если есть аргументы
    if len(args) == 1:  # если аргумент один
        for vocabulary in items:
            text = vocabulary.get(args[0])  # получаем значение ключа
            if text is not None:  # если значение не нулевое
                yield text  # yield возвращает генератор text
    else:  # если аргументов несколько
        for j in items:
            vocabulary = dict()  # создали словарь с помощью dict
            for key in args:  # перебираем ключи аргументов
                text = j.get(key)  # получаем значение ключа
                if text is not None:  # если значение не нулевое
                    vocabulary[key] = text  # добавили значение к ключу
            if len(vocabulary) != 0:  # если vocabulary имеет хотя бы одно значение
                yield vocabulary  # yield возвращает генератор vocabulary


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': None},
        {'title': 'Стол', 'price': None, 'color': 'white'},
        {'title': None, 'price': None, 'color': 'pink'}
    ]
    data1 = list()  # объявили пременную как список
    data2 = list()  # объявили пременную как список

    for i in field(goods, 'title'):
        data1.append(i)
    print(data1)

    for i in field(goods, 'title', 'price'):
        data2.append(i)
    print(data2)
