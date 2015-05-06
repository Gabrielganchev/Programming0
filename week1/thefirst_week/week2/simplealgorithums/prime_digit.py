n = int(input("Enter n: "))

digits = []
while n != 0:
    digit = n % 10
    digits = [digit] + digits
    n = n // 10
has_simple_digit = False
for digit in digits:
    if digit in [2, 3, 5, 7]:
        has_simple_digit = True
        break
if has_simple_digit:
    print("At least one prime digit found")
else:
    print("Chuck Norris can not fail")
