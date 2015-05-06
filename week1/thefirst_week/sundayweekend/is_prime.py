n = int(input("Enter a number: "))

start = 2
is_prime = True
# Специален случай за 1.
if n == 1:
    is_prime = False
while start < n:
    if n % start == 0:
        is_prime = False
        break
    start = start + 1
if is_prime:
    print("It is prime")
else:
    print("It is not prime")
