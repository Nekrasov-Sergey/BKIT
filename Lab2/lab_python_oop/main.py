from lab_python_oop.rectangle import Rectangle  # прямоугольник
from lab_python_oop.circle import Circle  # круг
from lab_python_oop.square import Square  # квадрат

from PIL import Image, ImageDraw


def get_picture(r, c, s):
    imagine = Image.new('RGB', (800, 400), (255, 255, 255))  # размер рамки и цвет фона
    drawing = ImageDraw.Draw(imagine)
    scale = 20  # коэффициент
    drawing.rectangle((10, 10, scale * r.width, scale * r.height), fill='blue', outline=(0, 0, 0))
    drawing.ellipse((200, 10, 200 + 2 * scale * c.r, 10 + 2 * scale * c.r), fill='green', outline=(0, 0, 0))
    drawing.rectangle((570, 90, 570 + scale * s.width, 90 + scale * s.width), fill='red', outline=(0, 0, 0))
    # координаты верхнего левого угла, координаты нижнего правого угла, цвет фигуры и рамки
    drawing.text((50, 350), 'Rectangle', fill='blue')
    drawing.text((340, 350), 'Ellipse', fill='green')
    drawing.text((630, 350), 'Square', fill='red')
    # координаты, название, цвет надписи
    imagine.show()  # рисует фигуры


def main():
    r = Rectangle("синего", 8, 16)
    c = Circle("зеленого", 8)
    s = Square("красного", 8)
    print(r)
    print(c)
    print(s)

    get_picture(r, c, s)


if __name__ == "__main__":
    main()
