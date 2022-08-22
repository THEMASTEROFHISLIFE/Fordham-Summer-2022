#Nicholas Clarke
# Lab 6
#Aug 3, 2022

#Dictionaries
#Course Number(key!), Room Number(value!)
#Course Number(key!), Instructor(value!)
#Course Number(key!), Meeting Time(value!)

Room = {'CS1O1':'3004','CS102':'4501','CS103':'6755','NT110':'1244', 'CM241':'1411'}

Instructor = {'CS101':'HAYNES','CS102':'ALVARADO','CS103':'RICH','NT110':'BURKE','CM241':'LEE'}

Time = {'CS101':'0800AM','CS102':'0900AM','CS103':'1000AM','NT110':'1100AM','CM241':'0100PM'}

#Enter a course number
#Display course's number, instructor, and time
# ask user multiple times Y/N to exit

#get
# action = room.get
# acttwo = Instructor.get
# acttime = Time.get
#len


    
print("COURSES: CS101,CS102, CS103, NT110, CM241")
print()
print()

#def main():
    #while True:
Choice = input("Enter the course number of desired course:  ")

if 'CS101'== Choice:
    print ("3004:HAYNES:0800AM")
elif 'CS102' == Choice:
     print("4501:ALVARADO:0900AM")
elif 'CS103' == Choice:
    print("6755:RICH:1000AM")
elif 'NT110' == Choice:
    print("1244:BURKE:1100AM")
elif 'CM241' == Choice:
    print("1411:LEE:0100PM")
else:
    print("NO COURSE FOUND!")
print()
print("RE-RUN CODE DUE TO 404")
print("THANK YOU!")
#ChoiceB = input("Enter the course number of desired course:  ")
print()
##    while True:
##     input("Would like to continue Y/N?: ")
##     input = 'Y'
##    else:
##        print("QUIT")


#main()
