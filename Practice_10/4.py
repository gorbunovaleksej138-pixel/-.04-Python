print("=== КАССОВЫЙ АППАРАТ ===")
print("Вводите цены товаров (0 для завершения)")

total = 0  # Общая сумма

while True:
    try:
        price = int(input("Цена товара: "))
    except ValueError:
        print("Ошибка. Введите целое число.")
        continue

    if price == 0:
        break  # Завершение ввода

    if price < 0:
        print("Ошибка цены. Цена не может быть отрицательной.")
        continue

    total += price  # Добавляем цену к сумме
    print(f"Товар добавлен. Текущая сумма: {total} руб.")

print(f"\nСумма покупок: {total} руб.")

# Применение скидки
if total > 1000:
    discount = total * 0.10
    final_price = total - discount
    print(f"Стоимость привысила 1000р. Вы получате скидку 10%: -{discount:.0f} руб.")
    print(f"Итого к оплате: {final_price:.0f} руб.")
else:
    print(f"Итого к оплате: {total} руб.")