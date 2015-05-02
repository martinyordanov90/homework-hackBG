M = input("Enter number: ")
M = int(M)

N = input("Enter number: ")
N = int(N)

lower_bound = 0
upper_bound = 0

if N < M:
    lower_bound = N
    upper_bound = M
else:
    lower_bound = M
    upper_bound = N

start = lower_bound

while start <= upper_bound:
    n = start
    total_sum = 0
    while n != 0:
        digit = n % 10
        total_sum = total_sum + digit
        n = n // 10
    print("total_sum of digits of" + str(start) +" = "+ str(total_sum))
    start += 1
