# A class for dog informations 

dogsName = []
dogsBreed = []
dogsColor = []
dogsSize = []
dogsInformation = [dogsName, dogsBreed,
                   dogsColor, dogsSize]

#Create the class 
class Dog (): 

    #methods 
    # init method for intialization and attributes in ()
    def __init__(self, dogBreed, name, dogColor, dogSize):

        # self refers to itself (the class)
        # sth = self.atrribute
        self.dogBreed = dogBreed
        self.name=name
        self.dogColor=dogColor
        self.dogSize=dogSize

'''
    def barking (self,sound):
        self.sound=sound
        print("woof .. woofh ") 
'''

n = int(input("How many Dogs ? : "))

for i in range (0,n):

    a = input("breed : ",)
    b = input("name : ")
    c = input("dogColor : ")
    d = input("size : ")
    
    dogObject = Dog(dogBreed=a, name=b, dogColor=c, dogSize=d)

    dogsBreed.append(dogObject.dogBreed)
    dogsName.append(dogObject.name)
    dogsColor.append(dogObject.dogColor)
    dogsSize.append(dogObject.dogSize)
    

#myDog = Dog(dogBreed='labrador', name='jakie', dogColor='golden', dogSize='big') #objects
#myFriendDog = Dog(dogBreed='huskie', name='jousef',dogColor='balck', dogSize='small')


print(type(Dog))
print("dogsBreed : ", dogsBreed,'\n'
      "dogsName  : ", dogsName,'\n'
      "dogsSize  : ", dogsSize,'\n'
      "dogsColor : ", dogsColor)

#for i in dogsInformation:
    #print(i)

    
 # calling like object.attributes
'''
print("my dog information : " ,myDog.dogBreed,myDog.name,myDog.dogColor,myDog.dogSize)
print("my dad's dog information : ", myDadsDog.dogBreed, myDadsDog.name,
    myDadsDog.dogColor, myDadsDog.dogSize) '''

