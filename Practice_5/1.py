print("Программа для рассчета подоходного налога")
#Ввод своего налога пользователем
yearly_income = float(input("Введите свой годовой доход (одним чисолом) - "))
#Добавление константы
tax_rate = 0.13
#Расчет суммы налога
tax_amount = yearly_income * tax_rate
#Рассчета дохода после вычета налога
income_after_tax = yearly_income - tax_amount
#Вывод результатов
print(f"Годовой доход: {yearly_income:.2f} руб.")
print(f"Рассчитанный налог: {tax_rate:.2f} руб.")
print(f"Сумма после вычета: {income_after_tax:.2f} руб.")
