print("=" * 40)
print("☕  МЕНЮ КАФЕ  🍰")
print("=" * 40)

# Константы цен
COFFEE_PRICE = 120
TEA_PRICE = 80
JUICE_PRICE = 100
WATER_PRICE = 50
LEMONADE_PRICE = 90

print("1. Кофе☕ - 120 руб.")
print("2. Чай🍵 - 80 руб.")
print("3. Сок🧃 - 100 руб.")
print("4. Вода💧 - 50 руб.")
print("5. Лимонад🥤 - 90 руб.")
print("-" * 40)

# Ввод данных
drink_input = input("Выберите напиток (номер 1-5 или название): ").strip().lower()
quantity = int(input("Количество порций: "))
discount_code = input("Код скидки (если есть, иначе Enter): ").strip().upper()

print("\n" + "=" * 40)
print("🧾  ВАШ ЗАКАЗ  🧾")
print("=" * 40)

# Обработка выбора напитка
drink_name = ""
price = 0

match drink_input:
    case "1" | "кофе" | "coffee":
        drink_name = "Кофе ☕"
        price = COFFEE_PRICE
    case "2" | "чай" | "tea":
        drink_name = "Чай 🍵"
        price = TEA_PRICE
    case "3" | "сок" | "juice":
        drink_name = "Сок 🧃"
        price = JUICE_PRICE
    case "4" | "вода" | "water":
        drink_name = "Вода 💧"
        price = WATER_PRICE
    case "5" | "лимонад" | "lemonade":
        drink_name = "Лимонад 🥤"
        price = LEMONADE_PRICE
    case _:
        drink_name = "Ошибка выбора ❌"
        price = 0

# Расчет суммы
subtotal = price * quantity

# Применение скидки
discount = 0
discount_text = "нет"

match discount_code:
    case "WELCOME10":
        discount = subtotal * 0.1  # 10% скидка
        discount_text = "10%"
    case "VIP15":
        discount = subtotal * 0.15  # 15% скидка
        discount_text = "15%"
    case "SUMMER20":
        discount = subtotal * 0.2  # 20% скидка
        discount_text = "20%"
    case "":
        discount = 0
        discount_text = "нет"
    case _:
        discount = 0
        discount_text = f"код '{discount_code}' недействителен"

# Итоговая сумма
total = subtotal - discount

# Правильное склонение "порция"
if quantity % 10 == 1 and quantity % 100 != 11:
    portion_word = "порция"
elif 2 <= quantity % 10 <= 4 and not (12 <= quantity % 100 <= 14):
    portion_word = "порции"
else:
    portion_word = "порций"

# Вывод чека
if drink_name != "Ошибка выбора ❌":
    print(f"Напиток:        {drink_name}")
    print(f"Цена за 1 шт.:  {price} руб.")
    print(f"Количество:     {quantity} {portion_word}")
    print(f"Сумма:          {subtotal} руб.")
    print(f"Скидка:         {discount_text}")
    print("-" * 40)

    if discount > 0:
        print(f"Сумма скидки:   {discount:.0f} руб.")

    print(f"ИТОГО К ОПЛАТЕ: {total:.0f} руб.")
else:
    print("❌ Ошибка: выбран неверный напиток")
    print("Пожалуйста, перезапустите программу")

print("=" * 40)
print("Спасибо за заказ! Приходите еще! 😊")
print("=" * 40)