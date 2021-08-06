number = int(input("please enter a number : "))

stringNumber = str(number)
stringNumberArray=[]
for i in stringNumber:
    stringNumberArray.append(i)

l = len(stringNumberArray)
print ("l=",l)

m = int(l/2)
print ("m=",m)

if l%2==0:
    for i in range (0,m):
        for j in range (m,l):
            if stringNumberArray[m-j]==stringNumberArray[m+i] :
                print ("yes")
                print(stringNumberArray[m-i]==stringNumberArray[m+i])
            else :
                print("No")

else :
    for i in range (0,m):
        if stringNumberArray[m-1]==stringNumberArray[m+1]:
            print ("Yes")
        else :
            print ("NO")