import random

secret_number = random.randint(1, 10)
attempts = 3

print("Я загадав число від 1 до 10. У тебе є 3 спроби, щоб вгадати його!")

for i in range(attempts):
    user_guess = int(input("Введіть ваше число: "))

    if user_guess == secret_number:
        print("Вітаю! Ти вгадав число!")
        break
    elif user_guess > secret_number:
        print("Менше")
    else:
        print("Більше")
else:
    print(f"Спроби закінчилися! Я загадав число {secret_number}.")
