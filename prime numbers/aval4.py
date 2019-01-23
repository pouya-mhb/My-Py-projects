import time
start_time = time.time()

def isPrime(number):
    aval = True
    for i in range (2,int(number**0.5)+1):
        if number % i == 0:
            aval = False
    return aval

for i in range (1,1001):
    if isPrime(i):
        print (i,)

print ("--- %s seconds ---" % (time.time() - start_time))
