def count_words(words):
    result = {}

    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result

a = count_words(["apple", "banana", "apple", "banana", "pomegranade", "pomegranade"])
print(a)
