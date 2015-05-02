n = input("Enter number: ")
n = int(n)

digits = []

while n != 0:
    digit = n % 10
    digits = [digit] + digits
    n = n // 10
print(digits)
