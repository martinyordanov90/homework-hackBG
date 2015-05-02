a = input("Enter number: ")
a = int(a)

total_sum = 0

while a != 0:
    digit = a % 10
    total_sum += digit
    a = a // 10
print(total_sum)
