n = input("Enter number: ")
n = int(n)

count = 1
current_min = 0

while count <= n:
    number = input("Enter number: ")
    number = int(number)
    if number < current_min:
        current_min = number
    count += 1
print("Min is: " + str(current_min))
