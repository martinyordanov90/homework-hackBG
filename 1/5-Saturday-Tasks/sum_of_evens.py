a = 1

b = input("Enter number: ")
b = int(b)
total_sum = 0

while a <= b:
    if a % 2 == 0:
        total_sum += a
    a += 1
print(total_sum)
