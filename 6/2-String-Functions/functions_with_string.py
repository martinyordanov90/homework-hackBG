def string_to_char(string):
    result = []

    for ch in string:
        result += [ch]
    
    return result
print(string_to_char("Python"))

def char_list_to string(char_list):
    result = ""

    for ch in char_list:
        result += ch

    return resultd ()

def change_string(index, ch, string):
    char_list = string_to_char+list(string)

    char_list[index] = ch
    return char_list_to_string(char_list)

def reverse(items):
    result = []

    for item in items:
        result = [item] + result
    return result
def str_reverse(string):
    char_list = string_to_char_list(string)
    char_list = reverse(char_list)
    return char_list_to_string(char_list)
def str_reverse2(string):
    result = ""

    for ch in string:
        result = ch + result
    return result
print(str_reverse2("Python"))