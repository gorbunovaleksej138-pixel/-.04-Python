print("Программа для рассчета знакочередующаяся суммы")
n = int(input("Введите число n: "))
total = 0

for i in range(1, n + 1):
    if i % 2 == 1:
        total += i
    else:
        total -= i

print(f"Итоговое число после расчета: {total}")