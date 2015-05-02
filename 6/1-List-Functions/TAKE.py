def take(n, list):
    result = []
    
    if n > len(list):
        n = len(items)
    for index in range(0, min(n, len(list))):
        result = result + [list[index]] #(first take element(index 0) = 1,
                                        #(after take element(index 1) = 2,....))


    return result
n = 3
numbers = [1,2,3,4,5]
print(take(n, numbers))