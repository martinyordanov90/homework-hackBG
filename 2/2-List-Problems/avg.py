a = input("Enter number: ")
a = int(a)

count = 1
total_sum = 0
avg = 0

while count <= a:
    number = input("Enter number :")
    number = int(number)
    total_sum += number
    count += 1
avg = total_sum / a
print(avg)
