# calculator (functions)
import os

print("This calculator has functions: \nIf you want the Area of a Triangle you need 2 numbers and need to type into operator: Aot\nFor the Area of a circle you need 1 numbers and need to type into operator: Aoc\nFor area of a rectangle you need 2 numbers and need to type into operator: Aor\n")

print("For Aot put in number 1 as the base and 2 as the height\nFor Aoc Type in number 1 as the Radius and leve 2 blank\nFor Aor Type number 1 As length and numbner 2 as the Width\n")

def calculator():
    number = input("How many numbers do you need: ")
    if number == "1":
        num = int(input("Enter your first number: "))
    elif number == "2":
        num = int(input("Enter your first number: "))
        num2 = int(input("Enter your Second number: "))
    elif number == "3":
        num = int(input("Enter your first number: "))
        num2 = int(input("Enter your Second number: "))
        num3 = (int(input("Enter your third number: ")))
    op = input("Enter an operator: ")

    if op == "+":
        print(Addition(num,num2,num3))
    elif op == "-":
        print(Subtraction(num,num2,num3))
    elif op == "*":
        print(Multiplication(num,num2,num3))
    elif op == "/":
        print(Division(num, num2,num3))
    elif op == "Aot":
        print(Aoat(num, num2))
    elif op == "Aoc":
        print(Aoac(num))
    elif op == "Aor":
        print(Aoar(num, num2))

def Addition(num,num2,num3):
    return num + num2 +num3
    
def Subtraction(num , num2,num3):
    return num - num2
    
def Multiplication(num, num2,num3):
    return num * num2
    
def Division(num, num2,num3):
    return num / num2

def Aoat(num, num2 ,num3):
    return 1/2 * num * num2

def Aoac(num):
    return 3.14159 * num**2

def Aoar(num, num2):
    return num * num2

calculator()

