print("Программа для прогноза роста популяции")
m = int(input("Стартовое количество: "))
p = int(input("Процент увеличения: "))
n = int(input("Количество дней: "))
population = m
for day in range(1, n + 1):
    print(f"День - {day} Размер популяции - {int(population)}")
    population = population * (1 + p / 100)