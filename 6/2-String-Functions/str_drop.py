def str_drop(n, string):
    result = ""

    for index in range(n,len(string)):
        result += string[index]
    return result
n = 2 
string = "asdfgh"
print(str_drop(n,string))