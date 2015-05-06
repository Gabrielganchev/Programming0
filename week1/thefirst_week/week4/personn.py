import datetime
now = datetime.datetime.now()#abit ugly  just little bit :D 

person = {
    "first_name":input("Your first name "),
    "second_name":input("ypir second name"),
    "third_name":input("your last name "),
    "age":now.year-int(input("year that you are born")),
    }
print(person)

