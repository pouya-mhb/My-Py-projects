# write a program wich :
# A: have randome numbers and use them in a list and use the list in daraje 2
# B: fill the list with ordered numbers 
import random

#a = int(input("please enter A: "))
#b = int(input("please enter B : "))
#c = int(input("please enter c : "))

    
def RandomMHB ():
    for randNumber in range(0, 3):
        randNumber = random.randint(0, 9)
        print(randNumber)
        randNumberLIst.append(randNumber)
    print ("The randNumberLIst : " , randNumberLIst)

randNumberLIst = []

def D2(x, y, z):
     delta = y**2 - 4*x*z
     X1 = ((-y) + (delta**(1/2)))/2*x
     X2 = ((-y) - (delta**(1/2)))/2*x
     print("delta : ", delta)
     if (delta < 0):
            print("Delta is less than 0 , no answer exist.")
     elif (delta == 0):
         print("x1=x2=", X1)
     else:
         print("X1: ", X1, "\nX2:", X2)

RandomMHB()

a = randNumberLIst[0]
b = randNumberLIst[1]
c = randNumberLIst[2]

D2(a,b,c)
