def count_item(n, numbers):
    count = 0
    for number in numbers:
        if n == number:
            count += 1
    return count
n = 2
numbers = [1,2,2,2,2,2,2,3,4,5]
print(count_item(n,numbers))