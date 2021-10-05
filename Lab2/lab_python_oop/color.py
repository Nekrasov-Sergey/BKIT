class FigureColor:
    """
    Класс «Цвет фигуры»
    """

    def __init__(self):  # init-метод, который играет роль конструктора
        self._color = None

    @property  # property позволяет превратить метод класса в атрибут класса
    def colorproperty(self):
        """
        Get-аксессор
        """
        return self._color

    @colorproperty.setter  # применяется сеттер к методу colorproperty, то есть делаем метод доступным для записи
    # а не только для чтения
    def colorproperty(self, value):
        """
        Set-аксессор
        """
        self._color = value
