def join(delimiter, items):
    result = ""
    last_index = len(items) - 1
    for index in range(0, last_index):
        item = items[index]
        result = result + item + delimiter
    result += items[last_index]
    return result

print(join("!!", ["Kuche", "Kotka", "Slon"]))
