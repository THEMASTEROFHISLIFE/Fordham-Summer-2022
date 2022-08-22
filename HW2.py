#Nicholas Clarke
#HW2 #13 Planting Grapevines (Programming Exercises)
#July 22, 2022


#needs to know how many grapevines to plant in a row
#length of a future row

#V=R-2RES 
#Units feet
#V is the number of grapevines thta will fit in the row
#R is the length of the row, in feet
#E is the amount of space, in feet, used by an end-post assembly
#S is the space between vines, feet
##V= NUM_GP_ROW
##R= LEN_ROW
##E= SP_EPA
##S= SP_V

#User Input Prompts
#Length of the row, in feet (r)
#The amount of space used by an end post assembly, in feet(e)
#The amount of space between the vines, in feet (s)

answer = input ("Hello, I understand you need help with your grapevines ?:  " )


def main():
    
    if answer == ("yes"):
     print("Copy that")
    if answer == ("y"):
     print("Wow, nice!")
    if answer == ("Y"):
     print("Let's do this!")
    if answer == "Yes":
     print("Sure thing!")
    if answer == "YES":
     print("Awesome, I'm glad to help!")
    elif answer == "no":
     print("Alright")
    elif answer == "No":
     print("Ok, have a nice day")
    elif answer == "NO":
     print("No worries!")
    elif answer == "N":
     print("OK")
    elif answer == "n":
     print("Gotcha!")
    else: print ("********")
main()



    #user input prompts
#print(input("Hello, I understand you need help with your grapevines ?" , ))

R = float(input("Tell me what the length of the row is in feet?:   "))
print()
E = float(input("What is the amount of space in feet by the end post assembly?:  "))
print()
S = float(input("What is the space between the vines, in feet?:    "))
print()
import math
V= R-(2*(E*S))
print("The number of grapevines that will fit in the row", V)
print()
print("----------------------------------------------------------------------")
print("ALL DONE! HAVE A GREAT DAY")


