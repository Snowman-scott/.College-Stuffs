num1 = int(input("Enter a number: "))
num2 = int(input("Enter Another number: "))

operations=["*","+","/","-"]
answers = []

for op in operations:
    if op == "*":
        answers.append(num1 * num2)
    elif op == "+":
        answers.append(num1 + num2)
    elif op == "-":
        answers.append(num1 - num2)
    elif op == "/":
        answers.append(num1 / num2)

for item in answers:
    print(item)
