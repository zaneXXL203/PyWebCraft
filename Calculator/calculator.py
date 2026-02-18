


# user enters a number follow by an operator and then a number
# get the number before the operator and calculate it with the number after the operator
# then calculate the number and then print it
# loop it till they type cancel


print("CALCULATOR + - * /")

operator = input("+ - * /: ")
num1 = int(float(input("CALCULATE: ")))
num2 = int(float(input("CALCULATE: ")))


if operator == "+":
    result = num1 + num2
    print(result) 
elif operator == "-":
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print("INVALID INPUT!")
    



