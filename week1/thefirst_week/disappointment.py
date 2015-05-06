import math

water = int(input("water:"))  #Enter the amount of water in litres
n = input("Enter the number of tetrahedrons:")
tetrahedrons = []
for i in range(int(n)):
    edge = input("Enter the edge of a tetrahedron:")
    tetrahedrons.append(int(edge))
    tetrahedrons.sort()



def fill_tetrahedron(num):
    volume = (int(num) ** 3) // (6.0 * (2 ** 0.5))
    volume_in_l = volume / 1000

def tetrahedron_filled(tetrahedrons, water):
    if water >= 0:
        for number in tetrahedrons:
            value = fill_tetrahedron(number)
            water = water - value
            full_tetrahedrons = 0
            full_tetrahedrons += 1
        return full_tetrahedrons

print (tetrahedron_filled(tetrahedrons, water))
