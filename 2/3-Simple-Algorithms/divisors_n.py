start = 1
n = input("Enter number: ")
n = int(n)

while start <= n - 1:
    if n % start == 0:
        print(start)
    start += 1

    
