
#LAB3, Lincoln Center Bookstore
#July 23, 2022

#Obtain all user inputs
print("Welcome to the Lincoln Center Bookstore")
fname = input ("Enter your first name : ")
#Cervantes
numCervantesStr = input("Enter number of Cervantes books : ")
numCervantes    = int(numCervantesStr)
totalCervantes  = numCervantes *41.25
###Calculate tax at the end totalCtax = (numCervantes *41.25) + (totalCervantes *.10)
##ITWORKS_print("Tax",(totalCervantes *.10))
             
#Homer
numHomerStr     =input("Enter number of Homer books : ")
numHomer        =int(numHomerStr)
totalHomer      =numHomer *15.86 

#Shakespeare    
numShakStr      =input("Enter number of Shakespeare books : ")
numShak         =int(numShakStr)
totalShak       =numShak *30.50


#Compute 10% sales tax# Create a section that adds grand variables
txtotal=(totalShak*.10)+(totalHomer*.10)+(totalCervantes*.10)
gtotal=(totalCervantes + totalHomer + totalShak)


#Quantity, Total+Tax per a line
famount =int(gtotal+txtotal)


#print the bookstore receipt
print()
print("------------------------------------")

print("Customer: ", fname)
print("------------------------------------")
print("Item      Number      Price")
print("Cervantes      ", numCervantes , "   ", format(totalCervantes,  ",.2f"))
print("Homer          ",numHomer     ,"     ", format(totalHomer,      ",.2f"))
print("Shakespeare     ",numShak      ,"    ",format(totalShak,       ",.2f"))
print("--------------------------------------------------------------------------")
print("Tax Rate = 10%,  Amount Due inc.tax is below ")
print("Amount Due  $", int(gtotal + txtotal))
print("------------------------------------")
askpayStr = input("How much would you like to pay?:   ")
askpay =int(askpayStr)
print("------------------------------------")
print("Thank for shopping with us", fname)
print("BALANCE  $", int(famount-askpay))


