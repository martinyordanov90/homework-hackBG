def decode_word(encrypted_word, cypher):
    result = ""
    new_cypher = {}
    
    for key in cypher:
        value = cypher[key]
        new_cypher[value] = key
    for j in encrypted_word:
       	if j in new_cypher:
        	result += new_cypher[j]
    return result
print(decode_word("mjriew", {'h': 'i', 'y': 'j', 'o': 'e', 't': 'r', 'n': 'w', 'p': 'm'}))
print(decode_word("rpf", {'m': 'p', 'o': 'r', 'g': 'f'}))
print(decode_word("wfhsftzzuys", {'r': 'f', 'o': 'h', 'i': 'u', 'm': 'z', 'g': 's', 'a': 't', 'p': 'w', 'n': 'y'}))
print(decode_word("bbbbbbbbbbbbbbbbbbbbbbbbbbb", {'a': 'b'}))

