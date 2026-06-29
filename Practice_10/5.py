balance = 1000  # Начальный баланс

print("=== БАНКОМАТ ===")
print("Начальный баланс: 1000 руб.")

while True:
    print("\nМеню:")
    print("1. Узнать баланс")
    print("2. Снять 100 руб")
    print("3. Положить 100 руб")
    print("4. Выход")

    try:
        choice = int(input("Выберите операцию (1-4): "))
    except ValueError:
        print("Неверная команда. Введите число от 1 до 4.")
        continue

    if choice == 1:
        print(f"Текущий баланс: {balance} руб.")

    elif choice == 2:
        if balance >= 100:
            balance -= 100
            print("Снято 100 руб.")
        else:
            print("Недостаточно средств.")

    elif choice == 3:
        balance += 100
        print("Получено 100 руб.")

    elif choice == 4:
        print("До свидания!")
        break

    else:
        print("Неверная команда. Введите число от 1 до 4.")

print(f"Итоговый баланс: {balance} руб.")