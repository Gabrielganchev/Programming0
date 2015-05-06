a = int(input("a = potrebitel chislo  "))
b= int(input("b = potrebitel chislo  "  ))
oper=str(input("populni operator "))


result = False
if oper == "+":
    result=a+b
elif oper =="-":
    result = a-b
elif oper =="*":
    result = a*b
elif oper == "/":
    result = a/b



if result !=False:
 print("Result is : ")
 print(result)
else:
     print("We do not support this operation!!!!")
