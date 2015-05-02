def tail(items):
    result = []

    for index in range(1, len(items)):
        item = items[index]
        result += [item]
    return result
items = [1,2,3,4]
print(tail(items))