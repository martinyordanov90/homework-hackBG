def setify(a):
    result = []
    
    for number in a:
        if number not in result:
            result.append(number)
    return result


def diff(a, b):
    result = []
    for number in a:
        if number not in b:
            result.append(number)
    return setify(result)

def union(a, b):
    return setify(a + b)


def intersection(a, b):
    result = []
    for number in a:
        if number in b:
            result.append(number)
    return setify(result)


def cartesian_product(list1, list2):
    # Tuple is (a, b) as a syntax
    result = []
    for x in list1:
        for y in list2:
            result.append((x, y))
    return setify(result)


def main():
    print(setify([0, 1, 1, 5, 5, 6]) == [0, 1, 5, 6])
    print(union([0, 0, 0, 0, 0], [1, 2]) == [0, 1, 2])
    print(intersection([0, 0, 1, 2, 5], [5, 5, 6]) == [5])
    print(diff([0, 1, 2, 3, 4, 5], [0, 0, 1, 1, 2, 2, 3, 3]) == [4, 5])
    print(cartesian_product([0, 1], [1]) == [(0, 1), (1, 1)])


if __name__ == '__main__':
    main()