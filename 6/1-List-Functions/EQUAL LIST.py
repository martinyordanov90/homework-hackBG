
def equal_list(l1,l2):
    if len(l1) != len(l2):
        return False
    for index in range(0, len(l1)):
        if l1[index] != l2[index]:
            return False
    return True
print(equal_list([2,3,4],[2,3,4]))