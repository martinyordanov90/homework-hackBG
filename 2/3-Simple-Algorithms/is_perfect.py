start = 1
n = input("Enter number: ")
n = int(n)

divisors_sum = 0

while start <= n - 1:
    if n % start == 0:
        divisors_sum += start
    start += 1


if divisors_sum == n:
    print(str(n) + " is perfect!")
else:
    print(str(n) + " is not perfect")
