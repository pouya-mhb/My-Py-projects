
class Circle():
    pi = 3.14 

    #intial radius 
    def __init__(self,r):
        self.r=r
    #create the method of calculating area of circle    
    def area (self):
        return self.r*self.r*Circle.pi
    #defining new radius and call it
    def setRadius (self,newR):
        self.r=newR

#create Circle object and call the first radius
CircleObject = Circle(100)

#call new radius here 
CircleObject.setRadius(1000)

print(CircleObject)
print(CircleObject.area)
print(CircleObject.area())