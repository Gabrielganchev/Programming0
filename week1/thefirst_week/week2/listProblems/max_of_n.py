n = int(input("Enter n: "))

start = 0
numbers = []
while start < n:
    number = int(input("numbers for "))
    numbers = numbers + [number]
    start += 1
    
s_min = numbers[0]
for number in numbers:
    if number < s_min:
        current_min = number
print(current_min)
