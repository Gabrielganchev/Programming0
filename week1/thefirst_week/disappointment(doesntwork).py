import math

water = int(input("water:"))
num = int(input(" num for tetrahedrons:"))
tetrahedrons = []
for i in range(int(num)):
    edge = int(input("edges for tetrahedron:"))
    tetrahedrons.append(edge)
    tetrahedrons.sort()



def fill_tetrahedron(num):
    volume =((num**3)/(6*(math.sqrt(2)))/1000)
    volume=round(volume, 2)

def tetrahedron_filled(tetrahedrons, water):
    for number in tetrahedrons:
        value = fill_tetrahedron(number)
        
        water = int(water) - value
        full_tetrahedrons = 0
        full_tetrahedrons += 1
    return full_tetrahedrons

print(tetrahedron_filled(tetrahedrons, water))



