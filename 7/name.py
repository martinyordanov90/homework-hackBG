def taken_name(surname_husband, surname_wife):
    if surname_wife in surname_husband + "a":
        return True
    else:
        return False
name_1 = "Ivanov"
name_2 = "Ivanova"
print(taken_name(name_1,name_2))

