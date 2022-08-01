import random

random_namber = random.randint(1, 5)
user_namber = input("Угадай число (от 1 до 5): ")

if int(user_namber) == random_namber:
    print("Вы угадали!")
    print(f"Всё верно! Было загадано число {random_namber}")

else:
    print("Вы НЕ угадали ;)")
    print(f"Было загадано число {random_namber}")