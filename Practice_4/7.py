print("Программа для определения купе по месту")
seat = int(input('Введите ваше место: '))
compartment = (seat - 1) // 4 + 1
print('Ваше купе:', compartment)
