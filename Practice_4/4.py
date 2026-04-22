print("Программа для расчета сколько  мандаринов достанется каждому школьнику после деления")
students = int(input('количество школьников: '))
tangerines = int(input('количество мандаринов: '))
tangerines_per_student = tangerines // students
print('количество мандаринов у школьника:', tangerines_per_student)
tangerines_in_basket = tangerines % students
print('количество мандаринов в корзине:', tangerines_in_basket)