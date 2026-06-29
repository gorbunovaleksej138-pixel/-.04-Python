#Подключения блока математических данных
import math
#Объяснение работы программы
print("Программа для вычисления площади треугольника по координатам трех его вершин")
#Пользователь вводит значения всех трех перемнных одной строчкой
x1, y1, x2, y2, x3, y3 = map(float, input("Введите координаты (xi.yi) точек А,В,С (одной строкой, разделив пробелом каждое значение): ").split())
def calculate_distance(x1, y1, x2, y2):
    """
    Вычисляет евклидово расстояние между двумя точками.

    Args:
        x1, y1 (float): Координаты первой точки
        x2, y2 (float): Координаты второй точки
    :return:
        float: Расстояние между двумя точками.
    """
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance
#Возвращает функцию три раза (три величины)
a = calculate_distance(x1, y1, x2, y2)
b = calculate_distance(x1, y1, x3, y3)
c = calculate_distance(x2, y2, x3, y3)
def calculate_triangle_area(a, b, c):
    """
    Args:
        a, b, c: стороны треугольника
    :return:
        Площадь по формуле Герона
    """
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return S
area = calculate_triangle_area(a, b, c)
print(f"Площадь треугольника: {area:.2f}")