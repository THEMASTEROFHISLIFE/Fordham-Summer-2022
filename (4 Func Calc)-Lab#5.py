# Nicholas Clarke
# Aug 2, 2022
# Lab 5

# 4 function calculator only integers/non float
# Addition, Subtraction, Multiplication, Division
print(" +      -      x    /  ")
print()
print(" I'm a 4-function calculator")
print()
import math




#def add(var,varx):
    #return var + varx

def addition(A,B):
    return A+B
def subtract(A,B):
    return A-B
def multiply(A,B):
    return A*B
def divide (A,B):
    return A/B

print(" What is your desired operation")
print("ADD.addition")
print("SUBT.substract")
print("MULT.multiply")
print("DIVD.divide")

selection = input("Select (ADD/SUBT/MULT/DIVD):")

int_1 =float(input("INPUT FIRST INTEGER:"))
int_2 = float(input("INPUT SECOND INTEGER:"))


if selection=='ADD':
    print(int_1,"+",int_2,"=",addition(int_1,int_2))

elif selection == 'SUBT':
    print(int_1,"-",int_2,"=",subtract(int_1,int_2))

elif selection == 'MULT':
    print(int_1,'*',int_2, "=",multiply(int_1,int_2))

elif selection == 'DIVD':
    print(int_1,'/',int_2,"=",divide(int_1,int_2))
else:
    print("INVALID ENTRY")
    
#function = input("Enter equation:    ")
#if '+' in function:
 #   print((sum ))

    #if '*' in function:
     #   print("")
#loops for inputs...sigh


##for num in range(0, n+1, 1):
  ##  sum = sum+num
##print(sum=)
