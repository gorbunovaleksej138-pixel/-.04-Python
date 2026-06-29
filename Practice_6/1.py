print("Программа для определения состояния здоровья на основе введенных данных")
temperature, pressure, pulch =  map(int, input("Введите вашу температуру, давление и пульс целыми числами. Для разделения нажмите на пробел").split()) #Ввод перемнных одной строкой
if temperature >= 36 and temperature <= 37 and pressure >= 110 and pressure <=130 and pulch >= 60 and pulch <= 100:#gdgsg
    print("Вы здоровый!")
#Условие иначе проверяет отклонение хотябы в двух параметрах (немного запарился с этим но тем не менее)
elif ((temperature >= 35 and temperature <= 36) or (temperature >= 37 and temperature <= 38) and (pressure >= 105 and pressure <= 110) or (pressure <=140 and pressure >= 130))\
      or ((pulch >= 55 and pulch <= 60) or (pulch >= 100 and pulch <= 110) and (temperature >= 35 and temperature <= 36) or (temperature >= 37 and temperature <= 38))\
        or ((pulch >= 55 and pulch <= 60) or (pulch >= 100 and pulch <= 110) and (temperature >= 35 and temperature <= 36) or (temperature >= 37 and temperature <= 38)):
    '''
    Сначала программа проверяет температуру и давление
    Потом пульс и температуру
    А затем пульс и температуру
    '''
    print("У вас легкое недомогание")
elif temperature < 35 or temperature > 38 and pressure < 105 or pressure > 140 and pulch < 55 or pulch > 38: #Здесь проверяется все три характеристики показатели
    print("Ваши показатели неудовлетворительны! Обратитесль за помощью к врачу")
