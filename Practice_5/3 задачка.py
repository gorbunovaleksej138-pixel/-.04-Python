def convert_usd_to_rub(amount_usd):
    """
    Конвертирует сумму из долларов США в рубли.

    Аргументы:
        amount_usd: сумма в долларах (float или int)

    Возвращает:
        float: сумма в рублях
    """
    USD_TO_RUB = 95.50
    return amount_usd * USD_TO_RUB


# Основная программа
usd_amount = float(input("Введите сумму в долларах: "))
rub_amount = convert_usd_to_rub(usd_amount)

print(f"{usd_amount} USD = {rub_amount:.2f} RUB")