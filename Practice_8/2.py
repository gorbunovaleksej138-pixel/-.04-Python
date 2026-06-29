print("Проверка 10 чисел на четность")
even_count = 0
for i in range(1, 11):
    num = int(input(f"Число {i}: "))
    if num % 2 == 0:
        even_count += 1

if even_count == 10:
    print("YES")
else:
    print("NO")