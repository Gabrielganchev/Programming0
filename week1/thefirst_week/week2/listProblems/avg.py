n = int(input("Enter n: "))

start = 0
numbers = []
while start < n:
    number = int(input())
    
    numbers = numbers + [number]
    start += 1

    
total_sum = 0
count_numbers = len(numbers)
for number in numbers:
    total_sum += number
    
avg = total_sum / count_numbers

print("Avg is: " , (avg))

