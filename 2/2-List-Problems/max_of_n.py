n = input("Enter number: ")
n = int(n)

count = 1
current_max = 0

while count <= n:
    number = input("Enter number: ")
    number = int(number)
    if number > current_max:
        current_max = number
    count += 1
print("Max is:" + str(current_max))
