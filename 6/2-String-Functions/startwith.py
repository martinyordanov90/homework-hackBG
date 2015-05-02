def take(n, items):
    result = []

    for index in range(0, min(n, len(items))):
        result += [items[index]]

    return result


def startswith(search, string):
    n = len(search)
    search_char_list = string_to_char_list(search)
    return take(n, string) == search_char_list


def endswith(search, string):
    search = str_reverse(search)
    string = str_reverse(string)

    return startswith(search, string)