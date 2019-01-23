import random
'''
numbersArray = []
for i in range (0,50):
    numbersArray.append(random.randrange(0,1000))
print (numbersArray,'\n')
x = int(input("please enter the numbers you want to be founded : "))
for i in numbersArray:
    if i == x:
        print("element found " , i)
print ('element not found!')
'''

NumArray = []
arraySize = int(input("please enter the size of array : "))
randomRange = int(input("please enter range of random numbers (start from 0): "))
for i in range (0,arraySize):
    numbers = random.randint(0,randomRange)
    NumArray.append(numbers)

def Lsearch ():
    for i in NumArray:
        if i == X:
            return i
    print("element not found!!")

'''
    for j in NumArray:
        if j == X:
            return j
    #return 0
    print("element not found!!")
'''

print(NumArray)
X = int(input("please enter the numbers you want to find : "))
print ("element founded at : " , Lsearch())


'''
NumArray = []

for i in range (0,100):
    numbers = random.randrange(0,100)
    NumArray.append(numbers)


for element in NumArray:
    if NumArray[element] == X:
        print (element)
    print("element not found!!")

X = input("please enter the numbers you want to be founded : ")
'''
