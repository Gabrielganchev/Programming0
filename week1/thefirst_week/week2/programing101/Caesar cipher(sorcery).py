
#made in python3.4
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

key = 3
plaintext = "I WANT TO BE IN THE COURSE OF HACKBULGARIA"

# криптоваме
ciphertext = ""
for c in plaintext.upper():
    if c.isalpha(): ciphertext += I2L[ (L2I[c] + key)%26 ]#very ugly sorcery
    else: ciphertext += c

# декриптоваме
plaintext2 = ""
for c in ciphertext.upper():
    if c.isalpha(): plaintext2 += I2L[ (L2I[c] - key)%26 ]#more ugly sorcery
    else: plaintext2 += c

print (plaintext)
print (ciphertext)
print (plaintext2)
