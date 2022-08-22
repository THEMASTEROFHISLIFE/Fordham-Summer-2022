#Nicholas Clarke
#Chapter 5, HW-4
# July 27, 2022


###TYPO in TEXTBOOK KE IS (1/2) (m v^2)

#Kinetic Energy

#KE=12mv2
#KE, Kinetic Energy
#m is the object's mass in Kg
#v is the object's velocity m/s
##write a function named kinetic_energy


###function accepts an object's mass in kg and velocity m/s as arguments

### function should return the amount of KE that the object has

### User must enter values for mass and velocity
###then calls the kinetic_energy function to get the object's energy


print("Hello, I will assist you calculating the given kinetic energy of said object")
print()
print()
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
m = float(input("What is the mass of the object in kg?:  "))
print()
print()
print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
print()
print()
v = float(input("What is the velocity of the object in m/s?:   "))
print()
print()

print("--------------------------------------------------------")


import math
KE = 0.5*(m*(v*v))
print()
print(" The KE, Kinetic Energy is:   ", KE, "joules")

print()
print("ALL DONE!")


