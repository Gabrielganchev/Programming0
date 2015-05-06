person = {
    "name" : "Gabriel",
    "age" : 25,
    "hobbies": ["Programming","Windsurfing","Working out"],
    }
print(person["age"],"The age")
person["age"] +=1
#age went one level up
print(person["age"],"new age")


#adding one more hobby
person["hobbies"]  += ["Mountain climbing"]

print(person["hobbies"])

if "friends" not in person :
    # adds friends list
    person["friends"] =["ivo", "maria"]

for key in person:
    value = person [key]
    print (key, value ,"<---- last print")
