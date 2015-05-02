def divisors(n):
    result = []

    start = 1
    
    while start < n:
        if n % start == 0:
            result = result + [start]

        start += 1

    return result


n = 3456

print(divisors(n))