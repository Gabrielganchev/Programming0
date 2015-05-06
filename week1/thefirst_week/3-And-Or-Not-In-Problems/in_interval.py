a=int(input("number for lower value"))
b=int(input("number for upper value"))
c=int(input("number for c"))
if c == a:
    print("The number is equal to the lower bound of the interval")
elif c == b:
    print("The number is equal to the upper bound of the interval")
elif c > a and c < b:
    print("The number is in the interval")
elif c < a:
    print("The number is outside the interval, c < a")
elif c > b:
    print("The number is outside the interval, c > b")
else:
    print("chuck norris is coming ")
    
