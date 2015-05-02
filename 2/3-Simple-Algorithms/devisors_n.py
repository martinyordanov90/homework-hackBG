n = input("Enter n: ")
n = int(n)

divisors = []

start = 1
end = n - 1

while start <= end:
    if n % start == 0:
        divisors = divisors + [start]

    start += 1

divisors_sum = 0

for divisor in divisors:
    divisors_sum += divisor

print(divisors_sum)
