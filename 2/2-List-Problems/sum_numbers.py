a = input("Enter number: ")
a = int(a)

count = 1
total_sum = 0

while count <= a:
    number = input("Enter number: ")
    number = int(number)
    total_sum = total_sum + number
    count += 1
print("Total sum: " + str(total_sum))
