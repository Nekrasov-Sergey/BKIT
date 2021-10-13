def print_result(function):  # реализация декоратора print_result
    def decorated(*a):  # *a так как неизвестно количество аргументов
        print(function.__name__)  # печатаем имя функции
        if type(function(*a)) == list:  # если список
            for x in function(*a):
                print(x)
        elif type(function(*a)) == dict:  # если словарь
            for x in function(*a):
                print(x, '=', function(*a)[x])
        else:
            print(function(*a))

    return decorated


@print_result
def test_1():
    return '1'


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    test_1()
    test_2()
    test_3()
    test_4()
