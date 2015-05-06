def count_words(words):
    result = {}
    
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return result


print(count_words(input("Write a sentance").split())) # my logic , better way

# testing the logic  ///.split()///
#welcome = str("hello fucking world")
#print (welcome)
#welcometest = str("what ever is it ever").split()
#print(welcometest)

#words = welcome.split()
 #   print (words)


#number_of_words = len(words)
 #   print(number_of_words)











"""def count_words(words):
    result = {}
    

    for word in words:
        if word in result:
            result[word] +=1
        else:
            result[word]=1

    return result"""

