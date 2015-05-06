books = ["Learn You a Haskell",#index starts from 0 
         "The Healthy Programmer",
         "Code Complete",
         "The Pragmatic Programmer",
         "Pro Git",
         "Introduction to Algorithms",
         "Concrete Mathematics"]
index = 0
end = len(books)

while index < end: #eto zashto ne printi poslednata ako e len(books)-1
    book = books[index]
    print(book)

    index+=1
   
