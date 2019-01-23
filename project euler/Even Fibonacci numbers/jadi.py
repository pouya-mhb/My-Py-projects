def isEven(n):
    if n % 2 == 0 :
        return True
    else :
        return False

first = 1
second = 2
sum = 0
while (first < 4000000):
    if isEven(first):
        sum = sum + first
        print (first)
        new = first + second
        first = second
        second = new
print (sum)
