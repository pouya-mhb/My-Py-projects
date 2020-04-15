#import random

import matplotlib.pyplot as plt 

'''
def RandomMHB ():
    for randNumber in range(0, 3):
        randNumber = random.randint(0, 9)
        print(randNumber)
        randNumberLIst.append(randNumber)
    print ("The randNumberLIst : " , randNumberLIst)

randNumberLIst = []
'''

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
    

#RandomMHB()

#a = randNumberLIst[0]
#b = randNumberLIst[1]
#c = randNumberLIst[2]

def countNumb ():
    for i in range (0,5):
        a = i
        for j in range (0,5):
            b = j
            for k in range (0,5):
                c=k 
                print("a:", a, "b:", b, "c:", c)
                D2(a,b,c)
                #plt.plot(D2(a, b, c))
                #plt.plot(a,b,c)

countNumb()
#plt.show()