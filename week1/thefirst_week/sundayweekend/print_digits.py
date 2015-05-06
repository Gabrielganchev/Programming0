# Тук ползваме следната идея
# Ако имаме едно число n
# n % 10 ни дава последната цифра на това число
# n // 10 ни дава числото без последната цифра
# Ако n е само 1 цифра, n // 10 ще даде 0. Това е и условието за край на цикъла
n = int(input("Enter number: "))

while n != 0: #n not 0
    digit = n % 10 #last number 
    print(digit)
    n = n // 10
#i will look at this again in the morning
    
