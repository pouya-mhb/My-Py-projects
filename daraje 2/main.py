#a = int(input("please enter A: "))
##b = int(input("please enter B : "))
#c = int(input("please enter c : "))

#delta = b**2 - 4*a*c

#x1 = ((-b) + (delta**(1/2)))/2*a
#x2 = ((-b) - (delta**(1/2)))/2*a

#print ("delta : " , delta , "\n x1 : " , x1 , "\n x2: " , x2)


a = int(input("please enter A: "))
b = int(input("please enter B : "))
c = int(input("please enter c : "))


def CE(x, y, z):
    delta = y**2 - 4*x*z
    X1 = ((-y) + (delta**(1/2)))/2*x
    X2 = ((-y) - (delta**(1/2)))/2*x

    if (delta < 0):
        print("Delta is less than 0 , no answer exist.")
    else:
        print("delta : ", delta)
        print("X1: ", X1, "\nX2:", X2)


CE(a, b, c)
