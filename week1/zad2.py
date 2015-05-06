# dice_roll.py

from random import randint
n = input("Enter sides: ")
# Превръщаме string-a в int. Всеки input е string
n = int(n)
result = randint(1, n)
result2 = randint(1, n)
result3 = randint (1, n)
print("first",result )
print("second",result2)
print("3th",result3)
print(result+result2+result3)
