# Condition
# if elif else
# ternary operator

'''
    Condition: 
    Syntax = 
    if(expression(true or false)):
        .....
    else:
        .....
'''
a = 10
b = 12
if(a > b):
    print("Yes a is greator than b")
else:
    print("No")

name = "udhay"

if(name == "udhay"): # 0.4 s
    print("True 1")
if(name == "udhaya"): # 0.4 s
    print("True 2")
if(name == "udhayas"): # 0.4 s
    print("True 3")
if(name == "uday"):  # 0.4 s
    print("True 4")

# 1.6 s

if(name == "udhay"): # 0.4 s
    print("True 1")
elif(name == "udhaya"): 
    print("True 2")
elif(name == "udhayas"): 
    print("True 3")
elif(name == "udhay"):  
    print("True 4")
else:
    print("Nothing matched")

# 0.4 s

# project
# BMI Calculator
# weight in kg / height in m2 * height in m2
# 85 / 1.77 * 1.77

# bmi 
'''
    bmi - 19 > lean body
    bmi - 19 - 24  normal body
    bmi -  > 24 < 27 fat body
    bmi - > 27 - obese 
'''
# float - 80 .80.0
weight = float(input("Enter your weight? "))
height = float(input("Enter your height? "))
height_in_meter_square = height * height
print(height_in_meter_square)
bmi = weight / height_in_meter_square
print(bmi)
if(bmi < 19):
    print("lean body")
elif(bmi >= 19 and bmi <= 24):
    print("normal body")
elif(bmi > 24 and bmi <= 27):
    print("Fat body")
elif(bmi > 27):
    print("obese body")
else:
    print("Values does not fit for humans")