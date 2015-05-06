def dev(n):
    a=int(input("number for a "))
    b=1
    c=[]
    while True:
        if a%b==0:
            print(b)
            c=c+[b]
          # b+=1 was here and it didnt work i know why  
            print(c)
        if a==b:
            print("whatever")
            break
        b+=1
   
