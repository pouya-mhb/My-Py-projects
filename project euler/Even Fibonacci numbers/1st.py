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
        return 2
    else :
        return fibo(n-2) + fibo (n-1)

def ifEven (m):
    if m % 2 == 0:
        return True
    else :
        return False

count = 0
sum = 0
#while (fibo(i) <= 4000000):
for i in range (1,39):
    count = count + 1
    #print (count ,  ' : ', fibo(i) , "     ","sum : " , sum) // this line print all Fibonacci sequence
    if ifEven(fibo(i)):
        sum = sum + fibo(i)
        print (count ,  ' : ', fibo(i) , "     ","sum : " , sum) #this line shows the even fibos
        if sum > 4*10**6 :
            break
print ("--- %s seconds ---" % (time.time() - start_time))
