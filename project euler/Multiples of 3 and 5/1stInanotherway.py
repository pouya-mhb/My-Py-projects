sum = 0
for number in range (1,1000):
    if number % 3 == 0 or number % 5 == 0:
        print(number)
        #print ("zarib okeye !")
        sum = sum + number

print ("sum is : " , sum)
