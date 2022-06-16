num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
operand = input("Enter the operand (+,-,*,/) :  ")

def add(num1, num2):
    result = num1+num2
    return result

def subtract(num1, num2):
    result = num1-num2
    return result

def product(num1, num2):
    result = num1*num2
    return result
def division(num1, num2):
    result = num1/num2
    return result

if operand == "+":
    print(add(num1,num2))
elif operand == "-":
    print(subtract(num1,num2))
elif operand == "*":
    print(product(num1,num2))
elif operand == "/":
    print(division(num1,num2))
else:
    print("invalid operaor")