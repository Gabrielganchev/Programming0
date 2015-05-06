a=int(input("Number from you "))
count = 1
even_numbers = []
while count <= a:
    number = int(input("Enter number: "))
   
    if number % 2 == 0:
        even_numbers = even_numbers + [number]
        count += 1
print("Count of evens: " ,(len(even_numbers)))#works
print("Evens are: ")
for even in even_numbers:
    print(even)

   
"""a =5
b = a +5
print(a,b,"and me ")
"""
