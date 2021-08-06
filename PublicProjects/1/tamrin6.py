number = int(input("How many numbers? : "))

numArray=[]

for i in range (0,number):
    n = int(input("please enter a number : "))
    numArray.append(n)
    
print(numArray)

def maximum (numArray):
  max_val = numArray[0] 
  for check in numArray: 
    if check > max_val: 
      max_val = check 
  return max_val

def minimum (numArray):
    min_val = numArray[0] 
    for check in numArray: 
        if check < min_val: 
          min_val = check 
    return min_val


def average (numArray):
    sum = 0
    for i in numArray:
        sum = sum + i
    averageNum = sum / len(numArray)
    return averageNum 

print("Maximum : ", maximum(numArray))
print("Minimum : ", minimum(numArray))
print("Average : ",average(numArray))
