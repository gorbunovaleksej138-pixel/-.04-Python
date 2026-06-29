print("Поиск максимального числа в последовательности")
print("Вводите натуральные числа (0 для завершения):")

max_number = 0  # Начальное значение максимума
count = 0  # Счетчик введенных чисел

while True:
    try:
        num = int(input("Число: "))
    except ValueError:
        print("Ошибка. Введите натуральное число.")
        continue

    if num == 0:
        if count == 0:
            print("Не введено ни одного числа.")
        else:
            print(f"\nМаксимальное число: {max_number}")
        break  # Завершаем программу

    if num < 0:
        print("Ошибка. Введите натуральное число.")
        continue

    # Первое число становится максимумом
    if count == 0:
        max_number = num
    elif num > max_number:
        max_number = num

    count += 1  # Увеличиваем счетчик чисел