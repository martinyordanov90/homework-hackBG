def index_in(index, items):
        
    
    return index < len(items) and index >= 0
def hash_them(keys,values):
    result = {}

    index = 0
    for key in keys:
        if index_in(index, values):
            result[key] = values[index]
        else:
            result[key] = None
        index += 1
        
    return result

a = hash_them(["name", "age"],["Ivan", 23])
print(a)
