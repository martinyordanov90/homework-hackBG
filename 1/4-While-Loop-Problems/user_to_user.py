a = input("Enter number: ")
a = int(a)

b = input("Enter number: ")
b = int(b)

if a < b:
    while a <= b:
        print(a)
        a += 1
else:
    while b <= a:
        print(b)
        b += 1
