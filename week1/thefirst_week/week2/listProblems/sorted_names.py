print("whatever")

n = int(input("Enter count of names: "))

count = 1
names = []
while count <= n:
    name = input("Enter name: ")
    names = names + [name]
    count += 1

names = sorted(names) #sorted used 
for name in names:
    print(name)
