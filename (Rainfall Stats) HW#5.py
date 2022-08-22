#July 23, 2022
#Nicholas Clarke
#HW_5


#Rainfall Statistics

#Pseudocode
##A program that lets the user enter the total rainfall
##Use an int/input/print module
###FOR EACH of 12 months into a list
#Calculate and display total rainfall for the year
##The average monthly rainfall
#months with highest and lowest amounts
##all done, completion at end



print("WELCOME USER, I will you assist in calculating Rainfall")

print("----------------------------------------------------")

#per month prompt

print()
    
months=[]
months=['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']

##JANx= input("What was the rainfall for month of JAN :   ")
##JAN= int(JANx)
##FEBx=input("What was the rainfall for month of FEB:    ")
##FEB = int(FEBx)
##ravg=int(JAN+FEB)/int(months)


print("These are the months of the year", months)


print()
print("Please provide the rainfall to nearest decimal using the units, INCHES")

print()

JANStr = input("What was the recorded rainfall for JAN:   ")
JAN    = float(JANStr)
print()
FEBStr = input("What was the recorded rainfall for FEB:   ")
FEB    = float(FEBStr)
print()
MARStr = input("What was the recorded rainfall for MAR:   ")
MAR    = float(MARStr)
print()
APRStr = input("What was the recorded rainfall for APR:   ")
APR    = float(APRStr)
print()
MAYStr = input("What was the recorded rainfall for MAY:   ")
MAY    = float(MAYStr)
print()
JUNStr = input("What was the recorded rainfall for JUN:   ")
JUN    = float(JUNStr)
print()
JULStr = input("What was the recorded rainfall for JUL:   ")
JUL    = float(JULStr)
print()
AUGStr = input("What was the recorded rainfall for AUG:   ")
AUG    = float(AUGStr)
print()
SEPStr = input("What was the recorded rainfall for SEP:   ")
SEP    = float(SEPStr)
print()
OCTStr = input("What was the recorded rainfall for OCT:   ")
OCT    = float(OCTStr)
print()
NOVStr = input("What was the recorded rainfall for NOV:   ")
NOV    = float(NOVStr)
print()
DECStr = input("What was the recorded rainfall for DEC:   ")
DEC    = float(DECStr)


##@PROF: Is there a way to have the variable e.g. JAN, FEB, MAR to be called in tsumyr? A
###As in the user inputs per a month and the list of months get their value via that method?
####RESOLVED!
print()
print("---------------------------------------------------------")
 
#total sum year
tsumyr= (JAN+FEB+MAR+APR+MAY+JUN+JUL+AUG+SEP+OCT+NOV+DEC)
print("The total yearly rainfall was", tsumyr); print("INCHES")

print()
print()

#avg month

avgmonth= (tsumyr/12)
print("The annual average was", avgmonth); print("INCHES")

print()

print()
def main():
    
#sort method for months with highest and lowest
    months= [JAN,FEB,MAR,APR,MAY,JUN,JUL,AUG,SEP,OCT,NOV,DEC]
    #print('Months sorted in ascending order:', months)
   # months.sort()
    print()
    print('The month with the highest rainfall in order was', max(months))
    print()
    print('The month with the lowest rainfall in order was', min(months))
main()    

    #month max
#if max(months) is float
   #else:min(months) 

    #month minimum


print()






print("ALL DONE!")
