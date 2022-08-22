#Nicholas Clarke
#Aug 1, 2022
#Lab 4

# at least one if else statement
# constant variable
# prudent coding methods

#Fordham Airlines:
# purchase flights
# calculating how much the customer owes
# taking payment
# calculating change
# Flight time(1): daytime, 5AM, 0500Hrs,/Departure-Arrival\ 7PM, 1900Hrs
# Flight time(2): nightime, 7PM, /Departure-Arrival\1900HRS, 5AM, 0500Hrs
# Destinations: Chicago, Miami, Portland
# Types of Tickets: weekday, weekend (WD, WE)

print(u"\u2708            \u2708                 \u2708")
print(" Welcome to Fordham Airlines!")
print()
print(" Airline of the Empire State")
print(u"\u2708            \u2708                 \u2708")
print()
#o Prompt for user input of destination (use airport codes, CHIG,MIA,PTLD)
print()
print("It's an excellent time to travel, please inform of us your destination")
print()
print("CHICAGO = CHIG    MIAMI = MIA      PORTLAND = PTLD    USE CODES FOR PORTAL ENTRY")
#
print()
DEST= print(input(" What is your destination: "))
print()
##if 'CHIG' in DEST:
##    print("CHICAGO")
##elif 'MIA' = DEST:
##    print("MIAMI")
##elif 'PTLD'= DEST
##    print("PORTLAND")
#if 'MIA' in DEST:
    #printprint("Out of Carrier System")


      #use a list, or if else statement for CHIG, MIA, PTLD
      #else = Unfortunately, this is out of carrier system

print()
print(u"\u2708            \u2708                 \u2708")
print()
#o Prompt the user input of desired time to travel
print("Fordham Airlines offers DAYTIME & NIGHTIME flights")
S = input("ENTER your desired time of travel (DAYTIME, OR NIGHTIME):   ")
print()
print(u"\u2708            \u2708                 \u2708")
print()
print("TICKETS: $129: WEEKLY RATE")
print()
if 'DAYTIME' in S:
    print("If you selected DAYTIME, YOUR DEPARTURE is 5AM, ARRIVAL IS 7PM")
else:
    print("NIGHTIME DEPARTS AT 7PM, ARRIVES FOR 5AM")
    print()
D = input("Would you prefer to travel on WEEKENDS, or WEEKDAYS?:   ")
print()
if 'WEEKENDS' in D:
    print("Weekends - CONFIRMED")
else:
    print("Weekdays - CONFIRMED")
print()
print(u"\u2708            \u2708                 \u2708")
print()

##if SUN == 'DAYTIME'
##    print("DAYTIME")
##else:
##    print("NIGHTIME")
print()
print(u"\u2708            \u2708                 \u2708")

    #o Produce/Report price per ticket of specified type
if 'WEEKENDS' in D:
    print("Weekend tickets will cost $140")
else:
    print("Weekly Rate is $129")

print()

CT = int(input("How many tickets would you like:   "))
print()
#o Compute and display the total amount due
print()
print(u"\u2708            \u2708                 \u2708")
print()
if 'WEEKENDS' in D:
  T1 = print(CT*140)
else:
   T2 = print(CT*129)

#o Prompt the user to enter amount willing to pay; if less than<amt report
#insufficient funds or payment, order has been cancelled, exit

PY = int(input("How much would you like to pay?:   "))
               
print()
if 'WEEKENDS' in D:
    print(int(T1-PY))
else:
    print(int(T2-PY))

    
#oDisplay change and confirm the order has been placed


print()
print(u"\u2708            \u2708                 \u2708")
print("SAFE TRAVELS & THANK YOU FOR FLYING FORDHAM AIRLINES")
print(u"\u2708            \u2708                 \u2708")
