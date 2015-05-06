import time
print("Welcome")
time.sleep(1.5)
print("please enter username")
username=input()
if username == "Gabriel":
    print("Correct please wait")
    time.sleep(1.5)
    print("please enter password")
    password=input()
    if password == "1234gabriel":
        print("please wait")
        time.sleep(1.5)
        
        print("that is corrent this is the paswwrod")


if username != "Gabriel":
    print("wront username")
    time.sleep(1)
    exit
