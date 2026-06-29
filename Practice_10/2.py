print("Введите три числа в строго возрастающем порядке")

# Ввод первого числа
while True:
    try:
        num1 = int(input("Введите первое число: "))
        break
    except ValueError:
        print("Ошибка. Введите целое число.")
        continue

# Ввод второго числа
while True:
    try:
        num2 = int(input("Введите второе число: "))
    except ValueError:
        print("Ошибка. Введите целое число.")
        continue

    if num2 > num1:
        break  # Правильное число
    else:
        print("Ошибка. Второе число должно быть больше первого.")
        # Цикл продолжится для повторного ввода

# Ввод третьего числа
while True:
    try:
        num3 = int(input("Введите третье число: "))
    except ValueError:
        print("Ошибка. Введите целое число.")
        continue

    if num3 > num2:
        break  # Правильное число
    else:
        print("Ошибка. Третье число должно быть больше второго.")
        # Цикл продолжится для повторного ввода

# Вывод результата
print(f"\nПоследовательность принята:")
print(f"{num1} < {num2} < {num3}")