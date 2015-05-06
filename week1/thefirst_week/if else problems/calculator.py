a=int(input("number"))
b=int(input("number"))
operation =input("Enter Operation")
if operation == "+":
    print(a+b)
elif operation=="-":
    print(a-b)
elif operation=="*":
    print(a*b)
elif operation=="/":
    print(a/b)
else:
    print("WE do not support that operation")
