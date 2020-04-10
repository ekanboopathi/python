# OOP 
'''
    # Object - attributes and behaviour
    # Class - blueprint or entity of objects
    # Constructor
    # Inheritance
'''


'''
    1. Procedure oriented
        Modules based eg:
            module modulename:
                # operations or statements

            modulename
        
            Disadvantage - a module cannot return any values
    2. Function oriented
        Function based eg:
            def func1():
                a = 12
                b = 43
                return a + b

            valu1 = func1()
            value2 = 13
            value2 = valu1 + value2 

            Disadvantage: function increase creates a problems and hard to convert to ideas to real world problem
    3. Object oriented
'''

# Class with parameterized constructor
class Bird():

    # Constructor
    def __init__(self, height, weight, feather_weight, color, beak, name):
        self.height = height
        self.weight = weight
        self.feather_weight = feather_weight
        self.color = color
        self.beak = beak
        self.name = name


    def canfly(self, weight, feathers_weight):
        # Check wheter a bird can fly or not
        half_weight = weight / 2
        if(feathers_weight >= half_weight):
            print("Cannot Fly")
        else:
            print("Can fly")        


crow = Bird(2.3, 0.5, 0.3, "black", True, "Crow")
print(crow.name)
print(crow.weight)

crow.canfly(crow.weight, crow.feather_weight)


pigeon = Bird(2.3, 0.5, 0.1, "white", True, "Pigeon")