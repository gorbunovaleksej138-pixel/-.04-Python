print("Угадай число от 1 до 10 за 3 попытки")
import random

secret = random.randint(1, 10)
guessed = False

for attempt in range(1, 4):
    guess = int(input(f"Попытка {attempt}: "))

    if guess == secret:
        print("Угадали!")
        guessed = True
        break
    elif guess < secret:
        print("Неверно, загаданное число больше")
    else:
        print("Неверно, загаданное число меньше")

if not guessed:
    print(f"Загаданное число было: {secret}")