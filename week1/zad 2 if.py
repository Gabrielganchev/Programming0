from random import randint


player1 = input ("whats your name player1  ?")
player2 =input("whats your name player2 ?")
player1_zar = randint(1, 20)
print("player 1")
print(player1_zar)
player2_zar = randint(1, 20)
print("player 2")
print(player2_zar)
            
if player1_zar == player2_zar:
print("ravni")
elif player1_zar > player2_zar:
print("The winner is: " + player1)
else:
print("The winner is: " + player2)
