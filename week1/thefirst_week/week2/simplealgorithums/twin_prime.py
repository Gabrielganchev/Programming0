p = int(input("Enter number: "))

q = p - 2
q1 = p + 2
# check for  p
is_p_prime = True
start = 2



while start < p:
    if p % start == 0:
        is_p_prime = False
        break
    start += 1

# check for  q = p - 2
is_q_prime = True
start = 2

while start < q:
    if q % start == 0:
        is_q_prime = False
        break
    start += 1

# check for q1 = p + 2

is_q1_prime = True
start = 2
while start < q1:
    if q1 % start == 0:
        is_q1_prime = False
        break
    start += 1
# end checking
if is_p_prime and (not is_q_prime) and (not is_q1_prime):
    print(str(p) + " is prime")
    print("But " + str(q) + " and " + str(q1) + " are not.")
elif is_p_prime:
    if is_q_prime:
        print(q, p)
    if is_q1_prime:
        print(p, q1)
else:
    print(str(p) + " is not prime.")
