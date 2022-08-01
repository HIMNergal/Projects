#Калькулятор v2

from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()
print ( Fore. BLACK)
print ( Back. MAGENTA)

what = input("Что делаем? (+, -): ")

print ( Back. CYAN)

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

if what == "+":
    c = a + b
    print( Back. YELLOW)
    print("Результат: " + str(c))
elif what == "-":
	c = a - b
	print("Результат: " + str(c))
else:
	print (Fore. RED)
	print("Выбрана неверная операция!")

input()