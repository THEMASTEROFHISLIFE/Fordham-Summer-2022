#Nicholas Clarke
#HW6

##1) The number of uppercase letters in the file
##2) The number of lowercase letters in the file
##3) The number of digits in the file
##4) The number of whitespace characters in the file


#1. Use if statement, if A-Z
#2. Use if statement, if a-z
#3. Use if 0-9
#4. Use if " "

#print int amount how?

#import documentg.txt

##open('documentg.txt') as f:
##    w, h = [int(x) for x in next(f).split()]
##    array = [[int(x) for x in line.split()] for line in f]
##
##with open('/home/nicholas.documentg.txt', 'r') as inp:
##    y = inp.read().upper()
###with  open('/home/nicholas.documentg.txt', 'r') as out:
##    out.write(y)

import documentg.txt

read.documentg.txt('documentg.txt', 'r')

AZ = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','X','Z']
az=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','x','z']
num = ['0','1','2','3','4','5','6','7','8','9']
Space = [" "]

if documentg.txt== AZ:
    print(' ')
if documentg.txt==az:
    print(' ')
if documentg.txt == num:
    print(int(' '))
if documentg.txt== Space:
    print(" ")
else:
    print("not found")
