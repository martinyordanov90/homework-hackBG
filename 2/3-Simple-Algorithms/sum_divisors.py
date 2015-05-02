start = 1
n = input("Enter number: ")
n = int(n)
total_sum = 0
while start <= n - 1:
    if n % start == 0:
        total_sum += start
    start += 1
print(total_sum)
