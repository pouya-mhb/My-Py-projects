#number = input ("Please enter a number to see if it's prime or not: ")
import time
start_time = time.time()

number = 52

print ("the number is : ",number)

aval = True
for i in range (2,number):
    if number % i == 0:
        aval = False

if aval :
    print ("This is a prime number.")
else :
    print ("The number is not prime.")
    
print ("--- %s seconds ---" % (time.time() - start_time))
