n = input("Enter n: ")
n = int(n)

start = 0
even_count = 1

while start < n:
    number = input()
    number = int(number)
    
    if number % 2 == 0:

        even_count += 1

    start += 1
print("Event count: " + str(even_count))
