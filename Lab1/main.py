import sys
import math


def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        try:
            coef = float(input())
        except ValueError:
            print("Введены недопустимые символы")
            return get_coef(index, prompt)
    # Переводим строку в действительное число

    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float] Список корней
    '''
    result = []
    D = b * b - 4 * a * c
    if D < 0.0:
        print('Решений нет')
        exit(0)

    elif D == 0.0:
        if a != 0:
            x = -b / (2 * a)
        elif b != 0:
            x = -c / b
        elif c == 0:
            print('Любые решения')
            exit(0)
        else:
            print("Решений нет")
            exit(0)

        if x < 0:
            print('Решений нет')
            exit(0)
        elif x == 0:
            result.append(0)
        else:
            result.append(math.sqrt(x))
            result.append(-math.sqrt(x))

    else:
        if a != 0:
            x1 = (-b + math.sqrt(D)) / (2.0 * a)
        elif b != 0:
            x1 = -c / b
        if x1 > 0:
            result.append(math.sqrt(x1))
            result.append(-math.sqrt(x1))
        elif x1 == 0:
            result.append(0)

        if a != 0:
            x2 = (-b - math.sqrt(D)) / (2.0 * a)
        elif b != 0:
            x2 = -c / b
        if x2 > 0 and x2 != x1:
            result.append(math.sqrt(x2))
            result.append(-math.sqrt(x2))
        elif x2 == 0 and x2 != x1:
            result.append(0)

    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print('Решений нет')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {} и {} и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {} и {} и {} и {}'.format(roots[0], roots[1], roots[2], roots[3]))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
