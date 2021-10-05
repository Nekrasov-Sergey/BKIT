from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    """
    Класс «Квадрат» наследуется от класса «Прямоугольник».
    """
    FIGURE_TYPE = "Квадрат"

    @classmethod  # Метод класса — это метод, который привязан к классу, а не к его объекту.
    # Он не требует создания экземпляра класса
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color_param, side_param):  # init-метод, который играет роль конструктора
        """
        Класс должен содержать конструктор по параметрам «сторона» и «цвет».
        """
        self.side = side_param
        super().__init__(color_param, self.side, self.side)

    def __repr__(self):  # Функция __repr __() возвращает представление объекта.
        # Это может быть любое допустимое выражение в Python, такое как кортеж, словарь, строка и т.д.
        return '{} {} цвета со стороной {} площадью {}.'.format(
            Square.get_figure_type(),
            self.fc.colorproperty,
            self.side,
            self.square()
        )
