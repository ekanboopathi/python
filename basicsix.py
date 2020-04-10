'''
    Functions example program
'''
# execution starts at main
# Calculator
# define a method
def main():
    # Input - 
    operand1 = float(input("Enter the value 1: "))
    operand2 = float(input("Enter the value 2: "))
    operator = input("Enter the operator: (+, -, /, *) ")
    if operator == '+': 
        val = sum(operand1, operand2)
        print(f"The output is: {val}")
    elif operator == '-':
        val = sub(operand1, operand2)
        print(f"The output is: {val}")
    elif operator == '*':
        val = mul(operand2, operand2)
        print(f"The output is: {val}")
    elif operator == '/':
        val = div(operand1, operand2)
        print(f"The output is: {val}")
    else:
        print("No operator found, Please try only these +, -, /, *")


# +, -, /, *
# addition
def sum(operand1, operand2):
    return operand1 + operand2

# Subtraction
def sub(operand1, operand2):
    return operand1 - operand2

# Division
def div(operand1, operand2):
    return operand1 / operand2

# multiplication
def mul(operand1, operand2):
    return operand1 * operand2

# Main Method    
if(__name__ == '__main__'):
    # Call method
    main()

