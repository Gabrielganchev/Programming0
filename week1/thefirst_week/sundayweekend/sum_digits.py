n = int(input("Enter number: "))
total_sum = 0
while n != 0:

    digit = n % 10#kombinaciq ot simvoli ot zad napret
    total_sum += digit
    n = n // 10

print("Sum of digits is: " + str(total_sum))
