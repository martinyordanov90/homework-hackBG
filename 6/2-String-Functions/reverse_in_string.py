def reverse_string(word):
    result = ""
    index = len(word) - 1
    
    while index >= 0:
        result += word[index] # pribavqme index ot word
        index -= 1
    return result
word = "asd"
print(reverse_string(word))

def reverse(items):
    result = []

    for item in items:
        result = [item] + result

    return result
say = "Pesho"
print(reverse(say))