
a = int(input("number "))
x = int(input("number "))
a = int(input("number "))

if x==a:
    print("The number is equal to the lower bound of the interval")
elif x==b:
    print("The number is equal to the upper bound of the interval")
elif a<x<b:
    print("The number is in the interval")
elif x<a:
    print("The number is outside the interval ,x<a ")
elif x>b:
    print("The number is outside the interval, x > b")
else:
    print("what of shit")
