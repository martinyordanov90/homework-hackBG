def tail(items):
    result = []

    for index in range(1, len(items)):
        item = items[index]
        result += [item]
    return result
print(tail("Georgi"))