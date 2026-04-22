print("программа для нахождения цифр четырёхзначного числа")
number = int(input('Введите число: '))
thousands = number // 1000
print('тысячи', thousands)
hundreds = number // 100 % 10
print('сотни', hundreds)
tens = number // 10 % 10
print('десятки', tens)
units = number % 10
print('единицы', units)