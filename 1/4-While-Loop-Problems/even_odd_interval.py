lower_bound = input("Enter lower bound for interval: ")
upper_bound = input("Enter upper bound for interval: ")

lower_bound = int(lower_bound)
upper_bound = int(upper_bound)

while lower_bound <= upper_bound:
    
    n = lower_bound

    if n % 2 == 0:
        print(str(n) + " - even")
    else:
        print(str(n) + " - odd")


    lower_bound += 1
