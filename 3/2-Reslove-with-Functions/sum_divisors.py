def divisors(n):
    result = []

    start = 1

    while start <= n:
        if n % start == 0:
            result = result + [start]

        start += 1

    return result

def sum_ints(numbers):
    result = 0

    for number in numbers:
        result += number

    return result

n = 123

print(sum_ints(divisors(n)))