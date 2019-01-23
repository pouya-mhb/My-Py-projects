'''
if we list all the natural numbers below 10 that
are multiples of 3 and 5 , we get 3,5,6,9 .
the sum of the multiples is 23 .
find the sum of all multiples of 3 and 5 below 1000.

projecteuler.net
'''
import time
start_time = time.time()

def zarib3Or5(number):
    if number % 3 == 0 or number % 5 == 0:
        return True
    else :
        return False

evenNumbersList = []

sum = 0
for i in range (1,1001):
    if zarib3Or5(i):
        #print(i ,zarib3Or5(i))
        evenNumbersList.append(i)
        #print ("zarib okeye !")
        sum = sum + i
print(evenNumbersList)
print ("sum is : " , sum)

print ("--- %s seconds ---" % (time.time() - start_time))
