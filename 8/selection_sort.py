def min_element(start_index,numbers):
    min_index = start_index
    for index in range(start_index, len(numbers)):
        if numbers[index] < numbers[min_index]:
            min_index = index
        index += 1
    return min_index

def swap(index1,index2,numbers):
    temp = numbers[index2]
    numbers[index2] = numbers[index1]
    numbers[index1] = temp


def selection_sort(numbers):
    for i in range(0,len(numbers)):
        min = min_element(i, numbers)
        swap(i, min, numbers)
    return numbers
a = [2, 0, -10,-100,200,540,3213,432]
print(a)
print(selection_sort(a))
print(a)