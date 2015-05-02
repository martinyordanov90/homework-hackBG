def take(n, items):
    result = []

    for index in range(0, min(n, len(items))):
        result += [items[index]]
    return result
n = 3
items = [1,2,3,4]
print(take(n,items))
