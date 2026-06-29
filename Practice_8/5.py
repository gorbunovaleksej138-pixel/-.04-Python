print("Программа для определения двух наибольших чисел")
n = int(input("Количество чисел: "))

first_max = 0
second_max = 0

for _ in range(n):
    num = int(input("Число: "))
    if num > first_max:
        second_max = first_max
        first_max = num
    elif num > second_max:
        second_max = num

print("Первое наибольшее число", first_max)
print("Второе наибольшее число", second_max)