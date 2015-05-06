from random import randint

a=int(input("put a number here " ))
b = randint(1,a)
print("first roll  " +str(b))
print(b)# runs just once prints out the same log
i=0
while i<3:
    i+=1
    print("The roll is  ")
    print(randint(1,a))#seems legit :D but ugly
    
