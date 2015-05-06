#обемът volume

import math  #because logic 



def fill_tetrahedron():
    a=int(input("number for a"))#fancy

    volume =((a**3)/(6*(math.sqrt(2)))/1000)
    volume=round(volume, 2)#week sorcery
    print(volume,"liters of water")
    return 
fill_tetrahedron()
