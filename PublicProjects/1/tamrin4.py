number = int(input("please enter a number : "))

def symNum(n):
  return str(n) == str(n)[::-1]

if (symNum(number) == True):
    print ("yes")
else :
    print ("no")