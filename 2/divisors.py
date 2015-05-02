n = input("Enter fucking number: ")
n = int(n)

digits = []

while n != 0:
    digit = n % 10
    digits = [digit] + digits
    n = n // 10

has_prime_digit = False

for digit in digits:
    if n % 10 == 0:
        print("at least has one price digit")
else:
    print("no prime digit")
