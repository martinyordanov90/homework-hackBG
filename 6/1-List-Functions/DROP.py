def drop(n,items):
    result = []
    for index in range(n, len(items)):
        result = result + [items[index]]
    return result

n = 2
numbers = [1,2,3,4,5]
print(drop(n, numbers))
