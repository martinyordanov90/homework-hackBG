def count_zero_neighbours(numbers):
    index = 0
    count = 0
    for number in numbers:
        if index < len(numbers) - 1:
            neighbour = numbers[index + 1]

            if number + neighbour == 0:
                count += 1
        index += 1
            
    return count
a = [0, 1, -1, 2, -2, 0, 0, 5, -5]
print(count_zero_neighbours(a))
