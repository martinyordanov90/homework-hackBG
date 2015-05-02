a = input("Enter number: ")
a = int(a)

b = input("Enter number: ")
b = int(b)

oper = input("Enter operation: ")

if oper == "+":
    print("Result is: " , a + b)
elif oper == "-":
    print("Result is: " , a - b)
elif oper == "*":
    print("Result is: ", a * b)
elif oper == "/":
    print("Result is:", a / b)
else:
    print("We don't support that operation.")
