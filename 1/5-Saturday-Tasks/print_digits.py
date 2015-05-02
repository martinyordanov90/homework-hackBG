a = input("Enter number: ")
a = int(a)

while a != 0:
    digit = a % 10
   
    print(digit)
    
    a = a // 10
