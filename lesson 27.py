import random
num = random.randint(0, 1000000)

guess = int(input("Введите число от 0 до 10: "))
while True:
    if guess < 0 or guess > 1000000:
        print("введите число из того, что мы загадали")
        guess = int(input("Введите число от 0 до 10: "))
    else:
        if guess < num:
            print("Мало")
            guess = int(input("Введите число от 0 до 10: "))
        elif guess > num:
            print("Много")
            guess = int(input("Введите число от 0 до 10: "))
        elif guess == num:
            print("Вы угадали!")
            break






