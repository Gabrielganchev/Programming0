a=int(input("number for a "))
b=int(input("number for b "))

#tazi ne q razbiram modulno ot 10 ? utre shte q pogledna pak 
a_last = a % 10
b_last = b % 10
if a_last > b_last:
    print(a)
elif a_last < b_last:
    print(b)
else:
    if a > b:
        print(a)
    else:
        print(b)
