def string_to_char_list(string):
    result = []

    for ch in string:
        result += ch

    return result
a = "Matei"
print(string_to_char_list(a))