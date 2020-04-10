# OOP 
'''
    # Object - attributes and behaviour
    # Class - blueprint or entity of objects
    # Constructor
    # Inheritance
'''

# Class without parameterized constructor and with default values
class Bird():
    # Constructor
    def __init__(self):
        self.height = 1.5
        self.weight = 0.5
        self.feather_weight = 0.2
        self.color = "black"
        self.beak = True
        self.name = "Bird"


    def canfly(self):
        # Check wheter a bird can fly or not
        half_weight = self.weight / 2
        if(self.feather_weight >= half_weight):
            print("Cannot Fly")
        else:
            print("Can fly")  


crow = Bird()

crow.canfly()

class CarniBirds(Bird):
    # Constructor
    def __init__(self):
        Bird.__init__(self)
        self.hasSharpClaws = True
        self.power = 200 # RPM
        self.speed = 120 # Km / hr
        self.eyesight = 8 # Km vision

    def canHunt(self):
        if(self.power > 150 and self.speed >= 100 and self.eyesight > 5):
            print("It can hunt any species")
        else:
            print("It cannot hunt")
    
    def birdDeatils(self):
        print(f"{self.name}")


eagle = CarniBirds()
eagle.birdDeatils()
eagle.name = "Eagle"
eagle.height = 2.3
eagle.weight = 7

eagle.birdDeatils()