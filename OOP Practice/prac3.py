
import random

'''
class Human():
    def __init__(self,name,HealthStatus,age):
        self.name=name
        self.age = age
        self.HealthStatus = HealthStatus


HumanObject = Human(name,age,HealthStatus)
'''

age = 0
health = 100
air = 50
water = 50
food = 50

print('Age:', age, 'Health:', health, 'Air:',
      air, 'Water:', water, 'Food:', food)


   # human needs air,water,food to live
def KeepHumanAlive(air,water,food):
        # so we charging resources
        # giving him air,water,food
        
    for i in range(0, 100):
        newAir = random.randrange(0, 10)
        air = air + newAir
        print("Air is : ", air)
        newWater = random.randrange(2, 8)
        water = water+newWater
        print("\n Water is : ", water)
        newFood = random.randrange(0, 10)
        food = food+newFood
        print("\n food is : ", food)

            # He needs to grow
        humanAir = random.randrange(8, 10)
        print("human Air is : ", humanAir)
        humanFood = random.randrange(0, 10)
        print("human Food is : ", humanFood)
        humanWater = random.randrange(6, 8)
        print("humanWater is : ", humanWater)

        print("---------------------------")
        print("humanAir is : ", humanAir)
        print("\n humanFood is : ", humanFood)
        print("\n humanWater is : ", humanWater)

            # Reducing Sources
        air = air - humanAir
        food = food-humanFood
        water = water - humanWater

        killingHim()

        age = i+1
        print("age is : ", age)
        input("press inter ...")

        # Good Situation For health
    while (air >= 5 or air <= 10):
        while (food is True):
            while (water >= 3 or water <= 5):
                age = age - 1
                health = health + 2
                print("---------------------------")
                print("Congragations ! GOOD HEALTH")
                print("---------------------------")

def killingHim(air, water, food, disease):
    disease = random.randrange(0, 1)
    if disease == 1:
        health = -50
        print("He is Sick!")
    else:
        pass
    
    if air == 0:
        health = 0
    if air > 1 and air < 3:
        health = -20
    else:
        if air > 3 and air <5:
            health = -10

    if food > 1 and food < 3:
        health = -20
    else:
        if food > 3 and food < 5:
            health = -10

    if water > 1 and water < 3:
        health = -20
    if water > 3 and water < 5:
        health = -10
a = input()

while(health > 0 or age < 10):
    KeepHumanAlive()
    killingHim()
