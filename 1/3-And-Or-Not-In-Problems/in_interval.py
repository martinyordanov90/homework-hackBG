a = input("Enter lowest number: ")
a = int(a)

b = input("Enter biggest number: ")
b = int(b)

x = input("Enter number: ")
x = int(x)

if x == a:
    print("The number is equal to the lower bound of the interval")
elif x == b:
    print("The number is equal to the upper bound of the interval")
elif x > a and x < b:
    print("The number is in the interval")
elif x < a:
    print("The number is outside the interval, x < a")
elif x > b:
    print("The number is outside the interval, x > b")
