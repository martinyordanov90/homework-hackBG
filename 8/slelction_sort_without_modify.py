def diff(items1,items2):
    result = []
    for a in items1:
        if a not in items2:
            result.append(a)
    return result