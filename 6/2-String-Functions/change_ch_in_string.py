def change_at(index, ch, string):
    result = ""
    n = len(string)

    for str_index in range(0, n):
        if str_index == index:
            result += ch
        else:
            result += string[str_index]

    return result
index = 2
ch = "w"
string = "Ivan"
print(change_at(index,ch,string))