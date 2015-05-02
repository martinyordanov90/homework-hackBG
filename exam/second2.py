def second_largest(numbers):
    result = []
    
    for number in numbers:
        if number not in result:
            result.append(number)
    
    if len(numbers) <= 1:
        return False

    result = sorted(result)[-2]
    
    return result

number = [5,5,4]
print(second_largest(number))

