def reverse_int(n):
    
    return to_number(revers_list(to_digits(n)))

def reverse_int2(n):
    result = 0

    while n != 0:
        digit = n % 10
        result = result * 10 + digit
        n = n // 10
    
    return  result

def sum_digits(n):
    total_sum = 0

    while n != 0:
        digit = n % 10
        total_sum = total_sum + digit
        n = n // 10
    return total_sum

def multiple_digits(n):
    digits_multi = 1

    while n != 0:
        digit = n % 10
        digits_multi = digits_multi * digit
        n = n // 10
    return digits_multi

a = 7

print(reverse_int2(a))
print(sum_digits(a))
print(multiple_digits(a))
