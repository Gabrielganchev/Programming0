pyg = 'ay'

original = input('Enter a word:')
word = original.lower()
first = word[0]
new_word = word + first + pyg

new_word =new_word[1:len(new_word)]#fun code / cuts from the first 1 string and prints to the last
if len(original) > 0 and original.isalpha(): # isalpha()  > method  gives true if the input is alphabet
    
    print (original)
else:
    print ('empty')
print (new_word)
 #piglatin test 
