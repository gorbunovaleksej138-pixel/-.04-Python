print("Анализ цифр введенного целого числа")
num = int(input("Введите целое число: "))

# Инициализация
count_3 = 0
last_digit = num % 10
count_last = 0
even_count = 0
sum_greater_5 = 0
prod_greater_7 = 1
count_0_5 = 0

# Обработка цифр
temp = num
while temp > 0:
    digit = temp % 10

    if digit == 3:
        count_3 += 1
    if digit == last_digit:
        count_last += 1
    if digit % 2 == 0:
        even_count += 1
    if digit > 5:
        sum_greater_5 += digit
    if digit > 7:
        prod_greater_7 *= digit
    if digit in (0, 5):
        count_0_5 += 1

    temp //= 10

# Если не было цифр > 7, произведение = 1
if prod_greater_7 == 1:
    temp = num
    while temp > 0:
        if temp % 10 > 7:
            break
        temp //= 10
    else:
        prod_greater_7 = 1

# Вывод результатов с подписями
print("Количество цифр 3:", count_3)
print("Сколько раз последняя цифра:", count_last)
print("Количество четных цифр:", even_count)
print("Сумма цифр больше пяти:", sum_greater_5)
print("Произведение цифр больше семи:", prod_greater_7)
print("Количество цифр 0 и 5:", count_0_5)