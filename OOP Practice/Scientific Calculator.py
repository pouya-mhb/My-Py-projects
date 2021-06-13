
numberList = []
oprationList = []
simpleOpratorList = [sum,subtract,multiply,divide]
scientificOpratorList = []

class SimpleCalculator():
    def __sum__(self, numberinList):
        for numberinList in numberList:
            sum = numberinList + numberinList
        return sum

    def __subtract__(self, numberinList):
        for numberinList in numberList:
            sub = numberinList - numberinList
        return sub

    def __multiply__(self, numberinList):
        for numberinList in numberList:
            mul = numberinList * numberinList
        return mul

    def __divide__(self, numberinList):
        for numberinList in numberList:
            div = numberinList / numberinList
        return div


def mhbCalculator ():
    #while numbers in list is less than 2 , get numbers from user
    while(len(numberList)<2):
        number = float(input("Number : "))
        numberList.append(number)
    
    # now we use if statement .. after stable version of python 3.10 will change it to match case
    

mhbCalculator()
