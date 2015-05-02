def str_drop(n, string):
    result = ""
    for index in range(n,len(string)):
        result += string[index]

    return result

def trim_left(string):
    while startwith(search,string):
        string = str_drop(1, string)

    return string

def trim_right(string):
    return str_reverse(trim_left(str_reverse(string)))