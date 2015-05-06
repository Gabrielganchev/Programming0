a = int(input("put number for a "))
b=1
c=0

while b<=a :
    
    
    b+=1 #  zatvarqme cikala na while
    if b%2==1: # b%2==1  === chisloto b vutre vcikala obhojda cikala i prav razdelq b na  modul i  ako ima ostatuk (==) 1  dava true i dava napred
        
        print(str(b)+"  <========== number != even" ) # !=  - not even
    elif b%2==0: # b%2==0 , nqma ostatuk i dava 0  i produljava natatuk
        print(str(b)+"<==== number is even")# printira b  kato string  kazva che e chetno
    
        c=(b%2==0)# izliza boolean stoinost za c 
        print(c)
        
