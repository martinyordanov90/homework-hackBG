def leet_alphabet(string):
    string = string.tolower
    result = ""
    normal = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    leet = ["@","|3","(","|)","3","|=","6","]-[","][","_|","|{","|_","|\/|","|\|","[]","|D","(,)","|2","$","']['","|_|","\/","\/\/","}{","`/","(\)"]
    for ch in range(0, len(normal)):
        if ch == leet[index]:
            result += ch
    return result
a = "I drive a car"
print(leet_alphabet(a))