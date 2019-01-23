import time
start_time = time.time()

def isPrime(number):
    aval = True
    for i in range (2,int(number)):
        #use number/2 or number**0.5 to calculate faster 
        if inputNumber % i == 0:
            aval = False
            if (inputNumber == 0 or inputNumber == 1):
                aval = False
    return aval

inputNumber = int(input("Please enter a number to see if it's prime or not: "))
if isPrime(inputNumber):
    print (inputNumber,"is a prime number.\n")
else :
    print (inputNumber,"is not a prime number.\n")

print ("--- %s seconds ---" % (time.time() - start_time))
