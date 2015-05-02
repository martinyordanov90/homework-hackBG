def min_element(numbers):
    min_index = 0
    index = 0
    for number in numbers:
        if number < numbers[min_index]:
            min_index = index
        index += 1
    return min_index

def basic_sort(numbers):
    result = []
    n = len(numbers)
    while len(result) != n:
        min_index = min_index(numbers)
        result.append(numbers[min])
        del numbers[min]
    return result
list = [1,3,2,31,2,3,0,4,5]
print(min_element(list))
print(basic_sort(list))

