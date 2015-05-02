n = input("Enter number: ")
n = int(n)

m = input("Enter number: ")
m = int(m)

n_remainder = n % 10
m_remainder = m % 10

if n_remainder > m_remainder:
    print(str(n_remainder) + " " + "number is bigger than" + " " + str(m_remainder))
elif m_remainder > n_remainder:
    print(str(m_remainder) + " " + "number is bigger than" + " " + str(n_remainder))
else:
    if n > m:
        print(n)
    else:
        print(m)
