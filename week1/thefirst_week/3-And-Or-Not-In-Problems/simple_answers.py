while True:
    text = input("Say what? ")
    if "hello" in text or "Hello" in text:
        print("Hello there, good stranger!")
    elif "how are you?" in text:
        print("I am fine, thanks. How are you?")
    elif "feelings" in text:
        print("I am a machine. I have no feelings")
    elif "age" in text:
        print("I have no age. but i will die like the rest")
    elif "rest" in text:
        print("i dont know,but time will tell both of us wont it ? ")
    elif "real" in text:
        print("can you prove you are real?")
    elif "noone can" in text or "can" in text :
        print("was such a plasuare my friend")
        
        
    else:
        print("Sorry, I don't understan you. Try hello, feelings or age")
