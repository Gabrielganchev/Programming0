from random import randint
a=(input("your name"))
b=(input("YOUR NAME "))
number=int(input("number "))


first_diceroll = randint(1,number)
second_diceroll = randint(1,number)
print(first_diceroll)
print(second_diceroll)

if first_diceroll > second_diceroll:
    print(a + " has rolled " +str(first_diceroll))
else:
    print(b + "   has rolled " +str(second_diceroll))
#done perfectly
