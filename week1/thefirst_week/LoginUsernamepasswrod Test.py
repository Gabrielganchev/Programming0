import time

print ("Welcome to Test login fucntio of a program")
time.sleep(2)
print ("Enjoy")
time.sleep(0.5)

username = (input("Type Username Please").lower())#using    . lower() for less code in the if's 
if len(username) >3 and username=="gabriel": 
    time.sleep(1)
    print("Valid username")
else:
    time.sleep(1)
    print("Username must be more the 3 digits  or letters")
    
time.sleep(1)

password = (input ("Type Password Please ").lower())
time.sleep(1)
if len(password) >3  and password == "1234suzy":
    time.sleep(1)
    print ("Valid password")
else:
    time.sleep(1)
    print ("Password must be more then 3 digits or letters")
    exit

"""
# login username

#individual one by one  on the next part that is mixed together

if username == "gabriel":
    print ("Welcome Gabriel to your account")
else :
    print("User name not found")




#password login

aif password == "1234suzy":      #<---- is possible to make another function for  more datebase , but will keep it simple for now
    print ("thats the right passwrod")
else:
    print("The password is wrong")



"""

#both in one if
# def login()
if password == "1234suzy" and username == "gabriel":
    time.sleep(1)
    print("Procesing")
    time.sleep(0.5)
    
    print("Welcome Gabriel ")
    
    #return ("welcome Gabriel")
else :
    time.sleep(1)
    print(" Username or Password are wrong")
    time.sleep(0.5)
    print("Please try again")
    exit
    #return ("Wrong Username or password  Try again")\
    

    
