import random

money = []
for i in range (0,50):
    money.append(100)
print (money)


for sou in range (0,50):
    des = random.randint(0,50)


for beshkan in (0,5):
    money[sou] -= 1
    print ("$ src : " , money[sou])
    money[des] += 1
    print ("$ des: " , money[des])
    print ("sou : " , sou , "-->" , "Des : " , des)

print (money)
