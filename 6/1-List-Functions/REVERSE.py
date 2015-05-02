def reverse(items):
    result = []
    last_index = len(items) - 1

    while last_index >= 0:
        result += [items[last_index]]
        last_index -= 1
    return result

numbers = [1,2,3,4,5]
print(reverse(numbers))