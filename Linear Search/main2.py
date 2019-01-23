import random

NumArray = []
arraySize = int(input("please enter the size of array : "))
randomRange = int(input("please enter range of random numbers (start from 0): "))

for i in range (0,arraySize):
    randNumbers = random.randrange(0,randomRange)
    NumArray.append(randNumbers)
print(NumArray)

def Lsearch (NumArray,x):
    for j in range (0,arraySize):
        if NumArray[j] == X:
            return j
    print("element not found!!")


X = int(input("please enter the numbers you want to find : "))
if (True):
    print ("element" , "founded at : " , Lsearch(NumArray,X))
