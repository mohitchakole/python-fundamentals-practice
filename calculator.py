operator = input(f"enter operator(+,-,*,/):")
num1 = float(input("enter the first number:"))
num2 = float(input("enter the second number:"))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2

print(f"the result = {result}")