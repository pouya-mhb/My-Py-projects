'''
by considering the terms in Fibonacci sequence
whose values  do not exceed four million ,
find the sum of the even-valued terms.
'''
import time
start_time = time.time()

def fibo(n):
    if n == 1 :
        return 1
    if n == 2 :
        return 1
    else :
        return fibo(n-2) + fibo (n-1)
'''
def ifEven (m):
    if m % 2 == 0:
        return True
    else :
        return False
'''

count = 0
sum = 0
n = 0

FiboList = []
sumList = []
#while (sum < 4*10**6):
while (True):
    #for i in range (1,39):
    n = n + 1
    count = count + 1
        #print (count ,  ' : ', fibo(i) , "     ","sum : " , sum) // this line print all Fibonacci sequence
    if (fibo(n) %2 == 0):
        FiboList.append(fibo(n))
        sum = sum + fibo(n)
        print (count ,  ' : ', fibo(n) , "     ","sum : " , sum) #this line shows the even fibos
        if sum > 4*10**6:
           break
        sumList.append(sum)
print("Fibo List : " , FiboList)
print ("sum List : " , sumList)
print ("--- %s seconds ---" % (time.time() - start_time))
