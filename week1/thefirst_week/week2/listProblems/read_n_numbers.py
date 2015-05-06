n = int(input("Enter count of numbers: "))


count = 1
numbers = []

while count <= n:
    number = [int(input("Enter number: "))] # ako maxnem int vuvejda chislata kato str

    numbers = numbers + number # malko remake ot men
    

    count += 1

print(numbers)
