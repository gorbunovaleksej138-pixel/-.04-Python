#Подключения блока математических данных
import math
#Объяснение пользователю действие программы
print("Программа-калькулятор, которая умеет считать площадь круга и прямоугольника")
#Пользователь задает значение переменным
height, width = map(float, input("Введите высоту и ширину прямоугольника (одной строкой, разделив пробелом): ").split())
def calculate_rectangle_area(height, width):
    """
    Вычисляет площадь прямогольника по заданнаым величиным
    :param radius:
                    height (float): Высота прямоугольника
                    width  (float): Ширина прямоугольника
    :return:
                    float: площадь прямоугольника
    """
    AREA = height * width
    return AREA
#Вывод результата
print(f"Площадь прямоугольника равна: {calculate_rectangle_area(height, width)}")
#Пользователь задает значение переменной
radius = int(input("Введите радиус круга: "))
def calculate_circle_area(radius):
    """
    Вычисляет площадь прямогольника по заданнаым величиным
    :param radius (float):
                            радиус круга
    :return:
                    float: площадь круга
    """
    AREA = math.pi * radius ** 2
    return AREA
#Вывод результата
print(f"Площадь круга равна: {calculate_circle_area(radius):.2f}")