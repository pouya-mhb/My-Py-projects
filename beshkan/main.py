'''
problem :

ye otagh darim ke toosh 50 nafar adam hastan
har kodoom az ina 100 $ pool daran
har bar ke beshkan mizanim , har nafar 1$ random be yeki dg mide
age kasi poolesh t shode bood dg too bazi nist

baade ye modat chi mishe?
list e naha E money ha cheghadre?
baade chand bar pool t mishe ?

'''

import random
import time
start_time = time.time()
import matplotlib.pyplot as plt

money = []
sum1 = 0
for i in range (0,50):
    money.append(100)
    sum1 = sum1 + money[i]
print ("money List BEFORE Transaction\n" , money)


count = 0
sum2 = 0

#for beshkan in range (0,5):
#while(True):
while(count < 10000000): #beshkan ha
    #print ("---------------------------------")
    count = count + 1
    #print ("Try " , count , ":")
    for sou in range (0,50):
        des = random.randrange(0,50)
        if (sou == des):
            des = random.randrange(0,50)

        if (money[sou] == 0 or money[des] == 0):
            break
        else :
            #print ("sou : " , sou , "--->" , "des : " , des )
            money[sou] = money[sou] - 1
            #print ("money sou : " , money[sou])
            money[des] = money[des] + 1
            #print ("money des : " , money[des])
            #sum2 = sum2 + money[des] + money[sou]
             #--> WRONG PLACE

print ("---------------------------------")
print ("Number of Tries: " , count)
print ("---------------------------------")
print ("--- %s seconds ---" % (time.time() - start_time))
print ("---------------------------------")
print("sum before : " , sum1)
for i in range (0,50):
    sum2 = sum2 + money[i]
print("sum after : " , sum2)
print ("---------------------------------")
print ("money List AFTER Transaction\n" , money)


plt.scatter(range(0,50),money)
#plt.bar(range(0,50),money)
#plt.polar(range(0,50),money)
#plt.plot(range(0,50),money)
plt.xlabel('person')
plt.ylabel('mount of money')
plt.title('Transaction')
plt.show()


#randList = []
#for i in range (0,51):
#    randList.append(random.randrange(0,51))

'''
    for i in randList :
        source = randList[i] - 1
        des = randList[i] + 1
'''
#    print ("sou : " , source)
#    print ("des : " , des)
#    print ("Random List : " , randList)

#print ("people List : " , people)
