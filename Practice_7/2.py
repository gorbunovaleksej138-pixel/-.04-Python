# Заголовок программы
print("=" * 40)
print("📦  СИСТЕМА ОТСЛЕЖИВАНИЯ ЗАКАЗОВ  📦")
print("=" * 40)

# Ввод статуса заказа
status = input("Введите статус заказа (pending/processing/shipped/delivered/cancelled): ").lower()

print("\n" + "═" * 40)

# Обработка статусов через match-case
match status:
    case "pending":
        name = "В ожидании"
        desc = "Заказ принят, ожидает обработки"
        emoji = "⏳ 📋"
        time = "1-2 часа"
        color = "🟡"
    case "processing":
        name = "В обработке"
        desc = "Заказ формируется и проверяется"
        emoji = "🔧 📦"
        time = "2-4 часа"
        color = "🔵"
    case "shipped":
        name = "Отправлено"
        desc = "Заказ передан в службу доставки"
        emoji = "🚚 📤"
        time = "1-3 дня"
        color = "🟣"
    case "delivered":
        name = "Доставлено"
        desc = "Заказ получен покупателем"
        emoji = "✅ 🏠"
        time = "Доставка завершена"
        color = "🟢"
    case "cancelled":
        name = "Отменено"
        desc = "Заказ отменен"
        emoji = "❌ 📝"
        time = "Нет времени ожидания"
        color = "🔴"
    case _:  # Обработка некорректного ввода
        name = "Ошибка"
        desc = "Некорректный статус"
        emoji = "⚠️"
        time = "Проверьте ввод"
        color = "⚫"

# Вывод информации о статусе
print(f"{color} ИНФОРМАЦИЯ О СТАТУСЕ ЗАКАЗА {color}")
print("─" * 40)
print(f"📊 Статус:    {name}")
print(f"📝 Описание:  {desc} {emoji}")
print(f"⏱️  Время:    {time}")
print("─" * 40)

# Завершение программы
print("\n" + "=" * 40)
print("Спасибо за использование системы! 👋")
print("=" * 40)