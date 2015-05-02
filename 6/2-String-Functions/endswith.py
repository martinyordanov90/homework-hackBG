def endswith(search, string):
    search = str_reverse(search)
    string = str_reverse(string)

    return startswith(search,string)